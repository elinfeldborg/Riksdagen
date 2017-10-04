from flask import Flask, render_template

app = Flask(__name__, static_url_path = "",static_folder= "")

@app.route('/')
def index_html():
   return render_template('index.html')

@app.route('/members')
def members_html():
   return render_template('members.html')

@app.route('/contact')
def contact_html():
   return render_template('contact.html')

if __name__ == '__main__':
   app.run(debug = True)
