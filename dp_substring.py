#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 16:07:48 2019

@author: mdrahali
"""

"' in this file i will try to find the length of the longest substring between two words'"

"' the function return grid - 2D matrix where we did the calculation, '"
"' (dynamic programming technique all solutions are based on grid) length of the longest substring, and the substring  '"

def longest_substring(word_1,word_2):
    
    
    n = len(word_1)
    m = len(word_2)
    length = 0
    substring = set()
    grid = [ [ 0 for i in range(n) ] for j in range(m) ] 
    for i in range(n):
        for j in range(m):
            if word_1[i] == word_2[j]:
                grid[i][j] = grid[i-1][j-1] + 1
                if length < grid[i][j]:
                    length = grid[i][j]
                if grid[i-1][j-1] > 0:
                    substring.add(word_1[i])
                else:
                    substring = set()
                    substring.add(word_1[i])
            else:
                 grid[i][j] = 0
                 
    return grid,length,substring


def longest_subsequence(word_1,word_2):
    
    n = len(word_1)
    m = len(word_2)
    length = 0
    substring = set()
    grid = [ [ 0 for i in range(n) ] for j in range(m) ] 
    for i in range(n):
        for j in range(m):
            if word_1[i] == word_2[j]:
                grid[i][j] = grid[i-1][j-1] + 1
                if length < grid[i][j]:
                    length = grid[i][j]
                    
                substring.add(word_1[i])
                
            else:
                 grid[i][j] = 0
                 
    return grid,length,substring

if __name__ == "__main__":
    
    word_1 = "fish"
    word_2 = "fosh"

    
    print("the length of the longest substring is - ",longest_substring(word_1,word_2))
    print("the length of the longest subsequence is - ",longest_subsequence(word_1,word_2))
    
    
    
    
    