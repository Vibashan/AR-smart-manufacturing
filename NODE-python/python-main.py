import urllib.request
import socket                
import struct
import numpy as np
from random import randint

root_url = "http://192.168.43.63"
port = 8890 

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

i = 0
while True:
    c, addr = s.accept()      
    print('Got connection from ', addr) 

    while True:
        answer = str(c.recv(1024))
        answer = answer[2:-1]
        if(answer=="LED_OFF"):
            try:
                sendRequest(root_url+"/2")
            except Exception as e:
                continue
            print("LED OFF!!!!")

        if(answer=="LED_ON"):
            try:
                sendRequest(root_url+"/3")
            except Exception as e:
                continue
            print("LED ON!!!!")

        if(answer=="LEVEL_CHECK"):
            i = i+1
            c.send(bytearray("waterLevel:" + str(i), 'ascii'))
        
        if(answer=="LEVEL_RESET"):
            i = 0

        if(answer=="TEMP_PRESS"):
            c.send(bytearray("TEMP:" + str(27), 'ascii'))
            c.send(bytearray("PRESS:" + str(1), 'ascii'))
            #print("TEMP_PRESS")