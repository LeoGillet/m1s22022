#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  1 14:02:34 2022

@author: ruricaru
"""

# also uses pydot module 
import networkx as nx
from networkx.drawing.nx_pydot import write_dot
from graphviz import Source

def deBruijnize(t, k):
    """ Return a set of nodes and a list of edged holding pairs of nodes
        (for each k+1-mer (edge), form a pair from the left k-mer (node) 
        and the right k-mer (node))."""
    edges = []
    nodes = set()
    for i in range(len(t)-3):
        j = i+1
        word = t[i:i+k]
        next_word = t[j:j+k]
        nodes.add(word)
        if len(next_word) == k:
            edges.append((word, next_word))
    print(len(edges))
    return nodes, edges


def deBruijn2Str(t, nodes, edges, k):
    """ Visualize a directed multigraph as a string """
    dot_str = 'digraph "DeBruijn graph" {\n'
    for node in nodes:
        dot_str += '  %s [label="%s"] ;\n' % (node, node)
    for src, dst in edges:
        dot_str += '  %s -> %s ;\n' % (src, dst)
    return dot_str + '}\n'

def deBruijn2Dot(t, nodes, edges, filename):
    """ Visualize a directed multigraph as a dot file """
    G=nx.MultiDiGraph()
    G.add_nodes_from(nodes)
    G.add_edges_from(edges)
    #nx.draw(G, **{'with_labels':True})
    write_dot(G, filename)
    s = Source.from_file(filename)
    s.view()

# An Eulerian path exists if and only if the vertices have outdegree = indegree,
# except from 2 of them : one with outdegree = indegree + 1, 
# and one with indegree = outdegree + 1.
# In the case of an eulerian cycle, all vertices have outdegree = indegree
# We assume that the graph is connected (1 connected component)
def checkEulerian(nodes, edges):
    """ Test whether the graph has an eulerian path or cycle.
        Return True if eulerian, False otherwise """
    G=nx.MultiDiGraph()
    G.add_nodes_from(nodes)
    G.add_edges_from(edges)
    origin = final = path = False
    cycle = True

    for node in G.nodes:
        if G.in_degree(node) != G.out_degree(node):
            cycle = False

    for node in G.nodes:
        ind = G.in_degree(node)
        out = G.out_degree(node)
        if out != ind:
            if out == ind+1:
                if origin: # Path cannot have two origins
                    return False
                origin = True
            if ind == out+1:
                if final: # Path cannot have two final nodes
                    return False
                final = True
    if origin and final:
        path = True
    if cycle or path:
        print("Eulerian Path") if path else ""
        print("Eulerian Cycle") if cycle else ""
        return True
    return False

# algorithm in 6.2 in http://www.gymomath.ch/javmath/polycopie/th_graphe6.pdf 
def buildEulerianCycle(nodes, edges):
    """ Compute and return a list of edges corresponding to an eulerian cycle
        for the given graph. The graph is supposed to be connex and 
        eulerian. """
    




#############################################################################
k = 3

t = "ACGCGTCGCGACGCACG"
print("Text = " + t)
nodes, edges = deBruijnize(t, k)

print(nodes)
# should print {'GCA', 'GCG', 'TCG', 'CAC', 'GAC', 'CGT', 
# 'CGA', 'ACG', 'GTC', 'CGC'}

print(edges)
# should print [('ACG', 'CGC'), ('CGC', 'GCG'), ('GCG', 'CGT'), 
# ('CGT', 'GTC'), ('GTC', 'TCG'), ('TCG', 'CGC'), ('CGC', 'GCG'), 
# ('GCG', 'CGA'), ('CGA', 'GAC'), ('GAC', 'ACG'), ('ACG', 'CGC'), 
# ('CGC', 'GCA'), ('GCA', 'CAC'), ('CAC', 'ACG')]

print(deBruijn2Str(t, nodes, edges, k))
# should print 
# digraph "DeBruijn graph" {
#   GCA [label="GCA"] ;
#   GCG [label="GCG"] ;
#   TCG [label="TCG"] ;
#   CAC [label="CAC"] ;
#   GAC [label="GAC"] ;
#   CGT [label="CGT"] ;
#   CGA [label="CGA"] ;
#   ACG [label="ACG"] ;
#   GTC [label="GTC"] ;
#   CGC [label="CGC"] ;
#   ACG -> CGC ;
#   CGC -> GCG ;
#   GCG -> CGT ;
#   CGT -> GTC ;
#   GTC -> TCG ;
#   TCG -> CGC ;
#   CGC -> GCG ;
#   GCG -> CGA ;
#   CGA -> GAC ;
#   GAC -> ACG ;
#   ACG -> CGC ;
#   CGC -> GCA ;
#   GCA -> CAC ;
#   CAC -> ACG ;
# }

deBruijn2Dot(t, nodes, edges, "multi1.dot")

print(checkEulerian(nodes, edges))
# should print True

print("Eulerian cycle :")
print( buildEulerianCycle(nodes, edges))

###############################################################################
t = "ACGCGTCGCGACGC"
print("\nText = " + t)

nodes, edges = deBruijnize(t, k)

print(nodes)
# should print {'GCA', 'GCG', 'TCG', 'CAC', 'GAC', 'CGT', 'CGA', 
# 'ACG', 'GTC', 'CGC'}

print(edges)
# should print [('ACG', 'CGC'), ('CGC', 'GCG'), ('GCG', 'CGT'), 
#('CGT', 'GTC'), ('GTC', 'TCG'), ('TCG', 'CGC'), ('CGC', 'GCG'), 
#('GCG', 'CGA'), ('CGA', 'GAC'), ('GAC', 'ACG'), ('ACG', 'CGC')]

print(deBruijn2Str(t, nodes, edges, k))
# should print
# digraph "DeBruijn graph" {
#   GCG [label="GCG"] ;
#   TCG [label="TCG"] ;
#   GAC [label="GAC"] ;
#   CGT [label="CGT"] ;
#   CGA [label="CGA"] ;
#   ACG [label="ACG"] ;
#   GTC [label="GTC"] ;
#   CGC [label="CGC"] ;
#   ACG -> CGC ;
#   CGC -> GCG ;
#   GCG -> CGT ;
#   CGT -> GTC ;
#   GTC -> TCG ;
#   TCG -> CGC ;
#   CGC -> GCG ;
#   GCG -> CGA ;
#   CGA -> GAC ;
#   GAC -> ACG ;
#   ACG -> CGC ;
# }
deBruijn2Dot(t, nodes, edges, "multi2.dot")

print(checkEulerian(nodes, edges))
# should print True