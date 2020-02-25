#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 00:45:42 2019

@author: mdrahali
"""

class graph(object):
    
    def __init__(self,key,edges):
        self.key = key
        self.edges = edges
        
    def getKey(self):
        return self.key
    
    def getEdges(self):
        
        n = len(self.edges)
        
        stng = ""
        for i in range(n):
            stng+= self.edges[i].__str__()
        return stng
    
    def display_edges(self):
        n = len(self.edges)
        
        for i in range(n):
            print(self.edges[i],end='')
    
    def __str__(self):
        return "[" + str(self.key) + " - " + str(self.getEdges()) + "]"
    
class point(object):
    
    def __init__(self,key,distance):
        self.key = key
        self.distance = distance
    
    def __str__(self):
        return "[" + str(self.key) + " - " + str(self.distance) + "]"
    
class hashtable(object):
    
    def __init__(self,size=10):
        self.size = size
        self.array = [None]*self.size
        self.count = 0
        
    def hashing(self,key):
        val = 0
        for i in key:
            #print(i,ord(i))
            val += ord(i)
        return (val % self.size)
    
    def resizing(self):
        new_size = self.Prime_size()
        new_array = [None] * new_size
        
        for i in range(self.size):
            if self.array[i] is not None:
                new_array[i] = self.array[i]
        
        self.array = new_array
        self.size = new_size
        
        
        
    def isPrime(self,x):
        for i in range(2,x):
            if i%x== 0:
                return False
        return True
    
    def Prime_size(self):
        nsize = self.size*2
        
        while not self.isPrime(nsize) :
            nsize +=1
            
        return nsize
    
    def load_factor(self):
        
        lf = (self.count/self.size) * 100
        if lf >= 70:
            return True
        return False
    
    def insert(self,grp):
        
#        if self.load_factor():
#            self.resizing()

        hs = self.hashing(grp.key)
        index = hs
        for i in range(self.size):
            if self.array[index] is None:
                self.array[index] = grp
                self.count +=1
                return
            index = (hs + i) % self.size #linear probing
        

    
    def display(self):
        
        for i in range(self.size):
            if self.array[i] is not None:
                print("[",end='') ; print(self.array[i].getKey(),end='') ; print("] -> ",end='') ;
                if len(self.array[i].edges) != 0:
                    print(self.array[i].getEdges()) 
                else:
                    print("___")
            else:
                print("___")
    
    def salesman_problem(self):
        min_dist = float('inf')
        min_key = ''
        key = ''
        processed = set([])
        solution = hashtable(self.size)
        for i in range(self.size):
            min_dist = float('inf')
            min_key = ''
            key = ''
            key, min_key, min_dist = self.min_distance(min_dist,min_key,key,processed)
            p = point(min_key,min_dist)
            grp = graph(key,[p])
            solution.insert(grp)
        print(processed,"\n")
        return solution
        
    
    def min_distance(self,min_dist,min_key,key,processed):
        n = self.size
        for i in range(n):
           for j in range(len(self.array[i].edges)):
               if self.array[i].key not in processed and self.array[i].edges[j].distance < min_dist:
                   min_dist = self.array[i].edges[j].distance 
                   min_key = self.array[i].edges[j].key
                   key = self.array[i].key
        processed.add(key)
        return key,min_key,min_dist

if __name__ == "__main__" :

    p1 = point('B', 22) 
    p2 = point('C', 10)
    p3 = point('D', 14)
    p4 = point('E', 15)
    
    grp = graph("A",[p1, p2, p3,p4])
    
    p1 = point('A', 20) 
    p2 = point('C', 16)
    p3 = point('D', 25)
    p4 = point('E', 4)
    
    grp_1 = graph("B",[p1, p2, p3,p4])
    
    p1 = point('A', 32) 
    p2 = point('B', 56)
    p3 = point('D', 23)
    p4 = point('E', 41)
    
    grp_2 = graph("C",[p1, p2, p3,p4])
    
    p1 = point('A', 27) 
    p2 = point('B', 13)
    p3 = point('C', 48)
    p4 = point('E', 29)
    
    grp_3 = graph("D",[p1, p2, p3,p4])
    
    p1 = point('A', 6) 
    p2 = point('B', 26)
    p3 = point('C', 33)
    p4 = point('D', 11)
    
    grp_4 = graph("E",[p1, p2, p3,p4])
    
    ht = hashtable(5)
    ht.insert(grp) 
    ht.insert(grp_1)
    ht.insert(grp_2)
    ht.insert(grp_3)
    ht.insert(grp_4) 
    
    st = ht.salesman_problem()
    st.display()
    

