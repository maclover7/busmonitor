import csv
import datetime
from google.transit import gtfs_realtime_pb2
import requests

feed = gtfs_realtime_pb2.FeedMessage()
response = requests.get("https://truetime.portauthority.org/gtfsrt-bus/vehicles")
feed.ParseFromString(response.content)

vehicles = []

for entity in feed.entity:
    # Ensure that the vehicle is on a trip and not parked in a garage
    if entity.vehicle.trip.trip_id:
        vehicles.append([
                entity.vehicle.timestamp,
                entity.vehicle.trip.trip_id,
                entity.vehicle.trip.route_id,
                entity.vehicle.trip.schedule_relationship,
                entity.vehicle.vehicle.id,
                entity.vehicle.position.latitude,
                entity.vehicle.position.longitude
                ])

now = datetime.datetime.now()
filename = 'data/vehicle-%s-%s-%s.csv' %(now.year, now.month, now.day)
with open(filename, 'a', newline='') as csvfile:
    csv_file = csv.writer(csvfile, lineterminator='\n')
    csv_file.writerows(vehicles)
