import floodsystem.station as station
from floodsystem.stationdata import build_station_list

'''creating some sample stations to test functions'''
stations = build_station_list()
print(stations[2])



'''
This is TestSt
Station name:     Surfleet Sluice
   id:            http://environment.data.gov.uk/flood-monitoring/id/stations/E2043
   measure id:    http://environment.data.gov.uk/flood-monitoring/id/measures/E2043-level-stage-i-15_min-mASD
   coordinate:    (52.845991, -0.100848)
   town:          Surfleet Seas End
   river:         River Glen
   typical range: (0.15, 0.895)
'''
TestStation1 = stations[1]


