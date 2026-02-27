from pyxmolpp2 import Frame, TorsionAngleFactory
from pyxmolpp2.pipe import TrajectoryProcessor
from typing import List


class ExtractDihedrals(TrajectoryProcessor):

    def __init__(self,
                 angle_names: List[str],
                 writer,
                 filename_provider,
                 outdir=".",
                 residue_selector=None,
                 ):
        self.angle_names = angle_names
        self.writer = writer
        self.residue_selector = residue_selector
        self.filename_provider = filename_provider
        self.outdir = outdir

    def before_first_iteration(self, frame):
        selected_residues = frame.residues.filter(self.residue_selector) if self.residue_selector else frame.residues

        self._residue_writers_pairs = []
        for residue in selected_residues:
            fname = self.filename_provider(residue=residue)
            angle_writer = self.writer(self.outdir, fname)
            angle_writer.header(self.angle_names)
            self._residue_writers_pairs.append((residue, angle_writer))

    def __call__(self, frame: Frame):
        """Available attributes:
        - self.angle_names: List[str] - list of angle names
        - self._residue_writers_pairs: List[(Residue, writer)] - pairs of (residue, writer object)

        For each residue in self._residue_writers_pairs:
        1. Get angle values (using TorsionAngleFactory.get())
        2. Write them to the corresponding writer via writer.writerow(values)"""
        ...

    def after_last_iteration(self, exc_type, exc_value, traceback):
        for _, writer in self._residue_writers_pairs:
            writer.close()
