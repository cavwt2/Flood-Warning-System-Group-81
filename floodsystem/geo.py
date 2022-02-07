# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from .utils import sorted_by_key  # noqa
from .import datafetcher
from .station import MonitoringStation
(x,y) = (52.2053, 0.1218)

def stations_by_distance(stations,p):
   #define the tuple for p
   p = (x,y)
   for e in stations["items"]:
       town = None
       if "town" in e:
           town = e["town"]
        station_name = None
        if "Station name" in e:
            station_name = e["Station name"]