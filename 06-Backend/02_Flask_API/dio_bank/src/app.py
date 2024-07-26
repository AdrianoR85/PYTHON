from flask import Flask
app = Flask(__name__)

@app.route("/<user>")
def Home(user):
    return f"<h1>Welcome, {user}</h1>"

@app.route("/about")
def about():
    return "<h1>About</h1><p>This is a simple Flask application.</p>"