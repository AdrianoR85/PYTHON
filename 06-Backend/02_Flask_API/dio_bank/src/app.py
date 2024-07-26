from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h1>Hello, World!</h1>"

@app.route("/about", methods=["GET", "POST"])
def about():
    return "<h1>About</h1><p>This is a simple Flask application.</p>"

