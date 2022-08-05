import os
import csv


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
                line_num += 1
            else:
                rows.append(row)
                line_num += 1
        print(f"Read {line_num} lines!")
    return rows


def rewriteSalaryFile(fileName, flag):
    """Format 2020 to 2021 csv file appropriately, deleting unneccessary 
    columns and formatting the salary and other quoted numbers 
    appropriately. Function will rewrite the file and save it as a clean 
    version in the same folder.

    Flag:
        - Flag 1: 1999 to 2019 file
        - Flag 2: 2020 to 2021 file
        - Flag 3: 2021 to 2022 file

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

    if flag == 1:  # 1999 to 2019 file
        for i in range(len(rows)):
            if int(rows[i][-1]) < 2013:
                continue
            else:
                rows[i][-2] = float(rows[i][-2])
                newRows.append(rows[i])
        newFileName = fileName[:-4] + '_clean.csv'
        with open(newFileName, 'w') as newFile:
            csvwriter = csv.writer(newFile, delimiter=",")
            for row in newRows:
                csvwriter.writerow(row)
        return newRows

    if flag == 2:  # 2020 to 2021 file
        for i in range(len(rows)):
            salary = rows[i][3].strip()
            if salary[0] == "$":
                salary = salary[1:]
            salary = float("".join(salary.split(",")))
            newRows.append([i + 1, rows[i][0], rows[i][2], salary])
        newFileName = fileName[:-4] + '_clean.csv'
        with open(newFileName, 'w') as newFile:
            csvwriter = csv.writer(newFile, delimiter=",")
            for row in newRows:
                csvwriter.writerow(row)
        return newRows

    if flag == 3:  # 2021 to 2022 file
        for i in range(len(rows)):
            salary = rows[i][3].strip()
            if salary == "" or salary == " ":
                salary = "0"
            if salary[0] == "$":
                salary = float(salary[1:])
            newRows.append([rows[i][0], rows[i][1], rows[i][2], salary])
        newFileName = fileName[:-4] + '_clean.csv'
        with open(newFileName, 'w') as newFile:
            csvwriter = csv.writer(newFile, delimiter=",")
            for row in newRows:
                csvwriter.writerow(row)
        return newRows
