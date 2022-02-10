from re import S
import floodsystem.geo as geo
from floodsystem.stationdata import build_station_list

def run():
    stations = build_station_list()
    mydict = geo.stations_by_river(stations)

    list_of_rivers = list(geo.rivers_with_station(stations))
    list_of_rivers.sort()
    print(f'Number of rivers = {len(list_of_rivers)}')
    print(f'First 10 rivers = {list_of_rivers[:10]}')
    
    print(f"Stations of River Aire: {mydict['River Aire']}")
    print(f"Stations of River Cam: {mydict['River Cam']}")
    print(f"Stations of River Thames: {mydict['River Thames']}")


if __name__ == "__main__":
    print("*** Task 1D: CUED Part IA Flood Warning System ***")
    run()
