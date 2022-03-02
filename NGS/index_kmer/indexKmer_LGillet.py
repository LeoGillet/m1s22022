#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  8 11:12:35 2022

@author: ruricaru (adapted from Ben Langmead)
"""

def buildIndexKmer(t, k):
    ''' Create index for t from all k-mers, i.e. substrings of size k '''
    index = {}
    for i in range(len(t) - k + 1):  # for each k-mer
        kmer = t[i:i+k]
        if kmer not in index:
            index[kmer] = [i]
        else:
            index[kmer].append(i)
    return index

# The function takes the k-mer at position pos in p and returns 
# the list of positions where this k-mer is found in the text t.
# It uses the index built for the text from its substrings of size k.
def queryKmer(index, k, p, pos):
    ''' Return index hits for the k-mer starting at position pos in p '''
    kmer = p[pos:pos+k]
    try:
        return index[kmer] 
    except KeyError:
        return None


# The function takes the first k-mer in p and returns 
# the list of positions where this k-mer is found in the text t.
# It uses the index built for the text from its substrings of size k.
def queryFirstKmer(index, k, p):
    ''' Return index hits for the first k-mer of p '''
    return queryKmer(index, k, p, 0)

# Use the index built for the text from its substrings of size k,
# in order to find and return the list of the exact occurrences of p in t
def exactSearch(t, index, k, p):
    ''' Return positions in t where p matches exactly '''
    offsets = []
    if len(p) < k:
         print(f"The pattern is too small with respect to k={k}")
         return offsets
    starts = queryFirstKmer(index, k, p)
    if starts:
        for start in starts:
            if t[start:start+len(p)] == p:
                offsets.append(start)
    return offsets

# The function tests whether p is present in t at position pos with
# at maximum m mismatches, i.e. substitutions. It returns True or False.
def testOccurrence(t, p, pos, m):
    ''' Verify an occurrence of p with max m mismatches in t at position pos '''
    mismatches = 0
    subtext = t[pos:pos+len(p)]
    for i in range(len(p)):
        try:
            if p[i] != subtext[i]:
                mismatches += 1
            if mismatches > m:
                return False
        except IndexError:
            # La recherche a atteint la fin du texte
            return False
    return True


# The function looks for all approximate occurrence of p in t (at maximum
# m mismatches), based on the pigeonhole principle.
# It cuts the pattern in m+1 parts and looks for exact matches of these parts.
# Once an exact match is found, the rest of the pattern p is compared to t.
def approximateSearchPigeonhole(t, index, k, p, m):
    ''' Return positions for approximate occurrences of p in t, with maximum m mismatches. 
        Here we apply the pigeonhole principle : cut in m + 1 pieces and look for an exact
        match of a piece '''
    offsets = []
    nb_parts = m + 1
    size_part = len(p)//nb_parts
    parts = [p[i:i+size_part] for i in range(0, len(p), size_part)]
    parts[-2] = parts[-2]+parts[-1]
    parts.pop(-1)

    if size_part < k:
        print(f"The part of the pattern={size_part} is too small with respect to k={k}")
        return offsets

    for i in range(len(parts)):
        starts = exactSearch(t, index, k, parts[i])
        for start in starts:
            position = start-i*size_part
            if testOccurrence(t, p, position, m):
                if position not in offsets:
                    offsets.append(position)

    return offsets

# The function does the same thing as the previous one but this time without
# using the pigeonhole principle. It searches the exact occurrences of at least
# one k-mer from p and extends from there with m mismatches allowed.
def approximateSearch(t, index, k, p, m):
    ''' Return positions for approximate occurrences of p in t, with maximum m mismatches. 
        Here we start from an exact kmer and try to extend (not pigeonhole principle)'''
    offsets = []
    parts = [p[i:i+k] for i in range(0, len(p), k)]
    parts[-2] = parts[-2]+parts[-1]
    parts.pop(-1)
    
    if len(p) < k:
        print(f"The length of the pattern={p} is too small with respect to k={k}")
        return offsets

    for i in range(len(parts)):
        starts = exactSearch(t, index, k, parts[i])
        for start in starts:
            position = start-i*k
            if testOccurrence(t, p, position, m):
                if position not in offsets:
                    offsets.append(position)

    return offsets


def testPattern(t, index, k, p, m):
    print("\nPattern =", p)
    occ = exactSearch(t, index, k, p)
    print("Exact matches =", occ)

    occ = approximateSearch(t, index, k, p, m)
    print(f"Approx matches with {m} mm =", occ)
  
    occ = approximateSearchPigeonhole(t, index, k, p, m)
    print(f"Pigeonhole approx matches with {m} mm =", occ)
  
    

t = 'ACTTGGAGATCTTTGAGGCTAGGTATTCGGGATCGAAGCTCATTTCGGGGATCGATTACGATATGGTGGGTATTCGGGA'
print("Text =",t)
k = 4
index = buildIndexKmer(t, k)
print("Index =", index)
'''This should be printed
Index = {'ACTT': [0], 'CTTG': [1], 'TTGG': [2], 'TGGA': [3], 'GGAG': [4], 'GAGA': [5], 
'AGAT': [6], 'GATC': [7, 30, 49], 'ATCT': [8], 'TCTT': [9], 'CTTT': [10], 
'TTTG': [11], 'TTGA': [12], 'TGAG': [13], 'GAGG': [14], 'AGGC': [15], 'GGCT': [16],
 'GCTA': [17], 'CTAG': [18], 'TAGG': [19], 'AGGT': [20], 'GGTA': [21, 68], 
 'GTAT': [22, 69], 'TATT': [23, 70], 'ATTC': [24, 71], 'TTCG': [25, 43, 72], 
 'TCGG': [26, 44, 73], 'CGGG': [27, 45, 74], 'GGGA': [28, 47, 75], 'GGAT': [29, 48],
 'ATCG': [31, 50], 'TCGA': [32, 51], 'CGAA': [33], 'GAAG': [34], 'AAGC': [35], 
 'AGCT': [36], 'GCTC': [37], 'CTCA': [38], 'TCAT': [39], 'CATT': [40], 'ATTT': [41],
 'TTTC': [42], 'GGGG': [46], 'CGAT': [52, 58], 'GATT': [53], 'ATTA': [54], 
 'TTAC': [55], 'TACG': [56], 'ACGA': [57], 'GATA': [59], 'ATAT': [60], 'TATG': [61],
 'ATGG': [62], 'TGGT': [63], 'GGTG': [64], 'GTGG': [65], 'TGGG': [66], 'GGGT': [67]}
'''

p = 'GGTATTCGGGA'
m = 1
testPattern(t, index, k, p, m)
'''This should be printed
Pattern =  GGTATTCGGGA
Exact matches =  [21, 68]
Approx matches with 1 mm =  [21, 68]
Pigeonhole approx matches with 1 mm =  [21, 68]
'''

p = 'CGGGGAC'
m = 2
testPattern(t, index, k, p, m)
'''This should be printed
Pattern =  CGGGGAC
Exact matches =  []
Approx matches with 2 mm =  [27, 45]
The part of the pattern is too small with respect to k
Pigeonhole approx matches with 2 mm =  []
'''

p = 'AGGTAGTCGGGATCGAAACTCAC'
m = 3
testPattern(t, index, k, p, m)
'''This should be printed
Pattern =  AGGTAGTCGGGATCGAAACTCAC
Exact matches =  []
Approx matches with 3 mm =  [20]
Pigeonhole approx matches with 3 mm =  [20]
'''
