import numpy as np
from numpy.typing import NDArray


def calc_j_hn_ha(phi_array: NDArray[np.float64]) -> NDArray[np.float64]:
    """
    Calculate J_hn_ha values based on the phi array.

    Parameters
    ----------
    phi_array : NDArray[np.float64]
        Input array of phi values (in degrees).
        Expected to be a 1D array of float64 values in range [-180, 180].

    Returns
    -------
    NDArray[np.float64]
        Array of calculated J_hn_ha values with the same shape as input.

    Notes
    -----
    J_hn_ha typically represents some physical quantity in the system.
    The calculation details should be specified in the implementation.

    Examples
    --------
    >>> phi = np.array([-180, -90, 0, 90, 180])
    >>> j_hn_ha = calc_j_hn_ha(phi)

    >>> # Continuous range example
    >>> phi = np.linspace(-180, 180, 100)
    >>> j_hn_ha = calc_j_hn_ha(phi)
    """
    ...


def calc_j_c_c(phi_array: NDArray[np.float64]) -> NDArray[np.float64]:
    """
    Calculate J_c_c values based on the phi array.

    Parameters
    ----------
    phi_array : NDArray[np.float64]
        Input array of phi values (in degrees).
        Expected to be a 1D array of float64 values in range [-180, 180].

    Returns
    -------
    NDArray[np.float64]
        Array of calculated J_c_c values with the same shape as input.

    Notes
    -----
    J_c_c typically represents some physical quantity in the system.
    The calculation details should be specified in the implementation.

    Examples
    --------
    >>> phi = np.array([-180, -135, -90, -45, 0, 45, 90, 135, 180])
    >>> j_c_c = calc_j_c_c(phi)

    >>> # Continuous range example
    >>> phi = np.linspace(-180, 180, 50)
    >>> j_c_c = calc_j_c_c(phi)
    """
    ...
