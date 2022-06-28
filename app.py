import os
import urllib.request

from flask import Flask, render_template

app = Flask(__name__, template_folder='templates')

QUOTE_SERVICE_URL = os.environ.get("QUOTE_SERVICE_URL")
PORT = os.environ.get("QUOTE_SERVICE_PORT")

def fetch_quote():
    contents = urllib.request.urlopen(
            "http://{QUOTE_SERVICE_URL}:{PORT}/api/quote".format(
                QUOTE_SERVICE_URL=QUOTE_SERVICE_URL,
                PORT=PORT
            )
        ).read()


@app.route('/')
def hello_world():
    return render_template('home.html')

@app.route('/quote')
def get_quote():
    print ("Printing Quote of the Day")
    # quote = fetch_quote()
    return render_template(
            'home.html', 
            quote="People say nothing is impossible, but I do nothing every day.",
            by="Winnie the Pooh"
        )


if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0',port=int(os.environ.get('PORT', 8082)))
