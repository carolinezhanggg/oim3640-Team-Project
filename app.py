"""
application that can find current weather and recent events using Flask
"""

from flask import Flask, render_template, request
from helper import get_temp, get_events

app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def show_weather():
    if request.method == "POST":
        city_name = request.form['city']
        country_code = request.form['countrycode']
        state_code = request.form['statecode']
        number = request.form.get('How many number of events would you want to be listed?',type = int)
        temperature = get_temp(city_name,country_code)
        events = get_events(city_name,state_code,number)
        return render_template('weather-result.html', city=city_name, temp=temperature, events=events)
    else:
        return render_template("weather.html")



if __name__=="__main__":
    app.run(debug=True)

