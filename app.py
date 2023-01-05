from flask import Flask
from flask import request
import influxdb_client
from influxdb_client.client.write_api import SYNCHRONOUS

app = Flask(__name__)

@app.route("/api/humidity", methods=['POST'])
def humidity():
    if request.method == 'POST':

        frame = request.data
        digits = getDigits(frame)

        if digits == 6 :
            value = getPayloadOne(frame)
            writeInfluxDB("humidity", value)
        elif digits == 10 :    
            value = getPayloadOne(frame)
            writeInfluxDB("humidity", value)
            value = getPayloadTwo(frame)
            writeInfluxDB("humidity", value)

        return request.data

@app.route("/api/temperature", methods=['POST'])
def temperature():
    if request.method == 'POST':

        frame = request.data
        digits = getDigits(frame)

        if digits == 6 :
            value = getPayloadOne(frame)
            writeInfluxDB("temperature", value)
        elif digits == 10 :    
            value = getPayloadOne(frame)
            writeInfluxDB("temperature", value)
            value = getPayloadTwo(frame)
            writeInfluxDB("temperature", value)

        return request.data


def getDigits(frame):
    first = str(frame).split(":")
    second = first[1].split("\"")
    return len(second[1])

def getCorePayload(frame):
    first = str(frame).split(":")
    second = first[1].split("\"")
    return second[1]

def getPayloadOne(frame) :
    code = getCorePayload(frame)
    return int(code[3:6], 16) / 10

def getPayloadTwo(frame) :
    code = getCorePayload(frame)
    return int(code[7:10], 16) / 10

def writeInfluxDB(key, value) :
    bucket = "HD"
    org = "HD"
    token = "cjWOPbA7PCEwKQzvTOlgHy3dsQVJyJ_SNjG0T5Dxc60GWyDtNRyqj9_zWEIicVvxJ3mUWM11O9-wz-tj71eqUw=="
    url="http://localhost:8086"

    client = influxdb_client.InfluxDBClient(
        url=url,
        token=token,
        org=org
    )

    write_api = client.write_api(write_options=SYNCHRONOUS)

    p = influxdb_client.Point("my-measure").field(key, value)
    write_api.write(bucket=bucket, org=org, record=p)
