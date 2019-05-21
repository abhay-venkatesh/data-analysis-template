from lib.folder_db import FolderDB
from pathlib import Path

if __name__ == "__main__":
    fdb = FolderDB(
        Path(("D:/code/src/data-analysis-template/projects/" +
              "coco_stuff_small_confidences/data/f1")))
    print(fdb.items())

    raise NotImplementedError