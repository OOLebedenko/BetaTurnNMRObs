import os
import subprocess
import sys

from pyxmolpp2 import Frame
from pyxmolpp2.pipe import TrajectoryProcessor


class RunnerBetaTurn18(TrajectoryProcessor):

    def __init__(self,
                 path_to_betaturn18_py2,
                 dt_ns,
                 outdir: str = ".",
                 ):
        self.path_to_betaturn18_py2 = path_to_betaturn18_py2
        self.dt_ns = dt_ns
        self.outdir = outdir

    def before_first_iteration(self, frame: Frame) -> None:
        os.makedirs(self.outdir, exist_ok=True)

    def __call__(self, frame: Frame) -> None:
        basename = f"{round(frame.index * self.dt_ns, 3)}"
        frame.to_pdb(f"{basename}.pdb")
        subprocess.call(
            [sys.executable, self.path_to_betaturn18_py2, "-i", f"{basename}.pdb",
             "-o", os.path.join(self.outdir, f"{basename}.out")])
        os.remove(f"{basename}.pdb")
