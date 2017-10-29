<<<<<<< HEAD
from flask import Flask, render_template
from jinja2 import Template
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
=======
from flask import Flask, render_template, json
>>>>>>> origin/master
import requests

app = Flask(__name__)

@app.route('/')
def index_html():
    return render_template('index.html')

@app.route('/members', methods = ['GET'])
def members_html():

    response = requests.get("http://data.riksdagen.se/personlista/?iid=&fnamn=&enamn=&f_ar=&kn=&parti=KD&valkrets=&rdlstatus=&org=&utformat=json&termlista=")
    members = response.json()
<<<<<<< HEAD
      
    return render_template("members.html", members = members)
=======



    return render_template('members.html', members=members)
>>>>>>> origin/master

@app.route('/contact')
def contact_html():
    return render_template('contact.html')



if __name__ == '__main__':
    app.run(debug = True)
