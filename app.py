from flask import Flask, render_template, url_for, request, flash
import sqlite3
import requests, json

app = Flask(__name__)
app.secret_key = 'This_is_very_secret'

@app.route('/', methods = ['GET', 'POST'])
def main():
    print(request.method)
    if request.method == 'POST':
        api_key = "73c61ac872812494ce058fca44377691"
        base_url = "http://api.openweathermap.org/data/2.5/weather?"
        city_name = request.form['City']
        complete_url = base_url + "appid=" + api_key + "&q=" + city_name
        response = requests.get(complete_url)

        x = response.json()

        if x["cod"] != "404":

            y = x["main"]

            current_temperature = y["temp"]
            current_pressure = y["pressure"]
            current_humidity = y["humidity"]

            z = x["weather"]

            weather_description = z[0]["description"]

        
            flash(" Temperature (in kelvin unit) = " +
                            str(current_temperature) +
                "\n atmospheric pressure (in hPa unit) = " +
                            str(current_pressure) +
                "\n humidity (in percentage) = " +
                            str(current_humidity) +
                "\n description = " +
                            str(weather_description))
            
            message = [current_temperature, current_pressure, current_humidity, weather_description]
    
        else:
            print(" City Not Found ")
        
    return render_template('home.html', message = message)

if __name__ == '__main__': 
    app.run(debug = True)