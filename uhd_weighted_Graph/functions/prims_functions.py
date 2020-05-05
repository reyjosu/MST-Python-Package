def cost(G,e):
    
    #This function takes the given graph data 
    #and returns the the weight of each edge
    #to be used in the min_prims_edge
    
    return G.edges()[e]['weight']
#============================================================================#    

def valid_incident_edges(G,T):
           
           #A function that creates a list which 
           #finds all edges in the graph to later get
           #filtered and remove all possible edges which will 
           #create cycles. All remaining edges are stored in a
           #list, and in turn that list is sent outside of the
           #valid_incident_edges
    
    incidentedges=[]
    for e in G.edges():
        for v in T.nodes():
            if v in e:
                incidentedges.append(e)
            
    validedges=[]                      
    for e in incidentedges:
        if e[0] not in T.nodes() \
        or e[1] not in T.nodes():
            validedges.append(e)            
            
    return validedges
#============================================================================#

def min_prims_edge(G,T):
    
    #Using the valid_edges values from valid_incident_edges function,
    #we create a list which holds all the possible_edges to create a tree.
    #Once that's found we find the lowest weight/cost of each possible edge
    #and send that list outside of the function to be used for T in 
    #uhd_weighted_graphs.py
    
    
    possible_edges=valid_incident_edges(G,T)
    min_edge=possible_edges[0]
    for e in possible_edges:
        if (cost(G,e)<cost(G,min_edge)):
            min_edge=e
            
    return min_edge
#============================================================================#