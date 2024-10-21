#!/usr/bin/python3
import sys
import signal

# Initialize variables to store metrics
total_size = 0
status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0

# Helper function to print the current metrics
def print_metrics():
    global total_size, status_codes
    print(f"File size: {total_size}")
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print(f"{code}: {status_codes[code]}")

# Function to handle KeyboardInterrupt (CTRL + C)
def signal_handler(sig, frame):
    print_metrics()
    sys.exit(0)

# Set up the signal handler for CTRL + C
signal.signal(signal.SIGINT, signal_handler)

try:
    # Read from stdin line by line
    for line in sys.stdin:
        line_count += 1
        try:
            # Split the line and extract the necessary parts
            parts = line.split()
            if len(parts) < 7:
                continue  # Skip if line doesn't have enough parts

            # Extract the status code and file size from the log
            status_code = int(parts[-2])
            file_size = int(parts[-1])

            # Update metrics
            total_size += file_size
            if status_code in status_codes:
                status_codes[status_code] += 1

        except (ValueError, IndexError):
            continue  # Skip lines that can't be parsed

        # Every 10 lines, print the current metrics
        if line_count % 10 == 0:
            print_metrics()

except KeyboardInterrupt:
    # Handle KeyboardInterrupt gracefully
    print_metrics()
    sys.exit(0)
