from pathlib import Path
import os
import pandas as pd


class FolderDB:
    def __init__(self, folder):
        self.folder = folder
        self.file_names = [
            f for f in os.listdir(folder) if os.path.isfile(Path(folder, f))
        ]
        self._data = {}
        for file_name in self.file_names:
            self._data[file_name] = pd.read_csv(
                Path(self.folder, file_name), sep=',', header=None)

    def get(self, file_name):
        return self._data[file_name]

    def items(self):
        return self._data.keys()
