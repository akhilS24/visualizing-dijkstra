import random


#to find the min order (order*order) of the matrix required so as to plot the nodes of the graph
def find_min_order(no):
	i = 1
	while i**2 < no:
		i = i+1
	return i

#to randomly generate the coordinates required for each node inside the grid
def get_cordinate(grid):
	rn = random.choice(grid)
	grid.remove(rn)
	return rn

#creating the grid coordinates list
def create_grid_coordinates(order):
	grid_coordinates = []
	for i in range(order):
		for j in range(order):
			grid_coordinates.append((i,j))

	return grid_coordinates