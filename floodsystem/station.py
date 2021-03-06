# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module provides a model for a monitoring station, and tools
for manipulating/modifying station data

"""


class MonitoringStation:
    """This class represents a river level monitoring station"""

    def __init__(self, station_id, measure_id, label, coord, typical_range,
                 river, town):

        self.station_id = station_id
        self.measure_id = measure_id

        # Handle case of erroneous data where data system returns
        # '[label, label]' rather than 'label'
        self.name = label
        if isinstance(label, list):
            self.name = label[0]

        self.coord = coord
        self.typical_range = typical_range
        self.river = river
        self.town = town

        self.latest_level = None

    def __repr__(self):
        d = "Station name:     {}\n".format(self.name)
        d += "   id:            {}\n".format(self.station_id)
        d += "   measure id:    {}\n".format(self.measure_id)
        d += "   coordinate:    {}\n".format(self.coord)
        d += "   town:          {}\n".format(self.town)
        d += "   river:         {}\n".format(self.river)
        d += "   typical range: {}".format(self.typical_range)
        return d

    def typical_range_consistent(self):
        '''returns False if typical range is invalid'''
        if self.typical_range == None:
            return False
        if self.typical_range[0]>self.typical_range[1]:
            return False
        return True

    def relative_water_level(self):
        '''Provides a relative water level compared to typical range, 1.0 if exactly at high value, 0 if at low value'''
        if self.typical_range == None:
            return None
        low_value = self.typical_range[0]
        high_value = self.typical_range[1]

        if self.latest_level == None:
            return None
        '''elif self.latest_level > high_value:
            return None
        elif self.latest_level < low_value:
            return None'''
        return (self.latest_level - low_value)/(high_value - low_value)


def inconsistent_typical_range_stations(stations):
    '''Makes a list of stations with invalid typical range values'''
    list_of_inconsistent = list()
    for station in stations:
        if station.typical_range_consistent() == False:
            list_of_inconsistent.append(station.name)
    list_of_inconsistent.sort()
    return list_of_inconsistent