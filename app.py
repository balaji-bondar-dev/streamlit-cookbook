# app.py
import sys
import time

print("Initializing background task...")
time.sleep(1)  # Simulating some work

# Example: Read arguments passed from main script if available
if len(sys.argv) > 1:
    print(f"Received input parameter: {sys.argv[1]}")

print("Task complete! Data successfully updated.")
