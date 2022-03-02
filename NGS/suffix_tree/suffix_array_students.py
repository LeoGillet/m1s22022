#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  3 15:20:32 2022

@author: ruricaru (adapted from Ben Langmead)
"""
import sys

def buildSuffixArray(s):
    """ Return an SA (list of indexes corresponding to suffixes 
    sorted in ascending lexicographical order) """
    s = s + '$'
    suff_asc = sorted([(s[i:], i) for i in range(len(s))])
    sa = map(lambda x: x[1], suff_asc)
    return list(sa)
    
def printSA(s, sa):
    """ Print suffixes and corresponding indexes in ascending order"""
    s = s + '$'
    print("\n"+s)
    index = 0
    for si in sa :
        print(f"[{index:>2d}] {si:>3d} : {s[si:]}")
        index += 1

def firstIndex(s, sa, p):
    """ Return FIRST suffix array row index with p as a prefix of the corresponding suffix
        if such element exists, or the position where it would be otherwise. """
    s = s + '$'
    start = 0
    end = len(s)-1
    while start <= end:
        middle = (start+end)//2
        midpoint = s[sa[middle]:]
        if end-start <= 1:
            # print(f"Interval size is: {end-start} [{start} - {end} | {midpoint}]")
            if p <= midpoint:
                return start  
            else:
                return end
        elif p <= midpoint:
            end = middle 
        elif p > midpoint:
            start = middle + 1


    
def rangeSA(s, sa, p):
    """ Return the range of suffix array row indexes [l, r) having p as a prefix,
        or empty range (r<=l) if no elements have p as a prefix.
        Tip : use ord and chr functions."""
    nextpat = p[:-1]+chr(ord(p[-1])+1)
    find = firstIndex(s, sa, p)
    lind = firstIndex(s, sa, nextpat)
    return find, lind

def hasSubstring(s, sa, p):
    """ Return true if and only if p is substring of indexed text s"""
    ra = rangeSA(s, sa, p)
    for i in range(ra[0], ra[1]):
        if s[sa[i]:sa[i]+len(p)] == p:
            return True
    return False
    
def hasSuffix(s, sa, p):
    """ Return true if and only if p is a suffix of indexed text s"""
    ra = rangeSA(s, sa, p)
    for i in range(ra[0], ra[1]):
        if s[sa[i]:] == p:
            return True
    return False

def sa2BWT(s, sa):
    """ Return BWT string from suffix array (along with row where $ occurs)"""
    bw = ""
    s = s + '$'
    for i in sa:
        bw += s[i-1]
    return bw

def testPattern(s, sa, p):
    idx = firstIndex(s, sa, p)
    #exit program if firstIndex not yet implemented
    if idx is None:
        sys.exit("firstIndex function not yet implemented")
        
    if idx < len(sa):
        print(f"\n{p} should start suffix {sa[idx]} = {s[sa[idx]:]}")
        if hasSubstring(s, sa, p):
            print(f"{p} is a substring of {s}")
            l, r = rangeSA(s, sa, p)
            if l == r-1:
                print(f"{p} starts suffix {sa[l]} = {s[sa[l]:]}")
            else:
                print(f"{p} starts suffixes from {sa[l]} = {s[sa[l]:]} to {sa[r-1]} = {s[sa[r-1]:]}")
            if hasSuffix(s, sa, p):
                print(f"{p} is a suffix of {s}")
            else :
                print(f"{p} is not a suffix of {s}")
        else:
            print(f"{p} is not a substring of {s}")
    else :
        print(f"\n{p} is greater than all suffixes of {s}")

s = "bananababanaa"
sa = buildSuffixArray(s)
printSA(s, sa)
print(f"BWT({s}) = {sa2BWT(s,sa)}")
#BWT is aannbbnbaa$aaa

p = "banab"
testPattern(s, sa, p)
#must print 
#banab should start suffix 0 = bananababanaa
#banab is not a substring of bananababanaa

p = "nann"
testPattern(s, sa, p)
#must print
#nann is greater than all suffixes of bananababanaa

p = "bana"
testPattern(s, sa, p)
rangeSA(s, sa, p)
#must print
#bana should start suffix 8 = banaa
#bana is a substring of bananababanaa
#bana starts suffixes from 8 = banaa to 0 = bananababanaa
#bana is not a suffix of bananababanaa

p = "ana"
testPattern(s, sa, p)
#must print
#ana should start suffix 9 = anaa
#ana is a substring of bananababanaa
#ana starts suffixes from 9 = anaa to 1 = ananababanaa
#ana is not a suffix of bananababanaa

p = "anaa"
testPattern(s, sa, p)
#must print
#anaa should start suffix 9 = anaa
#anaa is a substring of bananababanaa
#anaa starts suffix 9 = anaa
#anaa is a suffix of bananababanaa