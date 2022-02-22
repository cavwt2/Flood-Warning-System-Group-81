import floodsystem.flood as flood
from floodsystem.stationdata import build_station_list, update_water_levels

def run():
    stations = build_station_list()
    N=10
    update_water_levels(stations)

    list_of_stations_over_tol = flood.stations_highest_rel_level(stations,N)
    for (station,relwaterlevel) in list_of_stations_over_tol:
        #Added a 10 station threshold can remove
        print(f"{station.name} {relwaterlevel}")


if __name__ == "__main__":
    print("*** Task 2C: CUED Part IB Flood Warning System ***")
    run()