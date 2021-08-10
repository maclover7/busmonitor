import csv
from google.transit import gtfs_realtime_pb2
import requests

feed = gtfs_realtime_pb2.FeedMessage()
response = requests.get("https://truetime.portauthority.org/gtfsrt-bus/trips")
feed.ParseFromString(response.content)

stop_times = []

for entity in feed.entity:
    for stop_time_update in entity.trip_update.stop_time_update:
        stop_times.append([
                entity.trip_update.timestamp,
                entity.trip_update.trip.trip_id,
                entity.trip_update.trip.route_id,
                entity.trip_update.trip.schedule_relationship,
                entity.trip_update.vehicle.id,
                stop_time_update.stop_id,
                stop_time_update.arrival.time,
                stop_time_update.departure.time
                ])

with open('bus-stoptime.csv', 'a', newline='') as csvfile:
    csv_file = csv.writer(csvfile, lineterminator='\n')
    csv_file.writerows(stop_times)
