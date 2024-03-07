from heapq import heappush, heappop

def dijkstra(g, s):
    pq = []
    d = [float('inf') for _ in g]
    p = [None for _ in g]
    d[s] = 0
    heappush(pq, (0, s))

    while pq:
        w, v = heappop(pq)
        if w > d[v]:
            continue
        for n, w in g[v]:
            dist = d[v] + w
            if dist < d[n]:
                d[n] = dist
                p[n] = v
                heappush(pq, (dist, n))

    return (p, d)

