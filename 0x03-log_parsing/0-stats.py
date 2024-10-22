#!/usr/bin/python3

"""
Log parsing script that reads logs from standard input, 
calculates file size, and counts occurrences of specific 
HTTP status codes.
"""

import sys

def print_stats(stats: dict, file_size: int) -> None:
    """
    Function to print the statistics: total file size 
    and counts for each HTTP status code that occurred.
    
    Args:
    stats (dict): Dictionary containing the counts of status codes.
    file_size (int): The total file size.
    """
    print(f"File size: {file_size}")
    for code, count in sorted(stats.items()):
        if count:
            print(f"{code}: {count}")

if __name__ == "__main__":
    # Initialize variables for tracking total file size and line count
    file_size = 0
    line_count = 0

    # Define the HTTP status codes we want to track
    status_codes = ["200", "301", "400", "401", "403", "404", "405", "500"]
    
    # Create a dictionary to store counts of each status code
    stats = {code: 0 for code in status_codes}

    try:
        # Read from standard input, line by line
        for line in sys.stdin:
            line_count += 1  # Track how many lines we’ve processed
            
            # Split the line into parts (assuming space-separated data)
            data = line.split()
            
            # Try to extract the status code and file size from the line
            try:
                # Status code is expected to be the second-to-last element
                status_code = data[-2]
                if status_code in stats:
                    stats[status_code] += 1  # Increment the count for the code
            except (IndexError, ValueError):
                # Catch index or conversion errors and skip this line
                pass

            try:
                # File size is expected to be the last element
                file_size += int(data[-1])
            except (IndexError, ValueError):
                # Catch errors in file size conversion
                pass
            
            # Print stats every 10 lines
            if line_count % 10 == 0:
                print_stats(stats, file_size)
        
        # After reading all lines, print the final stats
        print_stats(stats, file_size)

    except KeyboardInterrupt:
        # If the script is interrupted (Ctrl+C), print the stats before exiting
        print_stats(stats, file_size)
        raise
