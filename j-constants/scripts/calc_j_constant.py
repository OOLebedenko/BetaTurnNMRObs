import argparse
import os
import pandas as pd

from glob import glob
from tqdm import tqdm

from process_utils.calc import calc_j_c_c, calc_j_hn_ha, calc_j_hn_ha_gly, calc_j_c_c_gly

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Calc J(HN-HA) and J(C-C) constants')
    parser.add_argument('--path-to-dihedral-angles-dir', required=True)
    parser.add_argument('--output-directory', default=".")
    args = parser.parse_args()

    dihedral_csvs = glob(os.path.join(args.path_to_dihedral_angles_dir, "*.csv"))
    dihedral_csvs.sort()

    for dihedral_csv in tqdm(dihedral_csvs, desc="Calculation j-consts"):
        resname = os.path.basename(dihedral_csv)
        df_dihedral = pd.read_csv(dihedral_csv)
        phi_array = df_dihedral["phi"].values

        if "GLY" in resname:
            j_hn_ha = calc_j_hn_ha_gly(phi_array=phi_array)
            j_c_c = calc_j_c_c_gly(phi_array=phi_array)
        else:
            j_hn_ha = calc_j_hn_ha(phi_array=phi_array)
            j_c_c = calc_j_c_c(phi_array=phi_array)

        os.makedirs(args.output_directory, exist_ok=True)
        pd.DataFrame({"time_ns": df_dihedral["time_ns"], "J-HN-HA": j_hn_ha, "J-C-C": j_c_c}).to_csv(
            os.path.join(args.output_directory, os.path.basename(dihedral_csv)), index=False)
