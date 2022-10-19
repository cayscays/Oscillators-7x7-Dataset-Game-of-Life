#
# Author:       cayscays
# Date:         December 2021
# Version:      1
# Description: API for using the database of the 7x7 oscillators in Conway's Game of Life with max period of 15 generations.
#               The grid border is infinity not circular.
#
import copy
import random

from raw.oscillators_dataset import *

random.seed(10)


# Initiate a 1d array with len of GRID_SIZE*GRID_SIZE of a given 2d pattern.
# pattern - int representing the pattern
# 1 = alive
# 0 = dead
# grid - in a flattend form (1 dimention instead of 2)
#
# int --> int[]
def pattern_id_to_array(pattern):
    grid = []
    for i in range(GRID_SIZE * GRID_SIZE):
        grid.append(pattern % 2)
        pattern = int(pattern / 2)
    return grid


# Returns a database
# 0 non oscillators
# 1 oscillators
# [[flattened pattern] , [label]]
# 1d array, int --> 2d array
def prepare_data(oscillators, start, end):
    data = []
    for i in range(start, end):
        entry = []
        entry.append(pattern_id_to_array(i))
        if i in oscillators:
            entry.append([1])
        else:
            entry.append([0])
        data.append(entry)
    return data


# create data not oscilator:
# void --> void
def create_data_not_osci():
    counter = 0
    while counter < 1000:
        val = random.randrange(max_checked_value)
        while val in oscillators:
            val = random.randrange(max_checked_value)
        counter += 1
        entry = []
        entry.append(pattern_id_to_array(val))
        entry.append([0])
        print(entry)


# flipps the patterns
# list --> void
def flip_database(data):
    flipped_data = copy.deepcopy(data)
    for entry in flipped_data:
        entry[0].reverse()
        print(entry)


# save to file named filename of the current oscillators' raw data as a visual representation of 0s and 1s.
# string --> void
def dataset_to_file(filename):
    f = open(filename, "w")
    f.write("Source: https://github.com/cayscays/oscillators-7x7-dataset-game-of-life\nAuthor: cayscays\n"
            "ONGOING: Max checked value is 132000000, updated at 9.21.22\n\n"
            "A database of 7x7 oscillators in Conway's Game of Life.\n"
            "Max period of 15 generations, grid border goes to infinity.\n"
            "\n")
    for oscilator in oscillators:
        for i in range(0, GRID_SIZE * GRID_SIZE, GRID_SIZE):
            f.write(''.join(map(str, pattern_id_to_array(oscilator)[i:GRID_SIZE + i])))
            f.write('\n')
        f.write("-------\n")
    f.close()