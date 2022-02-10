import floodsystem.geo as geo
from floodsystem.stationdata import build_station_list

def run():
    stations = build_station_list()
    print(geo.rivers_by_station_number(stations,9))


if __name__ == "__main__":
    print("*** Task 1E: CUED Part IA Flood Warning System ***")
    run()

