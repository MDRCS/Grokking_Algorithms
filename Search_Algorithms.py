#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 21:28:49 2019

@author: mdrahali
"""
import statistics as st


def search(arr,x):
    high = len(arr) -1
    low = 0
    
    # While you haven’t narrowed it down to one element -> so any index that make high == low -> mid = (high+low)//2 
    #result gonna be mid == low | high 
    while low<=high:
        mid = (high+low)//2
        if arr[mid]>x:
            high = mid -1
        elif arr[mid] < x:
            low = mid + 1
        elif arr[mid] == x:
            return mid
    
    return -1
            

def count_down(n):
    if n>=0:
        print(n)
        count_down(n-1)
        
def fact(n):
    
    if n == 1:
        return 1
    
    return fact(n-1) * n       

def Euclid(l,d):
    
    r = l % d
    if r == 0:
        return d
    
    l = d
    d = r
    Euclid(l,d)
    
    
def sum_recur(ls,i):
    
    if i >= len(ls):
        return 0
    else:
        return ls[i] + sum_recur(ls,i+1)


def count(ls,i):
    
    if i >= len(ls):
        return 0
    else:
        return count(ls,i+1) + 1
        
def maxx(ls,i,mx):
    
    if i >= len(ls):
        return mx
    else:
        if mx<ls[i]:
            mx,ls[i] = ls[i],mx
        return maxx(ls,i+1,mx)

def recursion_search(arr,low,high,x):
    
    if low < high:
        mid = (low + high) // 2
        print(mid,arr[mid])
        if arr[mid] > x:
            print(mid,arr[mid])
            recursion_search(arr,low,mid-1,x)
        elif arr[mid] < x:
            print(mid,arr[mid])
            recursion_search(arr,mid+1,high,x)
        elif arr[mid] == x:
            print(mid,arr[mid])
            return mid     
            print("bla bla")
            
    return -1
  
#[10, 5, 2, 3]
#[5, 2, 3] 10 []
#[2, 3] 5 []
#[] 2 [3]
#[2, 3, 5, 10]    


def quicksort_simple(ls):
    
    less = []    
    greater = []
    equal = [] # we added equal because of duplicated items in the array, 
    #if we had duplicated numbers the algorithm wouldn't take them in consideration, pivot is always size 1 
    
    if len(ls) <= 1:
        return ls
    else:
        pivot = ls[0] #we cannot choose a pivot bigger than 0 because the minimum array that we couldhave is an array size 1
        for i in ls:
            if i > pivot:
                greater.append(i)
            elif i == pivot:
                equal.append(i)
            elif i < pivot:
                less.append(i)
        print(less,equal,greater)
        return quicksort_simple(less) + equal + quicksort_simple(greater)


def quicksort(ls):
    
    if len(ls) < 2:
        return ls
    else:
        pivot  = ls[0]
        less = [i for i in ls[1:] if i <= pivot]
        greater = [i for i in ls[1:] if i > pivot]
        print(less,pivot,greater)
        return quicksort(less) + [pivot] + quicksort(greater)

def selection_sort(arr):
    m = arr[0]
    
    for i in range(1,len(arr)):
        if arr[i] < m:
            arr[i],m = m,arr[i]
    print(arr)

if __name__ == "__main__":
    
    ls = [10, 5, 2,3,5,1,6,7]
    print(ls)
    #i = search(ls,3)
    #print(recursion_search(ls,0,len(ls),3))
    #n = fact(5)
    #n = Euclid(1680,640)
    #mx = ls[0]
    #summ = sum_recur(ls,0)
    #mx = maxx(ls,0,mx)
    #ct = count(ls,0)
    ls = quicksort(ls)
    print(ls)
    print()
    #count_down(10)
    
#    if i != -1:
#        print(i,"index of",ls[i])
#    else:
#        print("this value doesn't exist ")
    
    #selection_sort(ls)