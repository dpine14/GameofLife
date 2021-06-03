#!/usr/bin/env python3


import sys, time
from random import randint

#globals
WIDTH = 0
HEIGHT = 0



def cell_next_state(cell_coords, board_state):
	num_alive = 0
	x = cell_coords[0]
	y = cell_coords[1]

	for i in range((x-1), (x+1)+1):
		if i < 0 or i >= len(board_state[0]): continue

		for j in range((y-1), (y+1)+1):
			if j < 0 or j >= len(board_state): continue
			if i == x and j == y: continue

			if board_state[i][j] == 1:
				num_alive += 1

	if board_state[x][y] == 1:
		if num_alive <= 1:
			return 0
		elif num_alive <= 3:
			return 1
		else:
		    return 0
	else:
	    if num_alive == 3:
	        return 1
	    else:
	        return 0
	


def update_board(board_state):
	board_copy = dead_state([WIDTH,HEIGHT])

	for i in range(0, WIDTH):
		for j in range(0, HEIGHT):
			board_copy[i][j] = cell_next_state((i,j), board_state)

	return board_copy



#initializes cells randomly
def rand_state(grid_size):
	w = grid_size[0]
	h = grid_size[1]
	board_state = dead_state([w, h])
	
	for i in range(h):
		for j in range(w):
			board_state[i][j] = randint(0,1)

    #print(boardState)
	return board_state



#initializes cells to 0(dead)
def dead_state(grid_size):	
	board_state = []
	w = grid_size[0]
	h = grid_size[1]


	for i in range(h):
		board_state.append([0]*w)

	return board_state

def render(board_state):
	'This function displays the grid in visually understandable manner'
	for i in range(HEIGHT):
		print("|", end = "")
		for j in range(WIDTH):
			if(board_state[i][j] == 1):
				print("O", end = "")
			else:
				print(" ", end = "")
		print("|")



def run(init_state):
	global HEIGHT, WIDTH
	
	HEIGHT = len(init_state)
	WIDTH = len(init_state[0])

	next_state = init_state

	while True:
		render(next_state)
		next_state =update_board(next_state)
		time.sleep(0.1)


		
if __name__ == "__main__":
	init_state = [[0,0,0,0,0,0],
				  [0,0,0,0,0,0],
				  [0,0,1,1,1,0],
				  [0,1,1,1,0,0],
				  [0,0,0,0,0,0],
				  [0,0,0,0,0,0]]

	run(init_state)