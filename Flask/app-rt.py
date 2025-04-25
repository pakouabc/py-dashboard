import datetime
from collections import deque

from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

# Almacena los últimos 10 datos
sensor_data = deque(maxlen=10)


@app.route("/")
def index():
    return render_template("index.html")


# API para enviar datos desde el sensor (simulado)
@app.route("/api/sensor", methods=["POST"])
def receive_sensor_data():
    data = request.get_json()
    timestamp = datetime.datetime.now().strftime("%H:%M:%S")
    value = data.get("value")
    if value is not None:
        sensor_data.append({"timestamp": timestamp, "value": value})
        return jsonify({"status": "ok"}), 200
    return jsonify({"error": "Missing 'value'"}), 400


# API para entregar los datos más recientes al frontend
@app.route("/api/data")
def get_data():
    return jsonify(list(sensor_data))


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
