This script demonstrates the use of 2 APIs which help us see if by inputing our latitude and longitude coordinates, we can or can not spot the International Space Station in the sky.

http://api.open-notify.org/iss-now.json -> a GET request to this link returns a json response which is then parsed for the latitude and longitude of the ISS.


https://api.sunrise-sunset.org/json -> a GET request to this link return a json response which is then parsed for the time of sunrise and sunset based on your location.

