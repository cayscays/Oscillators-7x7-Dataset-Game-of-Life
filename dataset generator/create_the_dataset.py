#
# Author:       cayscays
# Date:         December 2021
# Version:      1
# Description:  Create a dataset of Conway's Game of Life oscillators.
#


GRID_SIZE = 7
MAX_GENERATION = 15


# Cell's next value
# 1 = alive
# 0 = dead
#
# int, ints --> int
def cell_next_gen(cell, environment_sum):
    if cell == 1:
        if environment_sum < 2 or environment_sum > 3:
            return 0
        else:
            return 1
    elif cell == 0 and environment_sum == 3:
        return 1
    else:
        return 0


# Initiate a grid with a given pattern.
# pattern - a base 10 int and treated as a binary number representing the pattern
# 1 = alive
# 0 = dead
# grid - in a flattend form (1 dimention instead of 2)
#
# int --> int[]
def init_grid(pattern):
    grid = []
    for i in range(GRID_SIZE * GRID_SIZE):
        grid.append(pattern % 2)
        pattern = int(pattern / 2)
    return grid


# Deep copy of a state
#
# int[] --> int[]
def deep_copy(state):
    grid = []
    for i in range(GRID_SIZE * GRID_SIZE):
        grid.append(state[i])
    return grid


# Comperes 2 states
#
# int[], int[] --> boolean
def equals(state1, state2):
    for i in range(GRID_SIZE * GRID_SIZE):
        if state1[i] != state2[i]:
            return False
    return True


# Returns the sum of the cells of a given cell's enviorment
# Grid's edges go to infinity and neighbors there are 0s
#
# int[] --> int
def get_environment_sum(state, i):
    sum = 0

    # whate neighbors does i have on the grid:
    top = i > GRID_SIZE - 1
    bottom = i < (GRID_SIZE * GRID_SIZE - GRID_SIZE)
    left = (i % GRID_SIZE) != 0
    right = ((i + 1) % GRID_SIZE) != 0

    if top and right:
        sum += state[i - GRID_SIZE + 1]
    if top:
        sum += state[i - GRID_SIZE]
    if top and left:
        sum += state[i - GRID_SIZE - 1]
    if left:
        sum += state[i - 1]
    if left and bottom:
        sum += state[i + GRID_SIZE - 1]
    if bottom:
        sum += state[i + GRID_SIZE]
    if right and bottom:
        sum += state[i + GRID_SIZE + 1]
    if right:
        sum += state[i + 1]
    return sum


# Returns the next configuration of a given state
#
# int[] --> int[]
def get_next_state(state):
    next_state = []
    for i in range(GRID_SIZE * GRID_SIZE):
        next_state.append(cell_next_gen(cell=state[i], environment_sum=get_environment_sum(state, i)))
    return next_state


# Finds out if a given configuration is an Oscillator
# pattern - a base 10 int and treated as a binary number representing the pattern
#
# int --> boolean
def get_is_oscillator(pattern):
    original_state = init_grid(pattern)
    current_state = init_grid(pattern)
    for generation in range(MAX_GENERATION):
        prev_state = deep_copy(current_state)
        current_state = get_next_state(prev_state)
        # If its a still life --> not an oscillator
        if equals(current_state, prev_state):
            return False
        elif equals(current_state, original_state):
            return True
    return False


# int, List, boolean --> void
# Saves a .txt file
# def configuration_to_textfile(index, is_oscillator):
#     # Create a textfile
#     if is_oscillator is True:
#         filename = "oscillator.txt"
#     else:
#         filename = "other.txt"
#     # textfile = open("/content/gdrive/My Drive/oscillators_dataset/" + str(index) + "_" + filename, "w")
#     open("/content/gdrive/My Drive/oscillator_dataset_13_9/" + str(index) + "_" + filename, "a").close()


# Creates the database
# Now's a good time for a break when the database is being built :)
max_pattern = 2 ** (GRID_SIZE * GRID_SIZE) - 1
start = 0
end = max_pattern
print('list of oscillators:')
for i in range(start, end):
    if get_is_oscillator(i):
        print("i=" + str(i))
print('Done')
