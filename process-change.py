import requests
import json

# Insert here username and password of your elastic server
ESUSERNAME = "YOUR_ELASTIC_USERNAME"
ESPASSWORD = "YOUR_ELASTIC_PWD"

INDEX = "car_monitoring_index"
TYPE = "_doc"
PORT = "9243"
HOST = "KIBANA_SERVER_URL"

headers = {
    'Content-Type': 'application/json',
}


def main(params):

    # Load Id of the modified item
    ID = params["_id"]

    # Load data
    data = {}
    data["date"] = params["data"]["date"]
    data["location"] = {}
    data["location"]["lat"] = params["data"]["location"]["lat"]
    data["location"]["lon"] = params["data"]["location"]["lon"]
    data["throttle"] = params["data"]["throttle"]
    data["rpm"] = params["data"]["rpm"]
    data["massAirFlow"] = params["data"]["massAirFlow"]
    data["speed"] = params["data"]["speed"]
    data["engineTemperature"] = params["data"]["engineTemperature"]

    # Create url
    url = "https://"+ESUSERNAME+":"+ESPASSWORD+"@"+HOST+":"+PORT+"/"+INDEX+"/"+TYPE+"/"+ID
    json_data = json.dumps(data)

    # Send data to Kibana
    response = requests.put(url, headers=headers, data=json_data)
    print("RESPONSE:::"+response.text)