import urllib.request
root_url = "http://192.168.43.63"  # ESP's url, ex: https://192.168.102 (Esp serial prints it when connected to wifi)

def sendRequest(url):
	n = urllib.request.urlopen(url) # send request to ESP

def get_data():
	global data

	n = urllib.request.urlopen(root_url).read() # get the raw html data in bytes (sends request and warn our esp8266)
	n = n.decode("utf-8") # convert raw html bytes format to string :3
	
	data = n
# Example usage
while True:
    answer = input(""" To see the level type "level": """)

    if (answer=="level"):
        lol = 0
        while lol<40:
            try:
                get_data()
            except Exception as e:
                continue
            get_data()
            print("Your data which we received: "+data)
            lol = lol+1