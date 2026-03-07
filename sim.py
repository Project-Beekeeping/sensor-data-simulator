import os
import random
import time

import requests

API_URL = os.getenv(
    "API_URL",
    "https://smart-nyuki-django-backend-development.up.railway.app/api/devices/sensor-readings/create/",
)
TOKEN = os.getenv("API_TOKEN", "")
SEND_INTERVAL_SECONDS = int(os.getenv("SEND_INTERVAL_SECONDS", "120"))

# Headers with Bearer token
HEADERS = {
    "Authorization": f"Bearer {TOKEN}",
    "Content-Type": "application/json"
}

# Device serials to simulate
DEVICE_SERIALS = ["23dgjkjoiu8erhg", "23dgjkjoiu8",
                  "00", "53", "52", "43", "33", "31", "22", "2", "1"]


def generate_sensor_data(device_serial):
    return {
        "device_serial": device_serial,
        "temperature": round(random.uniform(30.0, 40.0), 2),
        "humidity": round(random.uniform(50.0, 70.0), 2),
        "weight": round(random.uniform(10.0, 20.0), 2),
        "sound_level": random.randint(50, 90),
        "battery_level": random.randint(50, 100),
        "status_code": random.choice([0, 1])
    }


def send_data():
    for serial in DEVICE_SERIALS:
        data = generate_sensor_data(serial)
        try:
            response = requests.post(
                API_URL, json=data, headers=HEADERS, timeout=15)
            if response.status_code == 201:
                print(f"[OK] Sent data for device {serial}")
            else:
                print(
                    f"[FAIL] Device {serial}: {response.status_code} - {response.text}"
                )
        except requests.RequestException as exc:
            print(f"[ERROR] Device {serial}: {exc}")


if __name__ == "__main__":
    if not TOKEN:
        raise RuntimeError("Missing API_TOKEN environment variable")

    while True:
        send_data()
        time.sleep(SEND_INTERVAL_SECONDS)
