from datetime import timedelta
from floodsystem.datafetcher import fetch_measure_levels
import floodsystem.flood as flood
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.analysis import polyfit
from floodsystem.plot import plot_water_level_with_fit
import matplotlib as plt

def run():
    stations = build_station_list()
    N=5
    update_water_levels(stations)

    list_of_stations_over_tol = flood.stations_highest_rel_level(stations,N)
    for (station,relwaterlevel) in list_of_stations_over_tol:
        dt = 2
        dates, levels = fetch_measure_levels(station.measure_id, dt=timedelta(days=dt))
        p=4
        if dates != []:
            plot_water_level_with_fit(stations,dates,levels,p)
    
    low_values = [station.typical_range[0] for _ in range(len(dates))]
    plt.plot(dates,low_values,label = "Typical low value")

    high_values = [station.typical_range[1] for _ in range(len(dates))]
    plt.plot(dates,high_values,label = "Typical high value")
        

if __name__ == "__main__":
    print("*** Task 2F: CUED Part IB Flood Warning System ***")
    run()