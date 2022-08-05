import os
import numpy as np
import sys
from utils.salaryUtils import *

folder = 'salaries_data/'
files = ['1999_2019.csv', '2020_2021.csv', '2021_2022.csv']

###### REMOVE OLD CLEAN FILES ######
stats_files = os.listdir(folder)
for file in stats_files:
    if 'clean' in file:
        os.remove(folder + file)

####### STATS CLEANUP #########
for i in range(len(files)):
    newRows = rewriteSalaryFile(folder + files[i], i+1)
    if newRows == 0:
        print(f'Error cleaning up {folder + files[i]}')
    else:
        print(f'Cleaned up {folder + files[i]}!')
