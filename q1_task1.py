import os, pathlib, sys
import pandas as pd

PATH = os.path.dirname(__file__)
COLUMNS = ["SHORT-TEXT", "TEXT"]
ASSIGNMENT_FOLDER = "Assignment 2"
TEXTFILE = "ALLTEXT.txt"


def getCSVFiles(path=os.path.join(PATH, ASSIGNMENT_FOLDER), suffix=".csv"):
    return [os.path.join(path, x) for x in os.listdir(path) if x.endswith(suffix)]


def exportText(files, target=os.path.join(PATH, TEXTFILE)):
    # clear file
    open(target, "w").close()

    for file in files:
        csv = pd.read_csv(file, usecols=lambda c: c in set(COLUMNS))
        csv.to_csv(os.path.join(PATH, TEXTFILE), header=False, mode="a", index=False)


def main():
    files = getCSVFiles()
    if not files:
        sys.exit(
            "No CSV files found. please put this .py file in the parent folder of Assignment 2"
        )

    exportText(files)


main()
