import urllib.request
import socket                
import struct
import numpy as np
from random import randint
import cv2

root_url = "http://192.168.43.63"
port = 8889 

s = socket.socket()                         
s.bind(('', port))         
s.listen(5)      
print ("socket binded to " , port) 

def sendRequest(url):
	n = urllib.request.urlopen(url) 

def get_data():
	global data
	n = urllib.request.urlopen(root_url).read()
	n = n.decode("utf-8") 
	data = n

while True:
    c, addr = s.accept()      
    print('Got connection from ', addr) 

    while True:
        try:
            answer = c.recv(6000000)
            nparr = np.fromstring(answer, np.uint8)
            img_np = cv2.imdecode(np.frombuffer(answer, np.uint8), -1)

            cv2.imshow('lol',img_np)
            k = cv2.waitKey(30) & 0xFF
            if k == 27:
                break

            print(type(img_np), img_np.shape)
        except Exception as e:
            continue