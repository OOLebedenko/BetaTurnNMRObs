include common.mk

data/dihedral_angles/*.csv: ${SCRIPT_DIR}/extract_dihedral_angles.py
	python3 "$<" \
	    --path-to-trajectory-dir="${PATH_TO_TRAJECTORY}"\
	    --path-to-pdb-reference="${REFERENCE_PDB_PATH}" \
	    --trajectory-length="${TRAJECTORY_LENGTH}" \
	    --trajectory-stride="${TRAJECTORY_STRIDE}" \
	    --output-directory="data/dihedral_angles"