#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 22:34:02 2019

@author: mdrahali
"""

def greedy_algorithm(needed_states,stations,list_stations):
    
    while needed_states:
        best_station = None
        covered_states = set()
        for station, states in stations.items():
            #print(stations.items(),"\n")
            covered = needed_states & states #intersection between needed_states to cover and states of this station (index)
            if len(covered) > len(covered_states):
                best_station =  station
                covered_states = covered
        needed_states -= covered_states
        list_stations.add(best_station)
        


if __name__ == "__main__":
    
    stations = {}
    stations["kone"] = set(["id", "nv", "ut"])
    stations["ktwo"] = set(["wa", "id", "mt"])
    stations["kthree"] = set(["or", "nv", "ca"])
    stations["kfour"] = set(["nv", "ut"])
    stations["kfive"] = set(["ca", "az"])
    
    needed_states = set(stations["kone"] | stations["ktwo"] | stations["kthree"] | stations["kfour"] | stations["kfive"])
    
    print(stations)
    
    print(needed_states)
    
    ls = set()
    greedy_algorithm(needed_states,stations,ls)
    print(ls)
    
    list_states = needed_states = set(stations["kone"] | stations["ktwo"] | stations["kthree"] | stations["kfive"])
    print(list_states)