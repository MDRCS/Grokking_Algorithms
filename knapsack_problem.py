#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  7 11:54:03 2019

@author: mdrahali
"""
import json

#in this file, i will solve kanpsack problem using dynamic programming

def dp_knapsack_algorithm(items,capacity_knapsack):
    n = capacity_knapsack
    #m = len(items)
    solution = {}
    prec = ""
    l = None
    for key,value in items.items():
        lis = []
        #initialization
        if key == "Guitar":
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
                        li = items[prec] 
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
    
    items = {}
    items["Guitar"] = [1500,1]
    items["Stereo"] = [3000,8]
    items["Laptop"] = [2000,6]
    items["Iphone"] = [2000,2]
    items["MP3"] = [1000,2]
    items["Necklace"] = [1000,1]
    
    
    #print(items.get("Guitar")[1])
    sol = dp_knapsack_algorithm(items,8)
    #print(sol)
    #print(json.dumps(sol, indent=4, sort_keys=True)) #if you want to sort the result
    print(json.dumps(sol, indent=4))

    
    
    
    
    
    
    
    
    
    
    
    
    
    