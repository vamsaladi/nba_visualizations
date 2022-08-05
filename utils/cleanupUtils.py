import os
import sys
import csv
import pandas as pd

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

def collapseData(fileName):
    """Dataset from Basketball Reference contains multiple rows for players
    traded midway through a season. This function will collapse the table so
    that each player has only row associated with them for stats tables. The
    function will **EDIT** the original file to remove duplicate rows, while
    also returning the new rows for the table

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
        convenience. Additionally, each player is guaranteed to have only row

    None
        The function will also **EDIT** the original file such that multiple rows
        are erased. This will be not be a return of the function but will happen
        behind the scenes.

        Additionally, the function will return 0 if there is an error at any point

    """
    rows = fillInBlanks(fileName)
    if rows == 0:
        return 0
    newRows = [rows[0]]
    for i in range(1, len(rows)):
        if rows[i][0] == rows[i-1][0]:
            continue
        else:
            newRows.append(rows[i])
    newFileName = fileName[:-4] + '_clean.csv'
    with open(newFileName, 'w') as newFile:
        csvwriter = csv.writer(newFile, delimiter=",")
        for row in newRows:
            csvwriter.writerow(row)
    return newRows
