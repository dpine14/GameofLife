#Game of life function and helpers
#Dylan Pine 
import numpy as np
import io
import pprint

x=100
y=100
print('hello world')
pos_x = 8
pos_y = 67

class universe:
    def __init__(self,  x, y, alive):
        print('hello u')
        self.x = x
        self.y = y
        self = np.zeros((x,y), dtype='bool')
        self.alive = []
    
    def find_alive(self):
        #check everywhere in the universe for life and record it in self.alive[] <-- eventually to hold places indicated by user
        print('Hello')
        for i in self.x:
            for j in self.y:
                if self[i, j] == True:
                    self.alive.append(self[i, j])
    
u = universe(x, y, False)

#def generate_universe(x,y):
 #  return np.zeros((x,y), dtype='bool')

def is_ded(u, pos_x, pos_y):
    return ~u[pos_x, pos_y]

def die(u, pos_x, pos_y):
    u[pos_x, pos_y] = ~(u[pos_x, pos_y])

def game_of_life(u):
    ##################################################################################################
    #    Any live cell with two or three live neighbours survives.
    #    Any dead cell with three live neighbours becomes a live cell.
    #    All other live cells die in the next generation. Similarly, all other dead cells stay dead.
    ##################################################################################################
    print(str(u.find_alive()))
    print('Hello gol')

game_of_life(u)
 