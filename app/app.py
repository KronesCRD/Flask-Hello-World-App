#!/bin/python3

from flask import Flask

# Kommentar für Test
app = Flask(__name__)

@app.route("/")
def index():
    return """
    <h1>Python Flask in Docker!</h1>
    <p>A sample web-app for running Flask inside Docker.</p>
    """

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
