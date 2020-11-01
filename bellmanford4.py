def bellmanford(S,V,E):
    dist={}
    for i in V:
        dist[i]=float("inf")
    # distance from start to start is 0
    dist[S]=0

    # avoid cycles
    for _ in range(len(V)-1):
        for u,v,w in E:
            if dist[u] != float("inf") and dist[u] + w < dist[v]:
                # relax edge
                dist[v] = dist[u] + w 

    for u,v,w in E:
        if dist[u] != float("inf") and dist[u] + w < dist[v]:
            # relax edge
            print('negative cycle')
    return dist

V=['A','B','C']
E=[
    ('A','B',10),
    ('A','C',5)
]

print(bellmanford('A',V,E))

print(bellmanford('s',['s','a','b','c'],[('s', 'a', 5) , ('a', 'c', 3) , ('s', 'b', 6) , ('c', 'a', -7) , ('b', 'c', -2) ]))
print(bellmanford('s',['s','a','b','c'],[('s', 'a', 5) , ('a', 'c', 3) , ('s', 'b', 6) , ('c', 'a', 7) , ('b', 'c', -2) ]))





