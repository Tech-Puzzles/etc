def bellmanford(S,V,E):
    dist={}
    for v in V:
        dist[v]=float("inf")

    dist[S]=0
    for _ in range(len(V)):
        for u,v,w in E:
            if dist[u] != float("inf") and dist[u]+w < dist[v]:
                dist[v]=dist[u]+w
    for u,v,w in E:
        if dist[u] != float("inf") and dist[u]+w < dist[v]:
            print('negative cycle')
            return
    return dist

# test
print(bellmanford('S',['S','A','B','C'],[('S','A',1),('S','B',2),('A','C',-2)]))

def runTest(input,expect):
	S,V,E=input
	ret = bellmanford(S,V,E)
	print('pass' if ret == expect else 'fail')
    
runTest(('S',['S','A','B','C'],[('S','A',1),('S','B',2),('A','C',-2)]),{'S': 0, 'A': 1, 'B': 2, 'C': -1})
