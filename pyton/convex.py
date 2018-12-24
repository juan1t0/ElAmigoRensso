import matplotlib.pyplot as plt
import networkx as nx
from networkx import Graph

def special(p,q,r):
    return (q[1]-p[1])*(r[0]-q[0]) - (q[0]-p[0])*(r[1]-q[1])
    
############################################################################################
# CONVEX HULL : JARVIS'S ALGORITHM #########################################################
############################################################################################

def cloke(p,q,r):
    V = special(p,q,r)
    if(V == 0):
        return 0
    elif(V > 0):
        return 1
    else:
        return 2

def convexHull_Jarvis(pos):
    left = 0
    n = len(pos)
    for i in range (1,n-1):
        if (pos[i][0] < pos[left][0]):
            left = i
    p=left
    HULL = []
    while( True ):
        q = (p + 1)% n
        for i in range (n-1):
            if (cloke(pos[p],pos[i],pos[q]) == 2):
                q = i;
        HULL.append((p,q))
        p=q
        if(p == left):
            break;

    return HULL

############################################################################################
# CONVEX HULL : QUICKHULL ALGORITHM ########################################################
############################################################################################
HULL2 =[]
def ladito(p1,p2,p3):
    v = special(p1,p2,p3)
    if ( v > 0 ):
        return 1;
    if ( v < 0 ):
        return -1;

def quick(pos , p1 , p2 , lado):
    max_i = -1
    max_d = 0
    n = len(pos)
    for i in range(n-1):
        aux = abs(special(pos[p1],pos[p2],pos[i]))
        if( ladito(pos[p1],pos[p2],pos[i]) == lado and aux > max_d):
            max_i = i
            max_d = aux
    if(max_i == -1):
        HULL2.append((p1,p2))
        return 
    quick(pos,max_i,p1, (-1 * ladito(pos[max_i],pos[p1],pos[p2])));
    quick(pos,max_i,p2, (-1 * ladito(pos[max_i],pos[p2],pos[p1])));
    
def convexHull_Quick(pos):
    left = 0
    righ = 0
    n = len(pos)
    for i in range (1,n-1):
        if(pos[i][0] < pos[left][0]):
            left = i
        if(pos[i][0] > pos[righ][0]):
            righ = i
    quick(pos, left, righ,1)
    quick(pos, left, righ,-1)
    return HULL2
    
############################################################################################
############################################################################################


if __name__ == '__main__':
#    G = nx.gnp_random_graph(55, 0.01, seed=-1)
#    G = nx.gnp_random_graph(55, 0.101, seed=-1)
    G = nx.gnp_random_graph(55, 10.00005, seed=-1)

#    G = nx.erdos_renyi_graph(53,0.101)
#    G = nx.erdos_renyi_graph(53,0.01)
#    G = nx.erdos_renyi_graph(53,10.01)
    
    pos = nx.spring_layout(G)
    nx.draw_networkx_nodes(G, pos,node_size = 125 ,node_color='k')
    edgesz = convexHull_Jarvis(pos)
    edgess = convexHull_Quick(pos)
#    nx.draw_networkx_edges(G, pos)
    nx.draw_networkx_edges(G, pos,edgess,5.0,'b')
    nx.draw_networkx_edges(G, pos,edgesz,2.0,'r')
    plt.show()

