#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  7 19:18:35 2019

@author: mdrahali
"""

import json

#in this file, i will solve kanpsack problem using dynamic programming

#Optimizing your travel itinerary
#Suppose you’re going to London for a nice vacation. 
#You have two days there and a lot of things you want to do.
#You can’t do everything, so you make a list.

def dp_itinerary_algorithm(list_visit,capacity_knapsack):
    n = capacity_knapsack
    #m = len(items)
    solution = {}
    prec = ""
    l = None
    for key,value in list_visit.items():
        lis = []
        #initialization
        if key == "WT":
            for j in range(1,n+1):
                if value[1] <= j:
                    lis.append(value[0])
                else:
                    lis.append(0)
        else:
            
            for j in range(1,n+1):
                if value[1] == j:
                    if value[0] > l[j-1]:
                        lis.append(value[0])
                    elif value[0] < l[j-1]:
                        lis.append(l[j-1])
                    elif value[0] == l[j-1]:
                        li = list_visit[prec] 
                        if li[1] >= value[1]:
                            lis.append(value[0])
                        else:
                            lis.append(li[0])
                            
                elif j > value[1]:
                    lis.append(value[0]+l[j-value[1]-1])
                else:
                    lis.append(l[j-1])
                
        
        solution[key] = lis
        l = solution[key]
        prec = key    
    return solution
            

if __name__ == "__main__":
    
    list_visit = {}
    list_visit["WT"] = [7,1]
    list_visit["DP"] = [6,1]
    list_visit["GT"] = [9,2]
    list_visit["VST"] = [9,4]
    list_visit["MRT"] = [8,1]

    #print(items.get("Guitar")[1])
    sol = dp_itinerary_algorithm(list_visit,4) 
    #print(sol)
    print(json.dumps(sol, indent=4, sort_keys=True)) #if you want to sort the result


    
    
    
    
    
    
    
    
    
    
    
    
    
    