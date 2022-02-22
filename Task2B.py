import floodsystem.flood as flood
from floodsystem.stationdata import build_station_list, update_water_levels

def run():
    stations = build_station_list()
    update_water_levels(stations)
    tol = 0.8

    list_of_stations_over_tol = flood.stations_level_over_threshold(stations,tol)
    for (station,relwaterlevel) in list_of_stations_over_tol[:10]:
        print(f"{station.name} {relwaterlevel}")


if __name__ == "__main__":
    print("*** Task 2B: CUED Part IB Flood Warning System ***")
    run()