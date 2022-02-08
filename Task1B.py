from turtle import distance
from floodsystem.geo import stations_by_distance
from floodsystem.stationdata import build_station_list

def run():
    """Requirements for Task 1B"""
    stations = build_station_list()
    (p) = (52.2053, 0.1218)
    station_distances = stations_by_distance(stations,p)

    close =[(station.name, station.town, distance) for (station, distance) in station_distances[:10]]
    far = [(station.name, station.town, distance) for (station, distance) in station_distances[-10:]]
    print("10 closest stations")
    print(close)
    print("10 furthest stations")
    print(far)

if __name__ == "__main__":
    print("*** Task 1A: CUED Part IB Flood Warning System ***")
    run()