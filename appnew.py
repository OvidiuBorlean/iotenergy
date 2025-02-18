#2025-01-08T16:00:00Z
# Importing required functions
from flask import Flask, request, render_template
from datetime import datetime
from influxdb import InfluxDBClient
# Flask constructor
timeBox = ""
now = datetime.now()

iso_date = now.isoformat()
print('ISO DateTime:', iso_date)
app = Flask(__name__)


def iotenergy(value, time):
        print("----> ", time, value)
        json_body = [
        {
        "measurement": "energy",
        "tags": {
            "house": "Mosnita Veche",
            "kind": "Electric"
        },
        "time": time,
        "fields": {
            "value": value
        }
    }

]
        client = InfluxDBClient('localhost', 8086, 'root', 'root', 'energy')

        #client.create_database('energy')
        client.write_points(json_body)


def iotgas(value, time):
        print("---> ", time, value)
        json_body = [
        {
        "measurement": "energy",
        "tags": {
            "house": "Mosnita Veche",
            "kind": "Gas"
        },
        "time": time,
        "fields": {
            "value": value
        }
    }

]

        client = InfluxDBClient('localhost', 8086, 'root', 'root', 'energy')

#client.create_database('gas')
        #print(type(json_body))
        client.write_points(json_body)
# Root endpoint
@app.route('/', methods=['GET'])
def index():
        ## Display the HTML form template
        return render_template('index.html')


# `read-form` endpoint
@app.route('/read-form', methods=['POST'])
def read_form():
        # Get the form data as Python ImmutableDict datatype
        data = request.form
        elec = data['indexElectricity'].isdigit()
        gs = data['indexGas'].isdigit()
        #print(elec.isdigit())
        #print(gs.isdigit())
        if elec == False:
          return "Electricity Index Not Number"
        if gs == False:
          return ("Gas Index not Number")
        print("Index electricity - ",data['indexElectricity'])
        print("Index Gas - ", data['indexGas'])
        if data.getlist('switch'):
          print("Yuhuu")
          timeBox = iso_date
          iotenergy(int(data['indexElectricity']), timeBox)
          iotgas(int(data['indexGas']), timeBox)
        else:
          timeBox = data['indexTime']
        print("Time Now: - ", timeBox)
        #if switch.validate():
        ## Return the extracted information
        #if data['switch'] == "on":
        #  print("On")
        return "Ok"

# Main Driver Function
if __name__ == '__main__':
        # Run the application on the local development server
        app.run(host='0.0.0.0')
