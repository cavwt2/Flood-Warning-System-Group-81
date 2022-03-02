import floodsystem.station as station
from floodsystem.stationdata import build_station_list, update_water_levels
import floodsystem.flood as flood
import datetime
from floodsystem.datafetcher import fetch_measure_levels

'''creating some sample stations to test functions'''
stations = build_station_list()
update_water_levels(stations)
teststation = stations[1]
teststations = stations[1:10]
print(f'Test station current level {teststation.latest_level}')
print(f'Test station typical range {teststation.typical_range}')


'''
This is Test
Station name:     Surfleet Sluice
   id:            http://environment.data.gov.uk/flood-monitoring/id/stations/E2043
   measure id:    http://environment.data.gov.uk/flood-monitoring/id/measures/E2043-level-stage-i-15_min-mASD
   coordinate:    (52.845991, -0.100848)
   town:          Surfleet Seas End
   river:         River Glen
   typical range: (0.15, 0.895)
'''
#Task2B
print(f'Test station relative water level: {teststation.relative_water_level()}')
#Task2C
N=10
list_of_stations_over_tol = flood.stations_highest_rel_level(teststations,N)
for (station,relwaterlevel) in list_of_stations_over_tol:
    #Added a 10 station threshold can remove
    print(f"{station.name} {relwaterlevel}")

#Task2G
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