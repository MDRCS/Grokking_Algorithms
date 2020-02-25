#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 20:35:10 2019

@author: mdrahali
"""

from collections import deque

class graph(object):
    
    def __init__(self,key,edges):
        self.key = key
        self.edges = edges
        
    def getKey(self):
        return self.key
    
    def getEdges(self):
        return self.edges
    
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
        
        if self.load_factor():
            self.resizing()
        
        hs = self.hashing(grp.key)
        index = hs
        for i in range(self.size):
            if self.array[index] is None:
                self.array[index] = grp
                self.count +=1
                return
            index = (hs + i) % self.size #linear probing
            
    
    #Breadth first search Algorithm
    def closet_angel_investor(self):
        
        unchecked = deque()
        checked = []

        for j in range(self.size):
            if self.array[j] is not None and self.verify(checked, self.array[j].getKey()):
                unchecked.append(self.array[j])
                checked.append(self.array[j])
                v = unchecked.popleft()
            elif unchecked :             #len(unchecked) != 0:
                v = unchecked.popleft()

            if self.isAngelInvestor(v.getKey()):
                self.dis(checked)
                print("We found an angel investor", v.getKey())
                return
            
            for i in range(len(v.edges)):
                if self.verify(checked,v.edges[i]):
                    index = self.find_index(v.edges[i])
                    val = self.array[index]
                    checked.append(val)
                    unchecked.append(val)
                    
        self.dis(checked)
        print("\n \n We didn't found an angel investor")
     
        
    def dis(self,checked):
        for i in range(len(checked)):    
            print(checked[i].getKey() + " ",end='')  
        print("\n ")
        
    def find_index(self,key):
        
        hs = self.hashing(key)
        index = hs
        
        for i in range(self.size+1):
            if self.array[index] is not None and self.array[index].getKey() == key:
                return index
            index = (hs + i) % self.size
        
    
    def verify(self,arr_checked,key):

        for i in range(len(arr_checked)):
            if arr_checked[i].getKey() == key:
                return False
        return True
    
    def isAngelInvestor(self,job):
        #just a simulation of a function that check if that person is an angle investor
        
        return job[-1] == 'i'
    
    def display(self):
        
        for i in range(self.size):
            print("[",end='') ; print(i,end='') ; print("]",end='') ;
            if self.array[i] is not None:
                print(self.array[i].getKey(),"->",self.array[i].getEdges()) 
            else:
                print("___")
    

if __name__ == "__main__" :

    grp = graph("zxxxxli",["alice", "bob", "claire"])
    grp_1 = graph("bob",["anuj", "peggy"])
    grp_2 = graph("alice",["peggy"])
    grp_3 = graph("claire",["thom", "jonny"])
    grp_4 = graph("anuj",["thom", "jonny"])
    grp_6 = graph("peggy",[])
    grp_7 = graph("thom",[])
    grp_8 = graph("jonny",[])
    
    ht = hashtable(10)
    ht.insert(grp) 
    ht.insert(grp_1)
    ht.insert(grp_2)
    ht.insert(grp_3)
    ht.insert(grp_4) 
    ht.insert(grp_6) 
    ht.insert(grp_7)
    ht.insert(grp_8) 
    
    ht.display()
    
    ht.closet_angel_investor()
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            