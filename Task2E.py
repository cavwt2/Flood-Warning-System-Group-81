from datetime import datetime, timedelta
from floodsystem.datafetcher import fetch_measure_levels
import floodsystem.flood as flood
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.plot import plot_water_levels

def run():
    stations = build_station_list()
    N=5
    update_water_levels(stations)

    list_of_stations_over_tol = flood.stations_highest_rel_level(stations,N)
    for (station,relwaterlevel) in list_of_stations_over_tol:
        dt = 10
        dates, levels = fetch_measure_levels(
            station.measure_id, dt=timedelta(days=dt))
        if dates != []:
            plot_water_levels(station,dates,levels)
        

if __name__ == "__main__":
    print("*** Task 2E: CUED Part IB Flood Warning System ***")
    run()