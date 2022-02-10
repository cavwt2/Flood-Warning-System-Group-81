from floodsystem.geo import stations_by_distance
from floodsystem.geo import stations_within_radius
from floodsystem.geo import rivers_with_station
from floodsystem.geo import stations_by_river
from floodsystem.geo import rivers_by_station_number
from floodsystem.station import inconsistent_typical_range_stations


def test_stations_by_distance():
    """Test building list of stations by distance"""
    station_list = stations_by_distance()
    assert len(station_list) > 0

def test_stations_within_radius():
    """Test building list of stations by radius"""
    station_list = stations_within_radius()
    assert len(station_list) > 0

def test_rivers_with_station():
    """Test building list of rivers with station"""
    station_list = rivers_with_station()
    assert len(station_list) > 0

def test_stations_by_river():
    """Test building list of stations by river"""
    station_list = stations_by_river()
    assert len(station_list) > 0

def test_rivers_by_station_number():
    """Test building list of stations by distance"""
    station_list = rivers_by_station_number()
    assert len(station_list) > 0

def test_inconsistent_typical_range_stations():
    """Test if the function returns a list of inconsistent stations"""
    station_list = inconsistent_typical_range_stations()
    assert type(station_list) == list