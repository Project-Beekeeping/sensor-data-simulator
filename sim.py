import requests
import random
import time

# API URL
API_URL = "https://smart-nyuki-django-backend-development.up.railway.app/api/devices/sensor-readings/create/"

# Your authentication token
# TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzUyMDc3OTI3LCJpYXQiOjE3NTIwNzQzMjcsImp0aSI6ImI1MDFmOGVlMmRlMTQ5YjFiYWEyOTZkNmVkNzZmNjMzIiwidXNlcl9pZCI6IjdlYjE1OWY1LWMzYWEtNDRlYS1hMjk1LWViNGY5NjcwNDJiZCJ9.KRNp1M9ElbE23bLrQIKi36vKX3CTKS5qGKDQvaqlueQ"

TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzcyODg3Mzg0LCJpYXQiOjE3NzI4ODM3ODUsImp0aSI6IjVkNDgxNjg1YTk4YzQ2YmY5YTk5MTAyYjE3NDk4MGZlIiwidXNlcl9pZCI6IjdlYjE1OWY1LWMzYWEtNDRlYS1hMjk1LWViNGY5NjcwNDJiZCJ9.xjo77Gi9waMO4gar7G52Vmm1_aPFYneovXQYPYjmqxQ"

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
        response = requests.post(API_URL, json=data, headers=HEADERS)
        if response.status_code == 201:
            print(f"[✓] Sent data for device {serial}")
        else:
            print(
                f"[✗] Failed for device {serial}: {response.status_code} - {response.text}")


if __name__ == "__main__":
    while True:
        send_data()
        time.sleep(1200)  # Send data every 3 minutes
