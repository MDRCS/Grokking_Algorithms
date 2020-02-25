#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 18:34:54 2019

@author: mdrahali
"""

def linear_regression(rating):
    
    n = len(rating)
    s = 0
    for i in range(n):
        s+=rating[i]
    return s/n
    
if __name__ == "__main__":
    
    """ This feature vector represent rating for 5 movies, [The arrivals, The martian, Interstellar, La La land, Wolf of wall street] 
        the function that we will write will predict the movie - Suicide Squad based on 5 or N neighbors of Priyanka """
    
    Priyanka = Priyanka = [3,4,4,1,4] 
    
    rating = [5,4,4,5,3]
    
    print("prediction of Priyanka rating of Suicide squad movie is -",linear_regression(rating))