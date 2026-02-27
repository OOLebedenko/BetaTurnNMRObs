import csv
import os

from pyxmolpp2 import Residue


def filename_provider(residue: Residue):
    return f"{residue.id.serial:02d}_{residue.name}.csv"


class CsvWriter:

    def __init__(self, out_dir, fname):
        os.makedirs(out_dir, exist_ok=True)
        self.file = open(os.path.join(out_dir, fname), "w")
        self.csv_file = csv.writer(self.file)

    def writerow(self, value_array):
        self.csv_file.writerow(value_array)

    def header(self, header):
        self.csv_file.writerow(header)

    def close(self):
        self.file.close()
