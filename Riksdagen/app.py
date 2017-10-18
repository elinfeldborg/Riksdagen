from flask import Flask, render_template, request, json

app = Flask(__name__)

@app.route('/')
def index_html():
    return render_template('index.html')

@app.route('/members', methods=['GET', 'POST'])
def members_html():

    response = request.args.get('http://data.riksdagen.se/personlista/?iid=&fnamn=Elin&enamn=Feldborg+Nielsen&f_ar=1994&kn=&parti=&valkrets=&rdlstatus=&org=&utformat=html&termlista=parti')
    ledarmoter = response.json()
    print(ledarmoter)

    return render_template('members.html')

@app.route('/contact')
def contact_html():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug = True)
