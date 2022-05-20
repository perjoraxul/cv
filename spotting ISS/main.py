import requests
from datetime import datetime
import time

def iss_position() :
	'''return latitude and longitude coordinates of the ISS'''
	#use the API endpoin to get the data by making a request to that specific URL
	response = requests.get(url='http://api.open-notify.org/iss-now.json')

	#raise exception if status != 200
	response.raise_for_status()

	#get the desired data
	data_latitude = response.json()['iss_position']['latitude']
	data_longitude = response.json()['iss_position']['longitude']

	# print(response)
	# print(f'longitude : {data_longitude}, latitude : {data_latitude}')
	
	return float(data_latitude),float(data_longitude)

def sunrise_sunset(lat,longi) :
	MY_LAT = lat
	MY_LONG = longi

	parameters = {
		"lat" : MY_LAT,
		"long" : MY_LONG,
		#format to unix time
		'formatted' : 0
	}

	#same get request, but we pass some parameters in the URL as dictionary of key:value strings
	response = requests.get(url="https://api.sunrise-sunset.org/json",params=parameters)
	response.raise_for_status()
	data = response.json()
	#accessing the data we want - the hour of sunrise and sunset in my location
	sunrise_hour = data['results']['sunrise'].split('T')[1].split(':')[0]
	sunset_hour = data['results']['sunset'].split('T')[1].split(':')[0]
	# print(sunrise_hour, sunset_hour)
	return float(MY_LAT),float(MY_LONG),int(sunrise_hour),int(sunset_hour)


lat = input("Input my latitude ")

longi = input("Input my longitude ")

while True :
	hour_now = int(str(datetime.now()).split(" ")[1].split(":")[0]) 
	sunrise_sunset_params = sunrise_sunset(lat,longi)
	iss_position_params = iss_position()

	print(sunrise_sunset_params)
	if ((sunrise_sunset_params[3] < hour_now <= 24) or (0 <= hour_now < sunrise_sunset_params[2])) and ((sunrise_sunset_params[1] - 5 <= iss_position_params[1] <= sunrise_sunset_params[1] - 5) and (sunrise_sunset_params[0] - 5 <= iss_position_params[0] <= sunrise_sunset_params[0] - 5)):
		print("Go and check the ISS")

	else :
		print("Impossible to see.")

	time.sleep(3)