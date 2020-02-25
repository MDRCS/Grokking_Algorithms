#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 00:59:46 2019

@author: mdrahali
"""

from collections import deque

graph = {}
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = ["thom", "jonny"]
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = [] 

#def search(name):
#    search_queue = deque() 
#    search_queue += graph[name] 
#    searched = []
#    
#    while search_queue:
#        person = search_queue.popleft() 
#        if not person in searched:
#            if isSeller(person):
#                print(person + " is a mango seller!") 
#                return True
#            else:
#                search_queue += graph[person] 
#                searched.append(person)
#    return False 

def search(name):
    
    search_queue = deque() #Creates a new queue
    search_queue += graph[name]
    searched = []
    
    while search_queue:
        person = search_queue.popleft()
        #print(search_queue,person,"    ",end='')
    
        if not person in searched :      
            if isSeller(person):
                print(person + " is a seller")
                return True
            else:
                search_queue += graph[person]
                searched.append(person)
    return False
        
def isSeller(person):
    return (person == 'm')

print(search("you"))
    
    
    



