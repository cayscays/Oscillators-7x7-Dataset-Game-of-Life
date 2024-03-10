"""
Author:       cayscays
Date:         December 2021
Version:      1
Description:  This file contains utility functions for processing and manipulating data related to Conway's Game of Life oscillators. 
              It includes functions for transforming, and preparing the dataset for further use or analysis.
              This file serves as a tool for managing the dataset of oscillators, providing essential functionalities for data processing tasks.
"""

import copy
import random

from raw.oscillators_dataset import *

SEED = 10

random.seed(SEED)


def pattern_id_to_array(pattern):
    """
    Initiate a 1d array with len of GRID_SIZE*GRID_SIZE of a given 2d pattern.
    
    Args:
    pattern (int): Treated as a binary number representing the pattern. Each bit corresponds to a cell, where 0 indicates a dead cell and 1 indicates a live cell.
    
    Returns:
    list: Initialized grid in flattened form (one dimension instead of two).
    """
    grid = []
    for i in range(GRID_SIZE * GRID_SIZE):
        grid.append(pattern % 2)
        pattern = int(pattern / 2)
    return grid


def prepare_data(oscillators, start, end):
    """
    Returns a database of oscillators and non-oscillators. 

    Args:
    oscillators (list): List of oscillators.
    start (int): Start index.
    end (int): End index.
    
    Returns:
    list: A 2D array containing flattened patterns and corresponding labels (0 for non-oscillators, 1 for oscillators).
          Entry looks like this: [[flattened pattern] , [label]].
    """
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


def create_data_not_osci():
    """
    Creates data for non-oscillators.
    """
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


def flip_database(data):
    """
    Creates data for non-oscillators.
    Args:
    data (list): The database containing patterns to be flipped.
    """
    flipped_data = copy.deepcopy(data)
    for entry in flipped_data:
        entry[0].reverse()
        print(entry)


def dataset_to_file(filename):
    """
    Saves the current oscillators' data to a file as a visual representation of 0s and 1s.
    
    Args:
    filename (str): Name of the file to save the data.
    """
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
