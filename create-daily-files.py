import csv
import datetime

tomorrow = datetime.datetime.now() + datetime.timedelta(days=1)

filename = 'data/stoptime-%s-%s-%s.csv' %(tomorrow.year, tomorrow.month, tomorrow.day)
with open(filename, 'a', newline='') as csvfile:
    csv_file = csv.writer(csvfile, lineterminator='\n')
    csv_file.writerow(["timestamp", "trip_id", "route_id", "schedule_relationship", "vehicle_id", "stop_id", "arrival", "departure"])

filename = 'data/vehicle-%s-%s-%s.csv' %(tomorrow.year, tomorrow.month, tomorrow.day)
with open(filename, 'a', newline='') as csvfile:
    csv_file = csv.writer(csvfile, lineterminator='\n')
    csv_file.writerow(["timestamp", "trip_id", "route_id", "schedule_relationship", "vehicle_id", "latitude", "longitude"])
