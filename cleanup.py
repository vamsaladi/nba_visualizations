import os
import sys
import csv

########## LOAD FILE ##########

def loadFileRows(fileName):
    """Load a file as an array, where each element is a row

    Parameters
    ----------
    fileName : String
        Path to file being loaded

    Returns
    -------
    Array
        Each element in the array is a row in the original data file

    Int
        Returns 0 if file does not exist
    """
    if not os.path.exists(fileName):
        return 0
    rows = []
    with open(fileName) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_num = 0
        for row in csv_reader:
            if line_num == 0:
                print(f'Column Names: {", ".join(row)}')
                line_num += 1
            else:
                rows.append(row)
                line_num += 1
        print(f"Read {line_num} lines!")
    return rows

def fillInBlanks(fileName):
    """Fill in the blank entries in the file with 0.0 so there are no
    discrepancies in the dataset later and you don't have to deal with
    empty or NA values

    Parameters
    ----------
    fileName : String
        Path to file being loaded

    Returns
    -------
    Array
        Each element in the array is a row in the original data file, where
        each row is guaranteed to have entries for every column and each entry
        is transformed from a string value to a float for future mathematical
        convenience
    Int
        Returns 0 if file does not exist
    """
    rows = loadFileRows(fileName)
    entriesFilled = 0
    if rows == 0:
        return 0
    for row in rows:
        for i in range(len(row)):
            if row[i] == "" or row[i] == " ":
                row[i] = 0.0
                entriesFilled += 1
            elif i > 2 and i != 4 and i != len(row) - 1:
                row[i] = float(row[i])
            else:
                continue
    print(f"Total entries filled: {entriesFilled}")
    return rows
