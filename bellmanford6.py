def bellmanford(S,V,E):
	dist={}
	for v in V:
		dist[v]=float("inf")
	dist[S]=0


	for _ in range(len(V)-1):
		for u,v,w in E:
			if dist[u] != float("inf") and dist[u]+w < dist[v]:
				dist[v] = dist[u]+w
	
	# negative cycle check
	if dist[u] != float("inf") and dist[u]+w < dist[v]:
		print('negative cycle')
		return ""
	return dist

# test
print(bellmanford('S',['S','A','B','C'], [('S','A',1),('A','B',10),('B','C',-11)]))
