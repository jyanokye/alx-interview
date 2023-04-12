#!/usr/bin/python3

import sys


def print_stats(total_size, status_counts):
    """
    Print statistics for the given total size,status code counts
    """
    print("Total file size: {}".format(total_size))
    for code in sorted(status_counts.keys()):
        count = status_counts.get(code, 0)
        if count > 0:
            print("{}: {}".format(code, count))

def process_lines():
    """
    Reads lines from standard input,and print statistics
    """
    total_size = 0
    status_counts = {"200": 0, "301": 0, "400": 0, "401": 0, "403": 0, "404": 0, "405": 0, "500": 0}
    line_num = 0
    
    try:
        for line in sys.stdin:
            line = line.strip()
            parts = line.split()
            if len(parts) != 7:
                continue
            ip, _, _, path, status, size = parts
            if not status.isdigit():
                continue
            status_counts[status] = status_counts.get(status, 0) + 1
            if size.isdigit():
                total_size += int(size)
            line_num += 1
            if line_num % 10 == 0:
                print_stats(total_size, status_counts)
    except KeyboardInterrupt:
        pass

    print_stats(total_size, status_counts)

if __name__ == '__main__':
    process_lines()
