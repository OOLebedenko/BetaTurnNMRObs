from pyxmolpp2 import Frame, TorsionAngleFactory
from pyxmolpp2.pipe import TrajectoryProcessor
from typing import List, Callable, Optional


class ExtractDihedrals(TrajectoryProcessor):
    """
    A trajectory processor for extracting and writing dihedral angles to files.
    This processor extracts specified dihedral angles for each selected residue in every
    frame of a trajectory and writes the values to separate files (one per residue) using
    a user-provided writer class.

    Attributes
    ----------
    angle_names : List[str]
        Names of the dihedral angles to extract (e.g., 'phi', 'psi', 'chi1')
    writer : class
        Writer class used to create output files and write data
    residue_selector : Optional[Callable]
        Function to filter residues for angle extraction
    filename_provider : Callable
        Function that generates filenames for each residue's output file
    outdir : str
        Output directory where files will be written (default: ".")

    Notes
    -----
    The processor follows the TrajectoryProcessor protocol with three main phases:
    1. `before_first_iteration`: Initializes writers and selects residues
    2. `__call__`: Processes each frame, extracting and writing dihedral values
    3. `after_last_iteration`: Cleans up and closes all writers

    For each selected residue, a separate file is created using the `filename_provider`
    function to generate the filename. If a dihedral angle cannot be computed for a
    residue (e.g., missing atoms), None is written instead.
    """

    def __init__(self,
                 angle_names: List[str],
                 writer,
                 filename_provider: Callable,
                 dt_ns: float,
                 outdir: str = ".",
                 residue_selector: Optional[Callable] = None):
        """
        Initialize the ExtractDihedrals processor.

        Parameters
        ----------
        angle_names : List[str]
            List of dihedral angle names to extract. Common names include:
            - 'phi' (backbone phi angle)
            - 'psi' (backbone psi angle)
            - 'omega' (backbone omega angle)
            - 'chi1', 'chi2', etc. (side chain dihedrals)
            These names must be recognized by TorsionAngleFactory.

        writer : class
            A writer class that implements:
            - __init__(outdir: str, filename: str) -> writer instance
            - header(names: List[str]) -> None  # writes header row
            - writerow(values: List[float]) -> None  # writes data row
            - close() -> None  # closes the file

        filename_provider : Callable[[Any], str]
            A function that takes a residue object and returns a filename (without path).
            Example:
            >>> def name_provider(residue):
            ...     return f"residue_{residue.id.serial}.dat"


        dt_ns : float
            Time step in nanoseconds between trajectory frames. This value is used to:
            - Calculate actual time points for each frame when writing output
            - Provide time information to the writer for time-series data
            - Ensure consistent time scaling across all output files
            The time for frame i is calculated as i * dt_ns nanoseconds.

        outdir : str, optional
            Directory where output files will be created (default: ".")

        residue_selector : Callable[[Residue], bool], optional
            A function that returns True for residues to process, False to skip.
            If None, all residues in the frame are processed.
            Example:
            >>> def selector(residue):
            ...     return residue.name == "ALA"  # only alanines
        """
        self.angle_names = angle_names
        self.writer = writer
        self.residue_selector = residue_selector
        self.filename_provider = filename_provider
        self.outdir = outdir
        self.dt_ns = dt_ns
        self._residue_writers_pairs = []  # Internal storage for (residue, writer) pairs

    def before_first_iteration(self, frame: Frame) -> None:
        """
        Prepare writers before processing the first frame.

        This method is called automatically by the pipeline before the first frame.
        It selects residues based on the residue_selector and creates a writer
        instance for each selected residue.

        Parameters
        ----------
        frame : Frame
            First frame of the trajectory, used to access residue information.

        Notes
        -----
        This method creates self._residue_writers_pairs, a list of tuples
        (residue, writer) that will be used for all subsequent frames.
        The writers are initialized and headers are written during this phase.
        """
        # Filter residues if a selector is provided
        selected_residues = frame.residues.filter(self.residue_selector) if self.residue_selector else frame.residues

        self._residue_writers_pairs = []
        for residue in selected_residues:
            fname = self.filename_provider(residue=residue)
            angle_writer = self.writer(self.outdir, fname)
            angle_writer.header(["time_ns", *self.angle_names])
            self._residue_writers_pairs.append((residue, angle_writer))

    def __call__(self, frame: Frame) -> None:
        """
        Process a single trajectory frame.

        This method is called automatically by the pipeline for each frame.
        It extracts all specified dihedral angles for each selected residue
        and writes them to the corresponding files.

        Parameters
        ----------
        frame : Frame
            Current trajectory frame to process.

        Notes
        -----
        For each residue and angle name:
        1. Attempts to get the dihedral angle using TorsionAngleFactory
        2. If successful, converts the angle to standard range (0-360°) and degrees
        3. If the angle cannot be computed (e.g., missing atoms), writes None
        """
        for residue, writer in self._residue_writers_pairs:
            values = [frame.index * self.dt_ns]
            for angle_name in self.angle_names:
                angle = TorsionAngleFactory.get(residue=residue, angle_name=angle_name)
                if angle is None:
                    values.append("NA")
                else:
                    values.append(str(angle.value().to_standard_range().degrees))
            writer.writerow(values)

    def after_last_iteration(self, exc_type, exc_value, traceback) -> None:
        """
        Clean up after all frames have been processed.

        This method is called automatically by the pipeline after the last frame
        or if an exception occurs. It ensures all writers are properly closed.

        Parameters
        ----------
        exc_type : type or None
            Type of exception that occurred, or None if no exception
        exc_value : Exception or None
            Exception instance that occurred, or None if no exception
        traceback : traceback or None
            Traceback of the exception, or None if no exception

        Notes
        -----
        This method always attempts to close all writers, even if an exception
        occurred during processing. The exception parameters are ignored but
        maintained for compatibility with the TrajectoryProcessor protocol.
        """
        for _, writer in self._residue_writers_pairs:
            writer.close()
