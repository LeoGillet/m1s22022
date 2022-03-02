#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 24 13:30:36 2022

@author: ruricaru (adapted from Ben Langmead)
"""

from graphviz import Digraph
from collections import deque

#Note that this suffix-tree implementation stores string labels for the edges.
#In reality, to achieve the O(m) space bound, we store (offset, length) pairs 
#instead, where a pair refers to the substring of T labeling the edge.  
#We use substrings here to keep the code simpler.

class SuffixTree(object):
    
    class Node(object):
        def __init__(self, lab):
            self.lab = lab # label on path leading to this node
            self.out = {}  # outgoing edges; maps characters to nodes
    
    def __init__(self, s):
        """ Make suffix tree, without suffix links, from s in quadratic time"""
        s += '$'
        self.root = self.Node('root')
        self.root.out[s[0]] = self.Node(s) # trie for just longest suffix
        # add the rest of the suffixes, from longest to shortest
        
        for i in range(1, len(s)):
            # start at root; we’ll walk down as far as we can go
            cur = self.root
            j = i
            while j < len(s):
                if s[j] in cur.lab:
                    child = cur.out[s[j]]
                    lab = child.lab
                    # Walk along edge until we exhaust edge label or
                    # until we mismatch
                    k = j+1 
                    while k-j < len(lab) and s[k] == lab[k-j]:
                        k += 1
                    if k-j == len(lab):
                        cur = child # we exhausted the edge
                        j = k
                    else:
                        # we fell off in middle of edge
                        cExist, cNew = lab[k-j], s[k]
                        # create “mid”: new node bisecting edge
                        mid = self.Node(lab[:k-j])
                        mid.out[cNew] = self.Node(s[k:])
                        # original child becomes mid’s child
                        mid.out[cExist] = child
                        # original child’s label is curtailed
                        child.lab = lab[k-j:]
                        # mid becomes new child of original parent
                        cur.out[s[j]] = mid
                else:
                    # Fell off tree at a node: make new edge hanging off it
                    cur.out[s[j]] = self.Node(s[j:])
    
    def to_dot(self):
        """ Return Suffix Tree in graphviz representation. """
        g_st = Digraph()
        id_node = 0
        
        #BFS traversal of the tree using a queue
        q = deque()
        #use identifiers to obtain different nodes for same labels in the tree
        q.append((self.root, id_node)) 
        id_node += 1
        
        while q:
            (cur,id) = q.popleft()
            g_st.node(str(id), cur.lab)
            for char in cur.out:
                child = cur.out[char]
                q.append((child, id_node))
                g_st.edge(str(id), str(id_node))
                id_node += 1
            
        return g_st
    
    def followPath(self, p):
        """ Follow path given by p.  If we fall off tree, return None.  If we
            finish mid-edge, return (node, pos) where 'node' is the child
            to which we got and 'pos' is the position on the label where p ends. 
            If we finish on a node, return (node, None). """
        # cur = self.root
        for i in range(1, len(p)):
            # start at root; we’ll walk down as far as we can go
            cur = self.root
            j = i
            while j < len(p):
                if p[j] in cur.lab:
                    child = cur.out[p[j]]
                    lab = child.lab
                    # Walk along edge until we exhaust edge label or
                    # until we mismatch
                    k = j+1 
                    while k-j < len(lab) and p[k] == lab[k-j]:
                        k += 1
                        if k == len(p):
                            if lab[k-j] == '$' and '$' in cur.out.keys():
                                return cur, None
                            return cur, k
                    if k-j == len(lab):
                        if len(p) - 1 == j:
                            return cur, None
                        cur = child # we exhausted the edge
                        j = k
                    else:
                        # we fell off in middle of edge
                        return None
                else:
                    # Fell off tree at a node: make new edge hanging off it
                    if p[-1] == lab[j]:
                            return node, None
                    return None
        return NotImplemented

    
    def hasSubstring(self, p):
        """ Return true iff p appears as a substring """
        if self.followPath(p) is not None:
            return True
        return False
    
    def hasSuffix(self, p):
        """ Return true iff p is a suffix """
        result = self.followPath(p)
        if result is not None and result[1] is None:
            return True
        return False
        
def buildAndDrawST(s, name):
    """ Build suffix tree and return it, as well as its graphviz representation.
    Produce a png file corresponding to its representation. """
    st = SuffixTree(s)

    st_dot = st.to_dot()
    st_dot.format = 'png'
    st_dot.render(name, view = False)
    return st

########################################################################
#Test1

print('First test')
st1 = SuffixTree('there would have been a time for such a word')

print(st1.hasSubstring('nope'))
print(st1.hasSubstring('would have been'))
print(st1.hasSuffix('would have been'))
print(st1.hasSuffix('such a word'))

########################################################################
#Test2
print('\nSecond test')
st2 = buildAndDrawST('ABAABA', 'suffixTree2')
print(st2.hasSubstring('ABBA'))
print(st2.hasSubstring('AAB'))
print(st2.hasSubstring('ABA'))
print(st2.hasSuffix('ABA'))

########################################################################
#Test3
print('\nThird test')
st3 = buildAndDrawST('BANANA', 'suffixTree3')
print(st3.hasSubstring('BAN'))
print(st3.hasSubstring('NBA'))
print(st3.hasSubstring('ANA'))
print(st3.hasSuffix('BANA'))
