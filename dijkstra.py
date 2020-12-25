#dijkstra algorithm for single source shortest path

import pygame as pg


screen_height = 800
screen_width = 800



class Graph:
	def __init__(self, vertices, edges):
		self.adj_matrix = []
		self.vertices = []
		self.edges = []
		self.vertices_num = vertices
		self.edge_num = edges

		for i in range(self.vertices_num):
			self.add_vertex()

		

	def add_edge(self, vertex1, vertex2):
		self.edges.append([vertex1, vertex2])

		self.adj_matrix[vertex1][vertex2] = 1
		self.adj_matrix[vertex2][vertex1] = 1


	def add_vertex(self):
		if self.vertices == []:
			self.vertices.append(0)
		else:
			self.vertices.append(len(self.vertices))

		for each in self.adj_matrix:
			each.append(0)

		new_list = []
		for i in range(len(self.vertices)):
			new_list.append(0)
		self.adj_matrix.append(new_list)



	def print_graph(self):
		for each in self.adj_matrix:
			print(f'{each}\n')





class Grid:
	def __init__(self, order):
		if order%2 != 0:
			self.order = order+1
		else:
			self.order = order
		self.cell_width = screen_width/(self.order/2)
		self.cell_height = screen_height/(self.order/2)


	def draw(self, window):
		for i in range(self.order):
			pg.draw.line(window, (255, 0, 0), (0, (i+1)*self.cell_height), (screen_width, (i+1)*self.cell_height), 1)
			pg.draw.line(window, (255, 0, 0), ((i+1)*self.cell_width, 0), ((i+1)*self.cell_width, screen_height), 1)



	


def main():

	#getting the input
	vertices = int(input('enter the no of vertices: '))
	edges = int(input('enter the no of edges: '))

	graph = Graph(vertices, edges)

	for i in range(edges):
		a, b = input('enter values').split(sep=' ')
		a = int(a)
		b = int(b)

		assert(a<vertices and b<vertices)

		graph.add_edge(a, b)

	graph.print_graph()





	confirmation = input('Open pygame window?')

	#pygame window

	if confirmation == 'y' or confirmation == 'Y':

		WINDOW  = pg.display.set_mode((screen_width, screen_height))	

		grid = Grid(vertices)

		run = True
		while run:
			for event in pg.event.get():
				if event.type == pg.QUIT:
					run = false 
					pygame.quit()

			grid.draw(WINDOW)

			pg.display.update()
	else:
		quit()


if __name__ == "__main__":
	main()