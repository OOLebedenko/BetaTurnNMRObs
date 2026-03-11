import numpy as np
from numpy.typing import NDArray
import math

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
    j_hn_ha = []
    for phi in phi_array:
        phi_rad = math.radians(phi)
        theta_rad = phi_rad - math.radians(60)
        j = 7.97 * math.cos(theta_rad) ** 2 - 1.26 * math.cos(theta_rad) + 0.63
        j_hn_ha.append(j)
    return np.array(j_hn_ha, dtype=np.float64)



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
    j_c_c = []
    for phi in phi_array:
        phi_rad = math.radians(phi)
        j = 1.61 * math.cos(phi_rad) ** 2 - 0.93 * math.cos(phi_rad) + 0.55
        j_c_c.append(j)
    return np.array(j_c_c, dtype=np.float64)


def calc_j_hn_ha_gly(phi_array: NDArray[np.float64]) -> NDArray[np.float64]:
    """
    Calculate J_HN-HA coupling constants for glycine residues based on phi angles.

    Parameters
    ----------
    phi_array : NDArray[np.float64]
        Input array of phi dihedral angles (in degrees).
        Expected to be a 1D array of float64 values in range [-180, 180].

    Returns
    -------
    NDArray[np.float64]
        Array of calculated J_HN-HA coupling constants (in Hz)
        with the same shape as input.

    Notes
    -----
    J_HN-HA represents the three-bond vicinal coupling constant between
    amide proton and alpha proton in glycine residues. The calculation
    uses a modified Karplus relation specific for glycine due to its
    two alpha protons and lack of beta carbon.

    Examples
    --------
    >>> phi = np.array([-180, -120, -60, 0, 60, 120, 180])
    >>> j_hn_ha_gly = calc_j_hn_ha_gly(phi)

    >>> # Continuous range example
    >>> phi = np.linspace(-180, 180, 200)
    >>> j_hn_ha = calc_j_hn_ha_gly(phi)
    """
    j_hn_ha = []
    for phi in phi_array:
        phi_rad = math.radians(phi)
        j = 8.09 * math.cos(phi_rad) ** 2 + 1.00 * math.cos(phi_rad) + 1.01
        j_hn_ha.append(j)
    return np.array(j_hn_ha, dtype=np.float64)


def calc_j_c_c_gly(phi_array: NDArray[np.float64]) -> NDArray[np.float64]:
    """
    Calculate J_C-C coupling constants for glycine residues based on phi angles.

    Parameters
    ----------
    phi_array : NDArray[np.float64]
        Input array of phi dihedral angles (in degrees).
        Expected to be a 1D array of float64 values in range [-180, 180].

    Returns
    -------
    NDArray[np.float64]
        Array of calculated J_C-C coupling constants (in Hz)
        with the same shape as input.

    Notes
    -----
    J_C-C represents the three-bond vicinal coupling constant between
    carbonyl carbon and alpha carbon in glycine residues. The calculation
    uses a Karplus-type parametrization specific for glycine, accounting
    for its unique structural features.

    Examples
    --------
    >>> phi = np.array([-180, -135, -90, -45, 0, 45, 90, 135, 180])
    >>> j_c_c_gly = calc_j_c_c_gly(phi)

    >>> # Continuous range example
    >>> phi = np.linspace(-180, 180, 100)
    >>> j_c_c = calc_j_c_c_gly(phi)
    """
    j_c_c = []
    for phi in phi_array:
        phi_rad = math.radians(phi)
        j = 1.73 * math.cos(phi_rad) ** 2 + 1.08 * math.cos(phi_rad) + 0.28
        j_c_c.append(j)
    return np.array(j_c_c, dtype=np.float64)
