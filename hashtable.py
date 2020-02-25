#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 29 02:11:00 2019

@author: mdrahali
"""

class phone_number(object):
    
    def __init__(self,key,value):
        self.name = key
        self.number = value
    
    def getNumber(self):
        return self.number
    
    def getName(self):
        return self.name
    
    def __str__(self):
        return self.getName()+" - "+str(self.getNumber())

class hashtable(object):
    
    def __init__(self,nsize=10):
        self.size = nsize
        self.array = [None] * self.size
        self.count = 0
        
    def hashing(self,key):
        return len(key) % self.size
    
    def insert(self,phone_num):
        
        hs = self.hashing(phone_num.getName())
        index = hs
        print(index)
        for i in range(self.size+1): # for the linear probing if in the worst case we had a collision for the first index 
            #in the array and the empty case is the latest when i == self.size the last case the the loop condition is not valid 
            #he will quit so to prevent this problem the loop should be like this -> for i in range(self.size+1):
            if self.array[index] is None:
                self.array[index] = phone_num
                self.count+=1
                return
                
            index = (hs + i) % self.size # linear probing
            print(index,"here",i)
    
    def display(self):
        
        for i in range(self.size):
            print("[",end='') ;  print(i,end='') ;  print("]",end='') ;
            
            if self.array[i] is not None:
                 print(self.array[i])
            else:
                 print("___") ;
                 

if __name__ == "__main__":
    
    pn = phone_number("apple",33.5)
    p1 = phone_number("ananas",143.5)
    p2 = phone_number("bananas",22.25)
    p3 = phone_number("butter",70.0)
    p4 = phone_number("knife",10.40)
    ht = hashtable(5)

    
    ht.insert(pn)
    ht.insert(p1)
    ht.insert(p2)
    ht.insert(p3)
    ht.insert(p4)
    
    ht.display()
    
    
    
    