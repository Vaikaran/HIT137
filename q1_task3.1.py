import csv, os
from collections import Counter

PATH = os.path.dirname(__file__)
TEXTFILE = "ALLTEXT.txt"
CSV = "top30.csv"
COUNT = 30
TXT_PATH = os.path.join(PATH, TEXTFILE)
CSV_PATH = os.path.join(PATH, CSV)


def main():
    counter = Counter()
    with open(TXT_PATH, "r") as text:
        for line in text:
            split_words = line.split()
            counter.update(Counter(split_words))

    resultDict = dict(counter.most_common(COUNT))
    with open(CSV_PATH, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["word", "count"])
        for key, value in resultDict.items():
            writer.writerow([key, value])


main()
