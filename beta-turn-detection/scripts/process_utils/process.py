import os
import subprocess
import sys

from pyxmolpp2 import Frame
from pyxmolpp2.pipe import TrajectoryProcessor


class RunnerBetaTurn18(TrajectoryProcessor):

    def __init__(self,
                 path_to_betaturn18_py2,
                 outdir: str = ".",
                 ):
        self.path_to_betaturn18_py2 = path_to_betaturn18_py2
        self.outdir = outdir

    def before_first_iteration(self, frame: Frame) -> None:
        os.makedirs(self.outdir, exist_ok=True)

    def __call__(self, frame: Frame) -> None:
        frame.to_pdb(f"frame{frame.index:05d}.pdb")
        subprocess.call(
            [sys.executable, self.path_to_betaturn18_py2, "-i", f"frame{frame.index:05d}.pdb",
             "-o", os.path.join(self.outdir, f"frame{frame.index:05d}.out")])
        os.remove(f"frame{frame.index:05d}.pdb")
