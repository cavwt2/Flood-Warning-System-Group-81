# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from .utils import sorted_by_key  # noqa
from haversine import haversine,unit
(x,y) = (52.2053, 0.1218)

def stations_by_distance(stations,p):
   #define the tuple for p
   p = (x,y)
   station_list = []
   for i in stations["items"]:
       q = [i["town"],i["Station name"],haversine(i["coordinate"],p)]
       station_list.append(q)
       return sorted_by_key(q,2)


    