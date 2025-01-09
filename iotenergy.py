from influxdb import InfluxDBClient

json_body = [
{
        "measurement": "energy",
        "tags": {
            "house": "My House",
            "kind": "Electricity"
        },
        "time": "2025-01-08T16:00:00Z",
        "fields": {
            "value": 12089
        }
    }

]

client = InfluxDBClient('localhost', 8086, 'root', 'root', 'energy')

client.create_database('energy')
client.write_points(json_body)
print("Done")
