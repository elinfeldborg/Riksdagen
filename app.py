from flask import Flask, render_template, json
import requests

app = Flask(__name__)

@app.route('/')
def index_html():
    return render_template('index.html')

@app.route('/members', methods = ['GET'])
def members_html():

    response = requests.get("http://data.riksdagen.se/personlista/?iid=&fnamn=&enamn=&f_ar=&kn=&parti=KD&valkrets=&rdlstatus=&org=&utformat=json&termlista=")
    members = response.json()



    return render_template('members.html', members=members)

@app.route('/contact')
def contact_html():
    return render_template('contact.html')



if __name__ == '__main__':
    app.run(debug = True)
