<<<<<<< HEAD
from flask import Flask, json, render_template
import requests
=======
from flask import Flask, render_template, request, json
>>>>>>> 725e1c166cdda6726db15989954c7b3ea126df65

app = Flask(__name__)

@app.route('/')
def index_html():
    return render_template('index.html')

@app.route('/members', methods=['GET', 'POST'])
def members_html():
<<<<<<< HEAD
    response = requests.get("http://data.riksdagen.se/personlista/?iid=&fnamn=Matilda&enamn=Sundblom&f_ar=1992&kn=kvinna&parti=&valkrets=&rdlstatus=&org=&utformat=json&termlista=parti5")
=======

    response = request.args.get('http://data.riksdagen.se/personlista/?iid=&fnamn=Elin&enamn=Feldborg+Nielsen&f_ar=1994&kn=&parti=&valkrets=&rdlstatus=&org=&utformat=html&termlista=parti')
    ledarmoter = response.json()
    print(ledarmoter)

>>>>>>> 725e1c166cdda6726db15989954c7b3ea126df65
    return render_template('members.html')

@app.route('/contact')
def contact_html():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug = True)
