import requests
import random
import time

while True:
    requests.post(
        "http://localhost:5000/api/sensor", json={"value": random.randint(10, 90)}
    )
    time.sleep(2)
