import floodsystem.flood as flood
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.datafetcher import fetch_measure_levels
import datetime
def run():
    stations = build_station_list()
    N=20
    update_water_levels(stations)

    list_of_stations_over_tol = flood.stations_highest_rel_level(stations,N)

    for (station,relwaterlevel) in list_of_stations_over_tol:
        print(f"{station.town} {relwaterlevel}")
        if relwaterlevel < 0.8:
            print('Low Risk')
        elif relwaterlevel>= 10:
            print('Error in level data')
        elif relwaterlevel>= 3:
            print('High Risk')
        elif relwaterlevel >= 2:
            print('Severe Risk')
        elif relwaterlevel >= 0.8:
            print('Moderate Risk')

        dt = 2
        dates, levels = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=dt))

        if levels == []:
            print('No level data')
        elif levels[0]>levels[-1]:
            print('Water level rising')
        elif levels[0]<levels[-1]:
            print('Water level falling')
        elif levels[0]==levels[-1]:
            print('Water level stable')


if __name__ == "__main__":
    print("*** Task 2G: CUED Part IB Flood Warning System ***")
    run()