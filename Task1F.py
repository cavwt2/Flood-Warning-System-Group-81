import floodsystem.station as station
from floodsystem.stationdata import build_station_list

def run():
    stations = build_station_list()
    print(station.inconsistent_typical_range_stations(stations))


if __name__ == "__main__":
    print("*** Task 1A: CUED Part IA Flood Warning System ***")
    run()
