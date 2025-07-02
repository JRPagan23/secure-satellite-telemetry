# secure-satellite-telemetry
Simulates secure satellite telemetry by generating and encrypting data on a satellite simulator and decrypting it on a ground station using Python and symmetric cryptography. Demonstrates real-time secure communication for aerospace cybersecurity learning.
# Secure Satellite Telemetry Simulator

## Overview
This project simulates the generation and secure transmission of satellite telemetry data using Python. It demonstrates how to protect sensitive space system data by encrypting telemetry on a simulated satellite and decrypting it on a ground station.

## Features
- Generates realistic telemetry data (temperature, orientation, battery).
- Encrypts data using symmetric encryption (Fernet from the cryptography library).
- Saves encrypted telemetry to a file, simulating transmission.
- Ground station app decrypts and displays live telemetry data.
- Demonstrates key management and secure communication principles.

## How to Run
1. Generate the encryption key:
   ```bash
   python3 generate_key.py
