from flask import Flask, jsonify
import datetime
import socket   

port_number = 9000
app = Flask(__name__)
@app.route("/")
def index():
    return "$$$ Welcom to slave api ! Try /health or /time $$$"

@app.route("/health")
def health_check():
    response = {
        "status": "ok",
        "service": "Slave API"
    }
    return jsonify(response)

@app.route("/time")
def get_time():
    now = datetime.datetime.now()
    response = {
            "current_time": now.strftime("%Y-%m-%d[%H:%M:%S]")
    }
    return jsonify(response)
@app.route("/hostname")
def get_hostname():
    hostname = socket.gethostname()
    return jsonify({"hostname": hostname})

if  __name__ == "__main__":
    app.run(host = "0.0.0.0" , port = port_number)
