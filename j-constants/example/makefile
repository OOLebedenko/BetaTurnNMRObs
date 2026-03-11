include common.mk

data/j_consts/*csv:  ${SCRIPT_DIR}/calc_j_constant.py data/dihedral_angles/*.csv
	python3 "$<" \
	    --path-to-dihedral-angles-dir="data/dihedral_angles"\
	    --output-directory="data/j_consts"

data/dihedral_angles/*.csv: ${SCRIPT_DIR}/extract_dihedral_angles.py
	python3 "$<" \
	    --path-to-trajectory-dir="${PATH_TO_TRAJECTORY}"\
	    --path-to-pdb-reference="${REFERENCE_PDB_PATH}" \
	    --trajectory-length="${TRAJECTORY_LENGTH}" \
	    --trajectory-stride="${TRAJECTORY_STRIDE}" \
	    --dt-ns="${DT_NS}" \
	    --output-directory="data/dihedral_angles"