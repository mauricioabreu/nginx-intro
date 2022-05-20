from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def index():
    return "<p>Index page!</p>"

@app.route("/hello")
def hello():
    name = request.args.get("name", "nobody")
    return f"<p>Hello, {name}</p>"