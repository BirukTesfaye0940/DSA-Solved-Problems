def build_graph(edges):
    graph = {}
    
    for u, v in edges:
        graph.setdefault(u, []).append(v)
        graph.setdefault(v, []).append(u)
    
    return graph


edges = [(0,1), (0,2), (1,3), (3,4)]
graph = build_graph(edges)

print(graph)