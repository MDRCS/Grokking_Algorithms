#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 19:55:19 2019

@author: mdrahali
"""

class StackOverFlowError(Exception):
    pass

class NotFoundError(Exception):
    pass

class cost(object):
    
    def __init__(self,key,value):
        self.key = key
        self.cost = value
    
    def __str__(self):
        return self.key + " - " + str(self.cost)
    
class parent(object):
    
    def __init__(self,key,value):
        self.key = key
        self.parent = value
    
    def __str__(self):
        return str(self.key) + " - " + str(self.parent)

class graph(object):
    
    def __init__(self,key,neighbours):
        self.key = key
        self.neighbours = neighbours
    
    def __str__(self):
        strr = " "
        if self.neighbours is None:
            return strr + "None"
        else:
            for i in range(len(self.neighbours)):
                strr += "[" + str(self.neighbours[i]) + "]  "
            return self.key + " - " + strr
     
    def search(self,key):
        
        n = len(self.neighbours)
        
        for i in range(n):
            if self.neighbours[i] is not None and self.neighbours[i].key == key:
                return self.neighbours[i]
        
        
        
        
    def display_neighbours(self):
        strr = ""
        if self.neighbours is None:
            return strr + " - None"
        else:
            for i in range(len(self.neighbours)):
                strr += "[" + str(self.neighbours[i]) + "]  "
            return " - " + strr
    
class hashtable(object):
    
    def __init__(self,size=11):
        self.size = size
        self.array = [None] * self.size
        self.count = 0
    
    def hashing(self,key):
        val = 0
        for i in key:
            #print(i,ord(i))
            val += ord(i)
        return (val % self.size)
    
    def rehashing(self,key):
        n  = self.size 

        for i in range(n-1,0,-1):
            if self.isPrime(i):
                return (i - (key%i))

    def isPrime(self,v):
        for x in range(2,v):
            if v % x == 0:
                return False
        return True
    
    def insert(self,node):
        
#        if self.count >= self.size // 2:
#            self.resizing()
            
        n = self.size
        hs = self.hashing(node.key)
        index = hs
        for i in range(n+1):
            if self.array[index] is None or self.array[index].key == -1:
                self.array[index] = node
                self.count+=1
                return
            
            index = (hs + i) % self.size  #Linear probing
            #index = (hs + i**2)% self.size #Quadratic probing
            #index = (hs + i*self.rehashing(node.key)) % self.size #double hashing
        return 
        raise StackOverFlowError("There is no space to store the new record ..")
        
    def resizing (self):
        htable = hashtable(self.size*2)
        n = self.size
        for i in range(n):
            if self.array[i] is not None:
                htable.array[i] = self.array[i]
            
        self.array = htable.array
        self.size = htable.size
        
    
    def search(self,key):

        n = self.size
        hs = self.hashing(key)
        index = hs
        
        for i in range(n+1):
            if self.array[index] is not None and self.array[index].key == key:
                return self.array[index]
            
            index = (hs + i) % self.size  #Linear probing
            #index = (hs + i**2)% self.size #Quadratic probing
            #index = (hs + i*self.rehashing(student.getStudentId())) % self.size #double hashing
        return None
        raise NotFoundError("Not Found Record ..")
        
    def cost_search(self,key):
        n = self.size
        hs = self.hashing(key)
        index = hs
        
        for i in range(n+1):
            if self.array[index] is not None and self.array[index].key == key:
                return self.array[index].cost
            
            index = (hs + i) % self.size  #Linear probing
            #index = (hs + i**2)% self.size #Quadratic probing
            #index = (hs + i*self.rehashing(student.getStudentId())) % self.size #double hashing
        
        raise NotFoundError("Not Found Record ..")
    
    def dijkstra_algorithm(self,costs,parents):
        processed = []
        node = costs.lowest_costnode(processed)
        while node is not None:
            graph = self.search(node.key)
            cst = node.cost
            if graph.neighbours is not None:
                for x in graph.neighbours :  
                    node = self.search(node.key)
                    new_cost = cst + node.search(x.key).cost
                    if costs.search(x.key) is not None and new_cost < costs.search(x.key).cost :
                        cst_update = costs.search(x.key)
                        cst_update.cost = new_cost
                        prnt_update = parents.search(x.key)
                        prnt_update.parent = node.key
            processed.append(node.key)
            node = costs.lowest_costnode(processed)
        print(processed)
        
        
    def lowest_costnode(self,processed):
        n = self.size
        node = None
        mn = float("infinity")
        for i in range(0,n):
            key = self.array[i].key
            if self.array[i].cost < mn and self.isprocessed(key,processed):     
                node  = self.array[i]
                mn = self.array[i].cost
        return node
        
    def isprocessed(self,key,processed):
        
        n = len(processed)
        for i in range(n):
            if key == processed[i]:
                return False
        return True
    
    def display(self):
        n = self.size
        
        print("\n Graph - Matrix  \n")
        
        for i in range(n):
            
            if self.array[i] is not None:
                print("[",end='') ; print(self.array[i].key,end='') ; print("]",end='') ;
                print(self.array[i].display_neighbours())

    def cost_display(self):
        
        print("\n COST - Matrix  \n")
        
        n = self.size
        
        for i in range(n):
            
            if self.array[i] is not None:
                print("[",end='') ; print(self.array[i].key,end='') ; print("]",end='') ;
                print(" - " + str(self.array[i].cost))
        
        
    def parent_display(self):
        
        print("\n PARENTS  - Matrix  \n")
        
        n = self.size
        
        for i in range(n):
            if self.array[i] is not None:
                print("[",end='') ; print(self.array[i].key,end='') ; print("]",end='') ;
                print(" - " + str(self.array[i].parent.__str__()))
                
    def isexist(self,key):
        
        n = self.size
        
        for i in range(n):
            if self.array[i] is not None and self.array[i].key == key:
                return False
        return True
        
if __name__ == "__main__":

    
    
#################################################################
#EXAMPLE DIRECTED ACYCLIC GRAPH
        print("\n EXAMPLE OF DIRECTED ACYCLIC GRAPH")
# Initialization 
    
        cst_1 = cost("2",5)
        cst_2 = cost("3",2)
        cst_3 = cost("2",8)
        cst_4 = cost("5",7)
        cst_5 = cost("4",4)
        cst_6 = cost("5",2)
        cst_7 = cost("6",1)
        cst_8 = cost("5",6)
        cst_9 = cost("6",3)
        
        
        ngbr_1 = []
        ngbr_1.append(cst_1)
        ngbr_1.append(cst_2)
        
        ngbr_2 = []
        ngbr_2.append(cst_5)
        ngbr_2.append(cst_6)
        
        ngbr_3 = []
        ngbr_3.append(cst_3)
        ngbr_3.append(cst_4)
        
        ngbr_4 = []
        ngbr_4.append(cst_8)
        ngbr_4.append(cst_9)
        
        ngbr_5 = []
        ngbr_5.append(cst_7)
        

        

        node_1 = graph("1",ngbr_1)
        node_2 = graph("2",ngbr_2)
        node_3 = graph("3",ngbr_3)
        node_4 = graph("4",ngbr_4)
        node_5 = graph("5",ngbr_5)
        node_6 = graph("6",None)
        
        graph_matrix = hashtable(6)
        
        graph_matrix.insert(node_1)
        graph_matrix.insert(node_2)
        graph_matrix.insert(node_3)
        graph_matrix.insert(node_4)
        graph_matrix.insert(node_5)
        graph_matrix.insert(node_6)
        
        costt = hashtable(6) #COST MATRIX
        prntt = hashtable(6) #PARENT MATRIX
        
        start_node = graph_matrix.search("1") #START NODE
        end_node = graph_matrix.search("6")   #END NODE
        
        for i in range(len(start_node.neighbours)):
            costt.insert(start_node.neighbours[i])
            prntt.insert(parent(start_node.neighbours[i].key,start_node.key))
        
        #print(costt.cost_display())
        infinity = float("inf")
        for i in range(graph_matrix.size):
            key = graph_matrix.array[i].key
            if costt.isexist(key):
                costt.insert(cost(key,infinity))
                prntt.insert(parent(key,None))
        #prnt = parent(end_node.key,None)
        #prntt.insert(prnt)
        
        
        new = cost(end_node.key,infinity)
        costt.insert(new)  

        print("\n \n Initialization \n")
        
        costt.cost_display()
        graph_matrix.display()
        prntt.parent_display()
        
        
############################################################
        
#Implementation of Dijkstra's algorithm     
        
        print("\n \n")
        
        graph_matrix.dijkstra_algorithm(costt,prntt)
        
        print("\n \n Solution \n")
        
        costt.cost_display()
        graph_matrix.display()
        prntt.parent_display()
    
#################################################################
#EXAMPLE DIRECTED CYCLIC GRAPH
        print("\n EXAMPLE OF DIRECTED CYCLIC GRAPH")
# Initialization 
    
        cst_1 = cost("A",10)
        cst_2 = cost("C",20)
        cst_3 = cost("A",1)
        cst_4 = cost("B",1)
        cst_5 = cost("FIN",30)

        
        
        ngbr_1 = []
        ngbr_1.append(cst_1)
        
        ngbr_2 = []
        ngbr_2.append(cst_2)
        
        ngbr_3 = []
        ngbr_3.append(cst_3)
        
        ngbr_4 = []
        ngbr_4.append(cst_4)
        ngbr_4.append(cst_5)
        
        

        

        node_1 = graph("START",ngbr_1)
        node_2 = graph("A",ngbr_2)
        node_3 = graph("B",ngbr_3)
        node_4 = graph("C",ngbr_4)
        node_5 = graph("FIN",None)
        
        graph_matrix = hashtable(5)
        
        graph_matrix.insert(node_1)
        graph_matrix.insert(node_2)
        graph_matrix.insert(node_3)
        graph_matrix.insert(node_4)
        graph_matrix.insert(node_5)
        
        costt = hashtable(5) #COST MATRIX
        prntt = hashtable(5) #PARENT MATRIX
        
        start_node = graph_matrix.search("START") #START NODE
        end_node = graph_matrix.search("FIN")   #END NODE
        
        for i in range(len(start_node.neighbours)):
            costt.insert(start_node.neighbours[i])
            prntt.insert(parent(start_node.neighbours[i].key,start_node.key))
        
        #print(costt.cost_display())
        infinity = float("inf")
        for i in range(graph_matrix.size):
            key = graph_matrix.array[i].key
            if costt.isexist(key):
                costt.insert(cost(key,infinity))
                prntt.insert(parent(key,None))
        #prnt = parent(end_node.key,None)
        #prntt.insert(prnt)
        
        
        new = cost(end_node.key,infinity)
        costt.insert(new)  

        print("\n \n Initialization \n")
        
        costt.cost_display()
        graph_matrix.display()
        prntt.parent_display()
        
        
############################################################
        
#Implementation of Dijkstra's algorithm     
        
        print("\n \n")
        
        graph_matrix.dijkstra_algorithm(costt,prntt)
        
        print("\n \n Solution \n")
        
        costt.cost_display()
        graph_matrix.display()
        prntt.parent_display()
    
    
    
#################################################################
#EXAMPLE DIRECTED CYCLIC GRAPH
        print("\n EXAMPLE OF DIRECTED CYCLIC GRAPH WITH NEGATIVE WEIGHT")
# Initialization 
    
        cst_1 = cost("A",2)
        cst_2 = cost("B",2)
        cst_3 = cost("C",2)
        cst_4 = cost("FIN",2)
        cst_5 = cost("A",2)
        cst_6 = cost("FIN",2)
        cst_7 = cost("B",-1)
        
        
        ngbr_1 = []
        ngbr_1.append(cst_1)
        ngbr_1.append(cst_2)
        
        ngbr_2 = []
        ngbr_2.append(cst_3)
        ngbr_2.append(cst_4)
        
        ngbr_3 = []
        ngbr_3.append(cst_5)
        
        ngbr_4 = []
        ngbr_4.append(cst_6)
        ngbr_4.append(cst_7)
        
        

        

        node_1 = graph("START",ngbr_1)
        node_2 = graph("A",ngbr_2)
        node_3 = graph("B",ngbr_3)
        node_4 = graph("C",ngbr_4)
        node_5 = graph("FIN",None)
        
        graph_matrix = hashtable(5)
        
        graph_matrix.insert(node_1)
        graph_matrix.insert(node_2)
        graph_matrix.insert(node_3)
        graph_matrix.insert(node_4)
        graph_matrix.insert(node_5)
        
        costt = hashtable(5) #COST MATRIX
        prntt = hashtable(5) #PARENT MATRIX
        
        start_node = graph_matrix.search("START") #START NODE
        end_node = graph_matrix.search("FIN")   #END NODE
        
        for i in range(len(start_node.neighbours)):
            costt.insert(start_node.neighbours[i])
            prntt.insert(parent(start_node.neighbours[i].key,start_node.key))
        
        #print(costt.cost_display())
        infinity = float("inf")
        for i in range(graph_matrix.size):
            key = graph_matrix.array[i].key
            if costt.isexist(key):
                costt.insert(cost(key,infinity))
                prntt.insert(parent(key,None))
        #prnt = parent(end_node.key,None)
        #prntt.insert(prnt)
        
        
        new = cost(end_node.key,infinity)
        costt.insert(new)  

        print("\n \n Initialization \n")
        
        costt.cost_display()
        graph_matrix.display()
        prntt.parent_display()
        
        
############################################################
        
#Implementation of Dijkstra's algorithm     
        
        print("\n \n")
        
        graph_matrix.dijkstra_algorithm(costt,prntt)
        
        print("\n \n Solution \n")
        
        costt.cost_display()
        graph_matrix.display()
        prntt.parent_display()
    
#    
#    
#    
#    
################################################################## 
## Initialization 
#    
#        cst_1 = cost("A",6)
#        cst_2 = cost("B",2)
#        cst_3 = cost("FIN",1)
#        cst_4 = cost("A",3)
#        cst_5 = cost("FIN",5)
#        cst_6 = cost("FIN",None)
#        
#        
#        ngbr = []
#        ngbr.append(cst_1)
#        ngbr.append(cst_2)
#        
#        #print(ngbr[0])
#        
#        ngbr_1 = []
#        ngbr_1.append(cst_3)
#        
#        ngbr_2 = []
#        ngbr_2.append(cst_4)
#        ngbr_2.append(cst_5)
#        
#        ngbr_3 = []
#        ngbr_3.append(cst_6)
#
#        
#        node = graph("START",ngbr)
#        node_1 = graph("A",ngbr_1)
#        node_2 = graph("B",ngbr_2)
#        node_3 = graph("FIN",None)
#        
#        
#        graph_matrix = hashtable(4)
#        
#        graph_matrix.insert(node)
#        graph_matrix.insert(node_1)
#        graph_matrix.insert(node_2)
#        graph_matrix.insert(node_3)
#        
#        costt = hashtable(graph_matrix.size-1) #COST MATRIX
#        prntt = hashtable(graph_matrix.size-1) #PARENT MATRIX
#        
#        start_node = graph_matrix.search("START") #START NODE
#        end_node = graph_matrix.search("FIN")   #END NODE
#        
#        for i in range(len(start_node.neighbours)):
#            costt.insert(start_node.neighbours[i])
#            prntt.insert(parent(start_node.neighbours[i].key,start_node.key))
#
#        prnt = parent(end_node.key,None)
#        prntt.insert(prnt)
#        
#        infinity = float("inf")
#        new = cost(end_node.key,infinity)
#        costt.insert(new)  
#
#        print("\n \n Initialization \n")
#        
#        costt.cost_display()
#        graph_matrix.display()
#        prntt.parent_display()
#        
#        
#############################################################
#        
##Implementation of Dijkstra's algorithm     
#        
#        print("\n \n")
#        
#        graph_matrix.dijkstra_algorithm(costt,prntt)
#        
#        print("\n \n Solution \n")
#        
#        costt.cost_display()
#        graph_matrix.display()
#        prntt.parent_display()
#        
#        
#        
#        
#        
#        
#        
#        
#        
#        
#        
#        
#        
#        
#        
#        
#        
#        
#        
#        
        
        
        
        
        
        
        
        
        
        
        
    