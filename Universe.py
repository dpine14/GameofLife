import Cell as cell

class universe:
    #constructor 
    def __init__(self,  x, y):
        self._x = x
        self._y = y

        self._board = [[cell() for column_cells in range(self._x)]
                                 for row_cells in range(self._y)]
    
    def big_bang(self):
       for i in self._grid:
           for j in i:
               j.set_dead()

    def neighbor_status(self):
        #check wether neighbors are dear or alive
        return 0