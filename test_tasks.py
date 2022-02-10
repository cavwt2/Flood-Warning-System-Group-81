from floodsystem.geo import stations_by_distance
from floodsystem.geo import stations_within_radius
from floodsystem.geo import rivers_with_station
from floodsystem.geo import stations_by_river
from floodsystem.geo import rivers_by_station_number
from floodsystem.station import inconsistent_typical_range_stations
from floodsystem.stationdata import build_station_list


def test_stations_by_distance():
    """Test building list of stations by distance"""
    stations = build_station_list()
    (p) = (52.2053, 0.1218)
    station_distances = stations_by_distance(stations,p)
    assert len(station_distances) > 0

def test_stations_within_radius():
    """Test building list of stations by radius"""
    stations = build_station_list()
    centre = (52.2053, 0.1218)
    r = 10
    station_list =[station.name for (station,radius) in stations_within_radius(stations, centre, r)]
    assert len(station_list) > 0

def test_rivers_with_station():
    """Test building list of rivers with station"""
    stations = build_station_list()
    station_list = rivers_with_station(stations)
    assert len(station_list) > 0

def test_stations_by_river():
    """Test building list of stations by river"""
    stations = build_station_list()
    station_list = stations_by_river(stations)
    assert len(station_list) > 0

def test_rivers_by_station_number():
    """Test building list of stations by distance"""
    stations = build_station_list()
    station_list = rivers_by_station_number(stations,9)
    assert len(station_list) > 0

def test_inconsistent_typical_range_stations():
    stations = build_station_list()
    """Test if the function returns a list of inconsistent stations"""
    station_list = inconsistent_typical_range_stations(stations)
    assert type(station_list) == list