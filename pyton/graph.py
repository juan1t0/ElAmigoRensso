import matplotlib.pyplot as plt
import networkx as nx
from networkx import Graph
import collections


############################################################################################
############################################################################################

def betweenness_centrality(G, k=None, normalized=True, weight=None, 
						endpoints=False, seed=None): 
	betweenness = dict.fromkeys(G, 0.0) # b[v]=0 for v in G 
	if k is None: 
		nodes = G 
	else: 
		random.seed(seed) 
		nodes = random.sample(G.nodes(), k) 
	for s in nodes: 

		# single source shortest paths 
		if weight is None: # use BFS 
			S, P, sigma = _single_source_shortest_path_basic(G, s) 
		else: # use Dijkstra's algorithm 
			S, P, sigma = _single_source_dijkstra_path_basic(G, s, weight) 

		# accumulation 
		if endpoints: 
			betweenness = _accumulate_endpoints(betweenness, S, P, sigma, s) 
		else: 
			betweenness = _accumulate_basic(betweenness, S, P, sigma, s) 

	# rescaling 
	betweenness = _rescale(betweenness, len(G), normalized=normalized, 
						directed=G.is_directed(), k=k) 
	return betweenness

############################################################################################
############################################################################################

def Special_BFS(G,u,v,cant_nodos): #u es el presunto central, v es el nodo de inicio
        
        tam_path = [-1 for i in range(cant_nodos)]
        tam_path[v] = 0

        cant_path = [0 for i in range(cant_nodos)]
        path_with_u = [0 for i in range(cant_nodos)]
        path_with_u[u] = 1

        queue_Neighbors = collections.deque([v])
        
        while queue_Neighbors:
                n = queue_Neighbors.popleft()

                for ne in nx.neighbors(G,n):                        
                        if (tam_path[ne] == -1):
                                queue_Neighbors.append(ne)

                        if(path_with_u[n] > 0):
                                path_with_u[ne] = path_with_u[n]
                        
                        #if(ne == u ):
                         #       path_with_u[ne] = 1#path_with_u[ne] + 1
                        if(tam_path[ne] == -1):
                                tam_path[ne] = tam_path[n] + 1
                                cant_path[ne] = cant_path[ne] + 1
                        elif( tam_path[ne] == tam_path[n] + 1):
                                cant_path[ne] = cant_path[ne] + 1

        temp = 0
        for x in range(cant_nodos):
                try:
                        temp = temp + (path_with_u[x] / cant_path[x])
                except :
                        temp = temp

        return temp

def calc_Betweenness_I(G,cant_nodos,u): #u es presunto central
        temp = 0
        for v in range(cant_nodos):
                if (v == u) :
                        continue
                temp = temp + ( Special_BFS(G,u,v,cant_nodos))
        return temp

def my_Betweenness(G):
        CB = dict.fromkeys(G,0.0)
        cant_nodos = nx.number_of_nodes(G)
        for i in range(cant_nodos):
                CB[i] = calc_Betweenness_I(G,cant_nodos,i)
        return CB

############################################################################################
############################################################################################


if __name__ == '__main__':
#    G = nx.gnp_random_graph(125, 0.5, seed=8)
    G = nx.erdos_renyi_graph(6,0.5)
#    G = nx.house_graph()
    pos = nx.spring_layout(G)
    b = my_Betweenness(G)
    b2 = nx.betweenness_centrality(G)
    
    cen = -1
    inde = -1
    for i in b:
        if(cen < b[i]):
            inde = i
            cen = b[i]
    
    print("my Betweenness ",cen," ",inde)
    nx.draw_networkx_nodes(G, pos)
    nx.draw_networkx_nodes(G, pos, nodelist=[inde], node_color='b')
    
    nx.draw_networkx_edges(G, pos)
    

    
    cen = -1
    ind = -1
    for i in b2:
        if(cen < b2[i]):
            ind = i
            cen = b2[i]
    
    print("NX Betweenness ",cen," ",ind)
    nx.draw_networkx_nodes(G, pos, nodelist=[ind], node_color='g')
    plt.show()
