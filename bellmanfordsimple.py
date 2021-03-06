import sys

class Graph:
	
	def __init__(self,V):
		self.V = V
		self.graph=[]
	def addEdge(self,u,v,w):
		self.graph.append([u,v,w])
	def print(self):
		print("\ngraph: (u,v,weight)")
		for item in self.graph:
			print(item)
	def bellmanford(self,src):
		self.print()
		iterations=0
		dist = [float("Inf")] * self.V 
		dist[src] = 0
		# dist[src] = 1
		for i in range(self.V-1):
			for (u,v,w) in self.graph:
				#print(i,u,v,w)
				iterations+=1
				if dist[u] != float("Inf") and dist[u]+w < dist[v]:
					dist[v] = dist[u] + w
				print('dist',dist)
		for (u,v,w) in self.graph:
			#print(i,u,v,w)
			if dist[u] != float("Inf") and dist[u]+w < dist[v]:
				print("Graph contains negative weight cycle") 
				dist[v] = dist[u] + w
				print('dist',dist)
				return
		print('dist',dist)
		print('iterations',iterations)

		
g = Graph(5) 
# print(g)

g.addEdge(0, 1, -1) 
g.addEdge(0, 2, 4) 
g.addEdge(1, 2, 3) 
g.addEdge(1, 3, 2) 
g.addEdge(1, 4, 2) 
g.addEdge(3, 2, 5) 
g.addEdge(3, 1, 1) 
g.addEdge(4, 3, -3) 
# g.print()
# sys.exit(1)

# Print the solution 
g.bellmanford(0) 

g = Graph(5) 
# print(g)

g.addEdge(0, 1, -1) 
g.addEdge(0, 2, 4) 
g.addEdge(1, 2, 1) 
g.addEdge(1, 3, 2) 
g.addEdge(1, 4, 2) 

g.addEdge(2, 0, 0) 

g.addEdge(3, 2, 5) 
g.addEdge(3, 1, 1) 
g.addEdge(4, 3, -3) 
# g.print()
# sys.exit(1)

# Print the solution 
g.bellmanford(0) 

g = Graph(5) 
# print(g)

g.addEdge(0, 1, -1) 
g.addEdge(0, 2, 4) 
g.addEdge(1, 2, 1) 
g.addEdge(1, 3, 2) 
g.addEdge(1, 4, 2) 

g.addEdge(2, 0, -1) 

g.addEdge(3, 2, 5) 
g.addEdge(3, 1, 1) 
g.addEdge(4, 3, -3) 
# g.print()
# sys.exit(1)

# Print the solution 
g.bellmanford(0) 

g = Graph(4) 
# print(g)

g.addEdge(0, 1, 5) 
g.addEdge(1, 3, 3) 
g.addEdge(0, 2, 6) 
g.addEdge(3, 1, -7) 
g.addEdge(2, 3, -2) 

# g.print()
# sys.exit(1)

# Print the solution 
g.bellmanford(0) 
