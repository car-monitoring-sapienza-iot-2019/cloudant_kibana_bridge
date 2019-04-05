import requests
import json

# Insert here username and password of your elastic server
ESUSERNAME = "YOUR_ELASTIC_USERNAME"
ESPASSWORD = "YOUR_ELASTIC_PWD"

INDEX = "car_monitoring"
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
    data["data"] = params["data"]

    # Create url
    url = "https://"+ESUSERNAME+":"+ESPASSWORD+"@"+HOST+":"+PORT+"/"+INDEX+"/"+TYPE+"/"+ID
    json_data = json.dumps(data)

    # Send data to Kibana
    response = requests.put(url, headers=headers, data=json_data)
    print("RESPONSE:::"+response.text)