from flask import Flask, render_template
from os import environ as env

hostname = env["HOSTNAME"]

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', hostname=hostname)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)