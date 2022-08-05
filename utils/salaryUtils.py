import os
import sys
import csv
import pandas as pd

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

def formatSalaryFile(fileName):
    """Format 2020 to 2021 csv file appropriately, deleting unneccessary columns
    and formatting the salary and other quoted numbers appropriately. Function will
    rewrite the file and save it as a clean version in the same folder.

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
    newRows = []
    if rows == 0:
        return 0
    for i in range(len(rows)):
        salary = rows[i][3].strip()
        if salary[0] == "$":
            salary = salary[1:]
        newRows.append([i+1, rows[i][0], rows[i][2], salary])
    return newRows
