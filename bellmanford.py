def bellmanford(nv, es, s):
    d = [float('inf') for _ in range(nv)]
    d[s] = 0
    p = [None for _ in range(nv)]
    for _ in range(nv - 1):
        for u, v, w in es:
            if d[u] + w < d[v]:
                d[v] = d[u] + w
                p[v] = u
    return (p, d)