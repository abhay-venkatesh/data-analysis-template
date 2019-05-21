import runpy
from pathlib import Path
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("analysis_file", help="path to analysis file")
    args = parser.parse_args()
    file_globals = runpy.run_path(Path(args.analysis_file))
    print(file_globals)
