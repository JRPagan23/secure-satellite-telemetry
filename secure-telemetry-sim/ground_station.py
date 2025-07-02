import json
from crypto_utils import load_key, decrypt_message
import time
import os

def main():
    key = load_key()
    last_mtime = 0

    print("Ground station started. Waiting for telemetry data...")

    while True:
        if os.path.exists("telemetry.enc"):
            mtime = os.path.getmtime("telemetry.enc")
            if mtime != last_mtime:
                last_mtime = mtime
                with open("telemetry.enc", "rb") as f:
                    encrypted_data = f.read()

                try:
                    decrypted_json = decrypt_message(encrypted_data, key)
                    telemetry = json.loads(decrypted_json)
                    print(f"Received telemetry: {telemetry}")
                except Exception as e:
                    print(f"Error decrypting or parsing telemetry: {e}")

        time.sleep(2)  # Check every 2 seconds

if __name__ == "__main__":
    main()

