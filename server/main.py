import time
import network
import requests
import socket
import json
import numpy as np
import pymongo
from pymongo import MongoClient
from decimal import Decimal
from django.http import HttpResponse

def json2dict(response):
        str = json.dumps(response)
        dict = json.loads(str)
        return dict

#establish a connection to MongoDB
client = MongoClient()
db = client.helmetDB
website = db.website

#init_data = {
#    'trips':'0',
#    'distance':'0',
#    'calories':'0'
#}
#result = website.insert_one(init_data)

#Server socket
HOST = '172.31.85.24'
PORT = 80
s = socket.socket()
s.bind((HOST, PORT))
s.listen(1)


while True:
    client_socket, client_addr = s.accept()
    print('client connected from', client_addr)
    original_recv = client_socket.recv(1024)
    find_recv = original_recv.decode("utf-8")
    if find_recv.find("trip") != -1:
        last_data = website.find_one()
        last_trip = Decimal(last_data['trips'])
        resp = str(last_trip)
    elif find_recv.find("distance") != -1:
        last_data = website.find_one()
        last_distance = Decimal(last_data['distance'])
        resp = str(last_distance)
    elif find_recv.find("calories") != -1:
        last_data = website.find_one()
        last_calories = Decimal(last_data['calories'])
        resp = str(last_calories)
    else:
        recv = Decimal(original_recv)
        print(recv)
        last_data = website.find_one()
        print(last_data)
        website.remove()
        last_trip = Decimal(last_data['trips'])
        last_distance = Decimal(last_data['distance'])
        last_calories = Decimal(last_data['calories'])
        new_trip = last_trip + 1
        user_data = {
        'trips':str(last_trip+1),
        'distance':str(last_distance+recv),
        'calories':str(last_calories+recv*32)
        }
        result = website.insert_one(user_data)
        resp = "HTTP/1.1 200 OK"
    client_socket.send(resp)
    client_socket.close()