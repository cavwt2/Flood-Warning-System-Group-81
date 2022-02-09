# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from .utils import sorted_by_key  # noqa
from haversine import haversine, Unit

def stations_by_distance(stations,p):
   """lists stations by distance from p"""
   station_list = []
   for i in stations:
       #creates a list of tuples each containing town name, station name and distance from p
       q =(i,haversine(i.coord,p, unit=Unit.KILOMETERS))
       station_list.append(q)
       #sorts the list by distance from p
   return sorted_by_key(station_list,1)

def stations_within_radius(stations, centre, r):
    """lists stations within radius r of centre x"""
    station_radius = []
    for i in stations:
    #creates a list of tuples each containing town name, station name and distance from the centre
        radius = haversine(i.coord,centre, unit=Unit.KILOMETERS)
        q =(i,radius)
        if radius < r:
            station_radius.append(q)
    return station_radius

def rivers_with_station(stations):
    '''Creates a list of river names'''
    river_names = set()
    for station in stations:
        if station.river != None:
            river_names.add(station.river)
    return river_names

def stations_by_river(stations):
    '''Creates a dictionary which maps river name to station name'''
    river_dict = dict()
    for station in stations:
        if station.river != None:
            if station.river in river_dict:
                river_dict[station.river].append(station.name)
                river_dict[station.river].sort()
            else:
                river_dict[station.river] = [station.name]
    return river_dict
