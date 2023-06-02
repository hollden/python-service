from flask import Flask
from datetime import datetime
import socket


app = Flask(__name__)


@app.route("/", methods=['GET'])
def root():
    response = "Hostname: " + socket.gethostname() + '\n' + "Current date: " + \
        str(datetime.today().strftime('%Y-%m-%d %H:%M:%S')) + '\n'
    return response


@app.route("/healthz", methods=['GET'])
def health_check():
    return "OK"


if __name__ == "__main__":
    app.run(host="0.0.0.0")
