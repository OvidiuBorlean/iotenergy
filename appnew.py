#2025-01-08T16:00:00Z
# Importing required functions
from flask import Flask, request, render_template
from datetime import datetime

# Flask constructor
timeBox = ""
now = datetime.now()

iso_date = now.isoformat()
print('ISO DateTime:', iso_date)
app = Flask(__name__)

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
        print("Index electricity - ",data['indexElectricity'])
        print("Index Gas - ", data['indexGas'])
        if data.getlist('switch'):
          print("Yuhuu")
          timeBox = iso_date
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
        app.run()
