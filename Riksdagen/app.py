from flask import Flask, json, render_template
import requests

app = Flask(__name__, static_url_path = "",static_folder= "")

@app.route('/')
def index_html():
   return render_template('index.html')

@app.route('/members', methods=['GET', 'POST'])
def members_html():
    response = requests.get("http://data.riksdagen.se/personlista/?iid=&fnamn=Matilda&enamn=Sundblom&f_ar=1992&kn=kvinna&parti=&valkrets=&rdlstatus=&org=&utformat=json&termlista=parti5")
    return render_template('members.html')

@app.route('/contact')
def contact_html():
   return render_template('contact.html')

if __name__ == '__main__':
   app.run(debug = True)
