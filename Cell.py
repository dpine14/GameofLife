class cell:
    #constructer
    def __init__(self):
        self.state = False
    
    #kill the cell
    def set_dead(self):
        self.status = False
    # the cell
    def set_alive(self):
        self.status = True

    def get_status(self):
        return self.state