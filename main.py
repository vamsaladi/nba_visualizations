import os
import numpy as np
import sys
from cleanup import *

######### CLEANUP TESTING #########

rows = fillInBlanks('season_stats_data/12_13_data.csv')
print(len(rows))
