# BipartiteToChordalMDV
Minimum Degree Vertex heuristic is applied on a bipartite graph. The aim is to make this bipartite graph chordal with as few edges as possible.
Minimum Degree method chooses a vertex v of minimum degree in Gi−1 at each
step i. Minimum Degree Vertex heuristic is in the lookout of addition of as few
edges as possible during triangulation. The input graph is denoted as G = (V,E), with |V| = n and |E| = m. The transitory graph obtained at the end of each step is denoted by H = (V,E + Q) where Q is list of Fill-edges. We
remove the vertices with degree say D, D < 2 (i.e. number of edges incident on it is less than 2). Then, the remaining vertices with D ≥ 2 are arranged in the ascending order and considered in the same order. In the case where two or more
vertices are of same degree, one of them is chosen ﬁrst arbitrarily. We take a
vertex v from the reduced vertex set and ﬁnd its neighbors, make the
neighbourhood a clique and then remove the vertex from graph H. The degrees
of the remaining vertices in graph H are updated. We will continue till all the
vertices are exhausted and in the end, we will add all the edges added in graph H
to the graph G. Thus, the graph becomes chordal with as few edges as possible.
