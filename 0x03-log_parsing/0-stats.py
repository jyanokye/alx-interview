#!/usr/bin/python3

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

    print("Total file size: {}".format(total_size))
    for code, count in sorted(code_count.items()):
        if count != 0:
            print("{}: {}".format(code, count))


total_size = 0
code = 0
counter = 0
code_count = {"200": 0,
              "301": 0,
              "400": 0,
              "401": 0,
              "403": 0,
              "404": 0,
              "405": 0,
              "500": 0}

try:
    for line in sys.stdin:
        parsed_line = line.split()  # split line into fields
        parsed_line = parsed_line[::-1]  # reverse the order of fields

        if len(parsed_line) > 2:
            counter += 1

            if counter <= 10:
                total_size += int(parsed_line[0])  # add file size to total
                code = parsed_line[1]  # get status code

                if (code in code_count.keys()):
                    code_count[code] += 1  # increment count for status code

            if (counter == 10):
                print_stats(code_count, total_size)  # print stats for batch
                counter = 0

finally:
    print_stats(code_count, total_size)  # print final stats for last batch
