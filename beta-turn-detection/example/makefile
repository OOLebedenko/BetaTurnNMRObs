include common.mk

all: data/*csv

clean:
	rm -rf data

data/*csv: ${SCRIPT_DIR}/collect_betaturn18_results.py data/betaturn18/*.out
	python3 "$<" \
		--path-to-betaturn18-outdir="data/betaturn18" \
		--output-directory="data/"

data/betaturn18/*.out: ${SCRIPT_DIR}/run_betaturn18.py
	python3 "$<" \
		--path-to-betaturn18-py2="${PATH_TO_BETATURN18_PY2}" \
		--path-to-trajectory-dir="${PATH_TO_TRAJECTORY}" \
		--path-to-pdb-reference="${REFERENCE_PDB_PATH}" \
		--trajectory-length="${TRAJECTORY_LENGTH}" \
		--trajectory-stride="${TRAJECTORY_STRIDE}" \
		--output-directory="data/betaturn18"