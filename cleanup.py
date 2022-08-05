import os
import numpy as np
import sys
from cleanupUtils import *

folders = ['season_stats_data/', 'advanced_stats_data/']

####### REMOVE OLD CLEAN FILES ######
for folder in folders:
    stats_files = os.listdir(folder)
    for file in stats_files:
        if 'clean' in file:
            os.remove(folder + file)

####### STATS CLEANUP #########

for folder in folders:
    stats_files = os.listdir(folder)
    for file in stats_files:
        newRows = collapseData(folder + file)
        if newRows == 0:
            print(f'Error cleaning up {folder + file}')
