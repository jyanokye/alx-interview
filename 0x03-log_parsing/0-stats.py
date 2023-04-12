#!/usr/bin/env python3

import sys

def print_stats(code_count, total_size):
    """
    Prints statistics about HTTP status codes and total file size.
    Args:
        code_count: a dictionary of status codes and their counts
        total_size: the total size of the file
    Returns:
        None
    """
    print(f"File size: {total_size}")
    for key, value in sorted(code_count.items()):
        if value != 0:
            print(f"{key}: {value}")


# Initialize variables
total_size = 0
code_count = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0,
}
count_lines = 0

# Read lines from input and process them
for line in sys.stdin:
    # Split line into fields
    fields = line.split()
    # Reverse fields
    fields.reverse()

    # If there are at least three fields
    if len(fields) >= 3:
        # Increment line counter
        count_lines += 1

        # If the line counter is 10, print statistics and reset counter
        if count_lines == 10:
            print_stats(code_count, total_size)
            count_lines = 0

        # Parse file size and status code
        file_size = int(fields[0])
        status_code = fields[1]

        # Increment status code count
        if status_code in code_count:
            code_count[status_code] += 1

        # Increment total file size
        total_size += file_size

# Print final statistics
if count_lines != 0:
    print_stats(code_count, total_size)
