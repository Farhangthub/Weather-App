from flask import Flask,render_template,request
import requests
import time


app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def hello_world():
    if request.method == "POST":
        city = request.form["city"]
        api="https://api.openweathermap.org/data/2.5/weather?q="+ city +"&appid=48a325d31dd00c45913281c77a13d13c"
        response = requests.get(api)
        data=response.json()
        temp =round(data["main"]["temp"] - 273.15)
        pressure=data["main"]["pressure"]
        humidity=data["main"]["humidity"]
        sunrise= time.strftime("%I:%M",time.gmtime(data["sys"]["sunrise"]-21600))
        sunset= time.strftime("%I:%M",time.gmtime(data["sys"]["sunset"]-21600))
        return render_template("index.html",city=city,temp=temp,pressure=pressure,humidity=humidity,sunrise=sunrise,sunset=sunset)
    return render_template("index.html")
    
if __name__ == "__main__":   
    app.run(debug=True)
