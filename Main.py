#Game of life function and helpers
#Dylan Pine 
import numpy as np

x=100
y=100

pos_x=8
pos_y=67
universe = False

def generate_universe(x,y):
    universe = np.zeros((x,y), dtype='bool')

def is_ded(universe, pos_x, pos_y):
    return ~universe[pos_x, pos_y]

def get_ded(universe, pos_x, pos_y):
    universe[pos_x, pos_y] = ~(universe[pos_x, pos_y])

def game_of_life(x,y, universe):
    
