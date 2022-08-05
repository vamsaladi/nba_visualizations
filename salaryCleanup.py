import os
import numpy as np
import sys
from utils.salaryUtils import *

folder = 'salaries_data/'

####### REMOVE OLD CLEAN FILES ######
# for folder in folders:
#     stats_files = os.listdir(folder)
#     for file in stats_files:
#         if 'clean' in file:
#             os.remove(folder + file)

####### STATS CLEANUP #########

# salary_files = os.listdir(folder)
# for file in stats_files:
#     newRows = collapseData(folder + file)
#     if newRows == 0:
#         print(f'Error cleaning up {folder + file}')

file = folder + 'salaries_data_20_21.csv'
rows = formatSalaryFile(file)
print(rows[1])
