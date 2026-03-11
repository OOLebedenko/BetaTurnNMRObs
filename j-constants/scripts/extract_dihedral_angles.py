import argparse
import os

from tqdm import tqdm
from pyxmolpp2 import PdbFile, Trajectory, TrjtoolDatFile, AmberNetCDF
from pyxmolpp2.pipe import Run

from process_utils.extract import ExtractDihedrals
from process_utils.write import CsvWriter, filename_provider

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Extract dihedral angles')
    parser.add_argument('--path-to-trajectory-dir', required=True)
    parser.add_argument('--path-to-pdb-reference', required=True)
    parser.add_argument('--trajectory-start', default=1, type=int)
    parser.add_argument('--trajectory-length', required=True, type=int)
    parser.add_argument('--dt-ns', required=True, type=float)
    parser.add_argument('--filetype', choices=["dat", "nc"], default="nc")
    parser.add_argument('--filepattern', default="run%05d")
    parser.add_argument('--trajectory-stride', type=int, default=1)
    parser.add_argument('--output-directory', default=".")
    args = parser.parse_args()

    trj_reader_dict = {"dat": TrjtoolDatFile,
                       "nc": AmberNetCDF,
                       }

    # read trajectory
    trj_ref = PdbFile(args.path_to_pdb_reference).frames()[0]
    traj = Trajectory(trj_ref)
    for ind in tqdm(range(args.trajectory_start, args.trajectory_length + 1), desc="traj_reading"):
        fname = "{pattern}.{filetype}".format(pattern=args.filepattern, filetype=args.filetype)
        traj.extend(
            trj_reader_dict[args.filetype](os.path.join(os.path.join(args.path_to_trajectory_dir), fname % (ind))))

    traj_handler = ExtractDihedrals(angle_names=["phi", "psi"],
                                    writer=CsvWriter,
                                    filename_provider=filename_provider,
                                    dt_ns=args.dt_ns,
                                    outdir=args.output_directory
                                    )

    tqdm(traj[::args.trajectory_stride] | traj_handler) | Run()
