import os
import urllib.request
import json

from flask import Flask, render_template

app = Flask(__name__, template_folder='templates')

QUOTE_SERVICE_URL = os.environ.get("QUOTE_SERVICE_URL")
FORECAST_SERVICE_URL = os.environ.get("FORECAST_SERVICE_URL")

def fetch_quote():
    contents = urllib.request.urlopen(
            "http://{QUOTE_SERVICE_URL}/api/quote".format(
                QUOTE_SERVICE_URL=QUOTE_SERVICE_URL
            )
        ).read()
    return json.loads(contents)

def fetch_weather(day):
    url =  "http://{FORECAST_SERVICE_URL}/api/{day}".format(
                FORECAST_SERVICE_URL=FORECAST_SERVICE_URL, 
                day=day
    )
    print("url::start")
    print(url)
    print("url::done")

    contents = urllib.request.urlopen(url).read()

    return json.loads(contents)



@app.route('/')
def home():
    return render_template('home.html')

@app.route('/quote')
def get_quote():
    quote = fetch_quote()
    return render_template(
        'home.html',
        quote=quote["quote"],
        by=quote["by"]
    )
    return render_template(
            'home.html', 
            quote="People say nothing is impossible, but I do nothing every day.",
            by="Winnie the Pooh"
        )

@app.route('/weather/today')
def get_weather_today():
    weather = fetch_weather("today")
    return render_template(
        'home.html', 
        day="today",
        weather=weather
    )

@app.route('/weather/tomorrow')
def get_weather_tomorrow():
    weather = fetch_weather("tomorrow")
    return render_template(
        'home.html', 
        day="tomorrow",
        weather=weather
    )

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0',port=int(os.environ.get('PORT', 8084)))
