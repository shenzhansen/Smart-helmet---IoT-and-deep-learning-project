import subprocess
import time
import socket
import datetime
import json
import sys
import requests
from decimal import Decimal

def json2dict(response):
    str = json.dumps(response)
    dict = json.loads(str)
    return dict

def get_time():
    print(datetime.datetime.now().time())
    c_time = datetime.datetime.now().time()
    c_time = str(c_time)
    c_time_h = c_time[:c_time.find(":")]
    c_time_m = c_time[c_time.find(":") + 1:c_time.find(":") + 3]
    c_time_ann = "The time now is " + c_time_h + " " + c_time_m
    print(c_time_ann)
    return c_time_ann

def get_weather():
    geo_url = 'https://www.googleapis.com/geolocation/v1/geolocate?key=AIzaSyCYUtkV41me0u1Hk$
    geo_header = {'content-type': 'application/json'}
    geo_resp = requests.post(geo_url, headers=geo_header)
    lat = str(json2dict(geo_resp.json())['location'] ['lat'])
    lng = str(json2dict(geo_resp.json())['location'] ['lng'])

    wea_url = 'http://api.openweathermap.org/data/2.5/weather?lat=' + lat + '&lon=' + lng + $
    wea_post_fields = {'foo': 'bar'}
    wea_all_resp = requests.post(wea_url, data=json.dumps(wea_post_fields))

    temp = json2dict(wea_all_resp.json())['main'] ['temp']
    temp = str(temp)+' Degrees Fahrenheit'

    wea_json = json2dict(wea_all_resp.json())['weather'][0]
    wea = json2dict(wea_json)['description']
    wea = str(wea).capitalize()

    weather_ann = "The weather now is " + wea + " and " + temp
    print(weather_ann)
    return weather_ann

def get_direction(p):
    destination = p

    dir_url = 'https://maps.googleapis.com/maps/api/directions/json?origin=Low+Memorial+Libr$
    dir_resp = requests.post(dir_url)

    routes_json = json2dict(dir_resp.json())['routes'][0]
    legs_json = json2dict(routes_json)['legs'][0]

    distance_json = json2dict(legs_json)['distance']['text']
    distance = str(distance_json)
    distance = distance.replace("mi", "")

    duration_json = json2dict(legs_json)['duration']['text']
    duration = str(duration_json)
    duration = duration.replace("mins", "")

    steps_json = json2dict(legs_json)['steps'][0]
    html_instructions_json = json2dict(steps_json)['html_instructions']
    html_instructions = str(html_instructions_json)
    html_instructions = html_instructions.replace("<b>", "")
    html_instructions = html_instructions.replace("</b>", "")

    navigation_ann = "The distance is " + distance + "miles " + " The riding time is about "$
    print(navigation_ann)
    return navigation_ann

def get_distance(p):
    destination = p

    dir_url = 'https://maps.googleapis.com/maps/api/directions/json?origin=Low+Memorial+Libr$
    dir_resp = requests.post(dir_url)

    routes_json = json2dict(dir_resp.json())['routes'][0]
    legs_json = json2dict(routes_json)['legs'][0]

    distance_json = json2dict(legs_json)['distance']['text']
    distance = str(distance_json)
    distance = distance.replace("mi", "")

    return distance

def get_duration(p):
    destination = p

    dir_url = 'https://maps.googleapis.com/maps/api/directions/json?origin=Low+Memorial+Libr$
    dir_resp = requests.post(dir_url)

    routes_json = json2dict(dir_resp.json())['routes'][0]
    legs_json = json2dict(routes_json)['legs'][0]

    duration_json = json2dict(legs_json)['duration']['text']
    duration = str(duration_json)
    duration = duration.replace("mins", "")

    return distance

def sent_sever(p):
    PORT = 80
    HOST = '52.91.78.255'
    ADDR = (HOST, PORT)
    ss = socket.socket()

    ss.connect(ADDR)
    p = p.encode("utf-8")
    ss.send(p)

    ss.close()

#set up a server
HOST = '129.236.236.197'
PORT = 1500

s = socket.socket()
s.bind((HOST, PORT))
s.listen(1)

while True:
    client_socket, client_addr = s.accept()
    data = client_socket.recv(5120)
    client_socket.send(b'HTTP/1.1 200 OK')
    client_socket.close

    #extract destination
    data = data.decode("utf-8")
    destination = data[data.find("destination="):data.find(" HTTP")]
    destination = destination.replace("%2B", "+")
    print(destination)

    if data.find("start") != -1:
        #get time
        c_time_ann = get_time()

        #get weather and tempeture
        weather_ann = get_weather()

        #announce time and weather
        announce = c_time_ann + " " + weather_ann
        announce = announce.encode("utf-8")
        arg1 = announce
        print(arg1)
        subprocess.Popen(['/home/pi/tts.sh %s' %(arg1)], shell = True)
        time.sleep(8)

        #announce navigation
        navigation_ann = get_direction(destination)
        announce = navigation_ann
        announce = announce.encode("utf-8")
        arg1 = announce
        print(arg1)
        subprocess.Popen(['/home/pi/tts.sh %s' %(arg1)], shell = True)

    elif data.find("end") != -1:
        #get_distance

        distance = get_distance(destination)
        duration = get_duration(destination)
        calories = str(Decimal(distance) * 32)

        #announce finished
        announce = "You have reached your destination You rode " + distance + "miles for " + duration + "minutes and consumed" + calories + " calories Thank you"
        announce = announce.encode("utf-8")
        arg1 = announce
        print(arg1)
        subprocess.Popen(['/home/pi/tts.sh %s' %(arg1)], shell = True)

        #sent to AWS server
        sent_sever(distance)