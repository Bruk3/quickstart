import os
import urllib.request
import json

from flask import Flask, render_template

app = Flask(__name__, template_folder='templates')

QUOTE_SERVICE_URL = os.environ.get("QUOTE_SERVICE_URL")

def fetch_quote():
    contents = urllib.request.urlopen(
            "http://{QUOTE_SERVICE_URL}/api/quote".format(
                QUOTE_SERVICE_URL=QUOTE_SERVICE_URL
            )
        ).read()
    return json.loads(contents)


@app.route('/')
def home():
    print("in home")
    return render_template('home.html')

@app.route('/quote')
def get_quote():
    print ("Printing Quote of the Day")
    print ("Fetching quote")
    quote = fetch_quote()
    print("Fetched quote: ", quote)
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


if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0',port=int(os.environ.get('PORT', 8080)))
