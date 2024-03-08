# Algorithm Flashcards

This repository is a collection of algorithms and data structures implemented in Python 3.
Each algorithm implementation is short enough to fit into an A6 index card (105mm×148mm).

## Implemented algorithms

- [x] [Dijkjstra’s shortest path](dijkstra.py)
- [x] [Bellman-Ford shortest path](bellmanford.py)
- [x] [Floyd-Warshall all-pairs shortest path](floydwarshall.py)

## Naming conventions

For the sake of brevity, the variable names are terse, and there is no typing information in the function signatures.
Variable types:
- `u` and `v` are vertices of `type Vertex = int`.
   Edges always go from `u` to `v`.
- `s` is a source vertex of type `int`.
- `e` is an edge of type `tuple[Vertex, Vertex, Weight]`.
- `es` is an array of edges.
- `nv` is the number of vertices in the graph (`int`).
  All algorithms assume that the vertices are numbered from `0` to `nv-1`.
- `w` is a weight of some numeric type (`int` or `float`).
- `g` is an adjacency list representation of a graph, of type `list[list[tuple[Vertex, Weight]]]`.
- `d` is a distance array or matrix (depending on the algorithm), of type `list[Weight]` or `list[list[Weight]]`.
- `p` is a predecessor array or matrix (depending on the algorithm), of type `list[Vertex]` or `list[list[Vertex]]`.