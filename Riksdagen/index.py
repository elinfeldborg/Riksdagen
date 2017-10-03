from flask import flask, render_template

app = Flask(__name__)

@app.route("/")
def index.html():
    return render_template("index.html")

@app.route("/members")
def member.html():
    return render_template("members.html")


if __name__ == "__main__":
    app.run(debug=True)
