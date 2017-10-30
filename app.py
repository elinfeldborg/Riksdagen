from flask import Flask, render_template
import requests
from flask import request
import json
from jinja2 import Template
import twitter


app = Flask(__name__)

@app.route('/')
def index_html():
    return render_template('index.html')

@app.route('/members')
def members_html():

    response = requests.get("http://data.riksdagen.se/personlista/?iid=&fnamn=&enamn=&f_ar=&kn=&parti=M&valkrets=&rdlstatus=&org=&utformat=json&termlista=")
    members = response.json()

    return render_template("members.html", members = members)


@app.route('/twitter', methods=['GET', 'POST'])
def twitter_html():

    api = twitter.Api(consumer_key='wfLFiJsqho3SCe4x0VZLWRpa2',
    consumer_secret='3yVVNXMhSL79sH23IUkPwOQztpdQ7lSWAWzQf2Ted9mnF935B9',
    access_token_key='368883718-jGwQoh8dYpW2IPMsmCexlYbLq2hc0cCxThaekzKm',
    access_token_secret='EuXP5ktiFkP0Rh1aEOuidLYmZk6RzoqSvoJeTbzqYdQe3')

    statuses = api.GetUserTimeline(screen_name='HultbergJohan')
    print([s.text for s in statuses])

    return render_template("twitter.html", statuses = statuses)

@app.route('/contact')
def contact_html():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug = True)
