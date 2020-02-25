#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 17:22:47 2019

@author: mdrahali
"""

""" KNN AKA K-nearest-neighbors is an algorithm with which we could make a recommandation system, 
the algo is simple,easy and powerful, the process is to calculate distance between two things (users in our example) 
based on a vector (point) size between [2..N] (x,y) OR (a,b,c .. ,Z) list of numbers (quantitatif features) 
to do classification of the two things (users) and also see what you will recommand to the user."""

import math  

def knn_recommandation_system(Priyanka,Justin):
    
    distance = 0
    
    for i in range(len(Priyanka)):
        print((Priyanka[i] - Justin[i]) ** 2  )
        distance += (Priyanka[i] - Justin[i]) ** 2
    
    #print(math.sqrt(distance))
    
    if math.sqrt(distance) > 2:
        print(math.sqrt(distance)," - Priyanka interest is not the same as Justin")
    else:
        print(math.sqrt(distance)," - Priyanka have the same interest as Justin")

    
if __name__ == "__main__":
    
    """ Feature Vector [3,4,4,1,4] is quantitatif representation of average ranking of each movies category
        [Comedie, Action, Drama, Horror, Romance] """
    
    Priyanka = [3,4,4,1,4]  
    Justin = [4,3,5,1,5]
    Morpheus = [2,5,1,3,1]
    
    """ Priyanka could help us to recommand movies to Justin """
    knn_recommandation_system(Priyanka,Morpheus)