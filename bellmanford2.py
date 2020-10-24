def bellmanford(V,E,start):
    dist={}
    for i in range(len(V)):
        dist[V[i]]=float("inf")
    dist[start]=0

    for _ in range(len(V)-1):
            for i in range(len(E)):
                print(E[i])
                if dist[E[i][0]] != float("inf") and dist[E[i][0]] + E[i][2]  < dist[E[i][1]]:
                    dist[E[i][1]]=dist[E[i][0]]+ E[i][2]

    for i in range(len(E)):
            if dist[E[i][0]] != float("inf") and dist[E[i][0]] + E[i][2]  < dist[E[i][1]]:
                dist[E[i][1]]=dist[E[i][0]]+ E[i][2]
                print('negative cycle')
                return dist
    print('single source shortest path distance',dist)
    return dist

    
# print(bellmanford(['s','a','b','c'],[('s', 'a', 5) , ('a', 'c', 3) , ('s', 'b', 6) , ('c', 'a', -7) , ('b', 'c', -2) ],'s'))
print(bellmanford(['s','a','b','c'],[('s', 'a', 5) , ('a', 'c', 3) , ('s', 'b', 6) , ('c', 'a', 7) , ('b', 'c', -2) ],'s'))
