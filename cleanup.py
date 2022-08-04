import os
import numpy as np
import sys
from cleanupUtils import *

######### CLEANUP TESTING #########

fileName = 'season_stats_data/12_13_data.csv'
rows = collapseData(fileName)
print(rows[3:6])
