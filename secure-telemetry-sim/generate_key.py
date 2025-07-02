import sys
import os

# Add current directory to sys.path explicitly
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

import crypto_utils

crypto_utils.generate_key()
print("Key generated!")
import sys
sys.path.insert(0, '.')

import crypto_utils

crypto_utils.generate_key()
print("Key generated!")
import crypto_utils

crypto_utils.generate_key()
print("Key generated!")

