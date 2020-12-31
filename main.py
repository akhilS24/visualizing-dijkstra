#dijkstra algorithm for single source shortest path

import pygame as pg
import func

pg.init()


screen_height = 600
screen_width = 600




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
	def __init__(self, graph):
	
		self.graph = graph
		self.order = func.find_min_order(self.graph.vertices_num)
		self.cell_width = round(screen_width/(self.order))
		self.cell_height = round(screen_height/(self.order))
		self.nodes = []
		self.node_count = self.graph.vertices_num
		self.edges = []
		self.edge_count = self.graph.edge_num
		self.grid_coordinates = func.create_grid_coordinates(self.order)


		
		for i in range(self.node_count):
			coordinate = func.get_cordinate(self.grid_coordinates)
			self.nodes.append(Node(round(self.cell_width/4), (round(((2*coordinate[1]+1)/2)*self.cell_width), round(((2*coordinate[0]+1)/2)*self.cell_height)), (0, 255, 0), i))

		for i in range(self.edge_count):
			edge = graph.edges[i]
			self.edges.append(Edge(self.nodes[edge[0]].position, self.nodes[edge[1]].position, [(255, 255, 255), (255, 0, 0)], round(self.cell_width*(3/16))))


	def draw(self, window):
		for i in range(self.order):
			pg.draw.line(window, (255, 0, 0), (0, (i+1)*self.cell_height), (screen_width, (i+1)*self.cell_height), 1)
			pg.draw.line(window, (255, 0, 0), ((i+1)*self.cell_width, 0), ((i+1)*self.cell_width, screen_height), 1)

		for node in self.nodes:
			node.draw(window)

		for edge in self.edges:
			edge.draw(window)






class Node:
	def __init__(self, radius, position, color, index):
		self.radius = radius
		self.position = position
		self.color = color
		self.index = index
		self.fontColor = (0, 0, 255)
		self.Font1 = pg.font.SysFont('impact', self.radius)

	def draw(self, window):
		pg.draw.circle(window, self.color, self.position, self.radius)
		txt1 = self.Font1.render(f'{self.index}', True, self.fontColor)
		window.blit(txt1, (self.position[0]-txt1.get_width()/2, self.position[1]-txt1.get_height()/2))





class Edge:
	def __init__(self, start, stop, color, radius):
		self.radius = radius
		self.start_coordinate = start
		self.stop_coordinate = stop
		self.color = color
	def draw(self, window):
		pg.draw.circle(window, self.color[1], self.start_coordinate, self.radius, 3)
		pg.draw.line(window, self.color[0], self.start_coordinate, self.stop_coordinate, 1)
		pg.draw.circle(window, self.color[1], self.stop_coordinate, self.radius, 3)

	


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

		grid = Grid(graph)

		run = True
		while run:

			WINDOW.fill((0,0,0))

			for event in pg.event.get():
				if event.type == pg.QUIT:
					run = false 
					pg.quit()

			grid.draw(WINDOW)

			pg.display.update()

	else:
		quit()


if __name__ == "__main__":
	main()