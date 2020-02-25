#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 18:48:36 2019

@author: mdrahali
"""

import math

""" Feature Vector [Weather [1..5], Weeknd | Holiday [1,0], There is a Game on [1,0]]
    
        Regression is very useful. Suppose you run a small bakery in Berkeley, and you make fresh bread every day. You’re trying to predict how many loaves to make for today. You have a set of features:
            • Weather on a scale of 1 to 5 (1 = bad, 5 = great).
            • Weekend or holiday? (1 if it’s a weekend or a holiday, 0 otherwise.)
            • Is there a game on? (1 if yes, 0 if no.)
        And you know how many loaves of bread you’ve sold in the past for different sets of features. """

def knn_classification_prediction(dataset,value,number_neighbours):

    result = {}
    dist = []
    for key,val in dataset.items():
        s = 0
        for i in range(len(val)):
            s+= (val[i] - value[i]) ** 2
        r =  math.sqrt(s) 
        result[key] = int(r)
        
    dist = [value for key,value in result.items()]        
    dist.sort()
    
    """ 5 is just a number if we want more accuracy we could pick more neighbors """
    
    mean = 0
    count = 0
    
    for key,value in result.items():
        if value == dist[i]:
            mean+=key
            count+=1
        if count == number_neighbours: break
            
    return mean/count
            
    
if __name__ == "__main__":
    
 
        dataset = {}
        dataset[300] = [5,1,0]
        dataset[225] = [3,1,1]
        dataset[75] = [1,1,0]
        dataset[200] = [4,0,1]
        dataset[150] = [4,0,0]
        dataset[50] = [2,0,0]
        
        number_neighbours = 5
        
        pred = knn_classification_prediction(dataset,[4,1,0],number_neighbours)
        
        print("the number of loaves that this bakery should produce for a Good weeknd day, when there is no game, ",pred)
        