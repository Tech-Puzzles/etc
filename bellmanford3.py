# (u,v,w)
# for all len(nodes)
# relax all edges
# maintain dist array per node
# initialize to infinity except source node

def bellmanford(S,V,E):
	dist={}
	for v in V:
		dist[v]=float("inf")
	dist[S]=0

	for _ in range(len(V)-1):
		for u,v,w in E:
			if dist[u] != float("inf") and dist[u] + w < dist[v]:
				# relax
				dist[v] = dist[u] + w
	return dist



V=['A','B','C']
E=[
	('A','B',10),
	('A','C',5)
]

print(bellmanford('A',V,E))





