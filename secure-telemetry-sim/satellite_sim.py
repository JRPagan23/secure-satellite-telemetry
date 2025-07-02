import json
import time
import random
from crypto_utils import load_key, encrypt_message

def simulate_telemetry():
    # Generate fake telemetry data
    data = {
        "temperature_celsius": round(random.uniform(-40, 85), 2),
        "orientation_deg": {
            "pitch": round(random.uniform(-180, 180), 2),
            "yaw": round(random.uniform(-180, 180), 2),
            "roll": round(random.uniform(-180, 180), 2),
        },
        "battery_percent": round(random.uniform(0, 100), 2),
        "timestamp": time.time()
    }
    return data

def main():
    key = load_key()

    while True:
        telemetry = simulate_telemetry()
        telemetry_json = json.dumps(telemetry)
        encrypted = encrypt_message(telemetry_json, key)

        # Save encrypted telemetry to a file
        with open("telemetry.enc", "wb") as f:
            f.write(encrypted)

        print(f"Encrypted telemetry saved: {telemetry}")
        time.sleep(5)  # Wait 5 seconds before next reading

if __name__ == "__main__":
    main()

