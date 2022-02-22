'''A submodule which should be made... Is this a submodule??'''
from .utils import sorted_by_key

def stations_level_over_threshold(stations,tol):
    '''creates list of tuples with stations with level over a thereshold'''
    stations_over_tol = []
    for station in stations:
        if station.typical_range_consistent() and (station.relative_water_level() != None) and (station.relative_water_level() > tol):
            stations_over_tol.append((station, station.relative_water_level()))

    return sorted_by_key(stations_over_tol,1,reverse=True)

def stations_highest_rel_level(stations,N):
    stations_over_tol = []
    tol = 0.8
    for station in stations:
        if station.typical_range_consistent() and (station.relative_water_level() != None) and (station.relative_water_level() > tol):
            stations_over_tol.append((station, station.relative_water_level()))

    return sorted_by_key(stations_over_tol,1,reverse=True)[:N]