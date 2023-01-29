import requests
import time

city="dhaka"

api="https://api.openweathermap.org/data/2.5/weather?q="+ city +"&appid=48a325d31dd00c45913281c77a13d13c"

response = requests.get(api)
data=response.json()
temp =round(data["main"]["temp"] - 273.15)
pressure=data["main"]["pressure"]
humidity=data["main"]["humidity"]
sunrise= time.strftime("%I:%M",time.gmtime(data["sys"]["sunrise"]-21600))
sunset= time.strftime("%I:%M",time.gmtime(data["sys"]["sunset"]-21600))
#print(data)
# print(temp)
# print(pressure)
# print(humidity)
# print(sunrise)
print(sunset)