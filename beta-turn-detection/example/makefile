include common.mk

data/betaturn18/*.csv: ${SCRIPT_DIR}/run_betaturn18.py
	python3 "$<" \
		--path-to-betaturn18-py2="${PATH_TO_BETATURN18_PY2}" \
		--path-to-trajectory-dir="${PATH_TO_TRAJECTORY}" \
		--path-to-pdb-reference="${REFERENCE_PDB_PATH}" \
		--trajectory-length="${TRAJECTORY_LENGTH}" \
		--trajectory-stride="${TRAJECTORY_STRIDE}" \
		--output-directory="data/betaturn18"