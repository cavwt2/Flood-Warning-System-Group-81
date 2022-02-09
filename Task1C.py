from turtle import distance
from floodsystem.geo import stations_within_radius
from floodsystem.geo import stations_by_distance
from floodsystem.stationdata import build_station_list
from floodsystem.station import MonitoringStation

"""10 closest stations to Cambridge City Centre"""
def run():
    """Requirements for Task 1C"""
    stations = build_station_list()
    centre = (52.2053, 0.1218)
    r = 10
    list_of_stations =[station.name for (station,radius) in stations_within_radius(stations, centre, r)]
    sortedstations = list_of_stations.sort()
    print("Stations within a radius of 10km")
    print(sortedstations)

if __name__ == "__main__":
    print("*** Task 1A: CUED Part IC Flood Warning System ***")
    run()