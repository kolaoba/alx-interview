#!/usr/bin/python3
"""
Log Parsing
"""

import sys
from collections import OrderedDict


def parse_logs():
    """defines logic to parse logs
    """
    count = 0
    global file_size
    global status_dict
    file_size = 0
    status_dict = {200: 0,
                   301: 0,
                   400: 0,
                   401: 0,
                   403: 0,
                   404: 0,
                   405: 0,
                   500: 0}

    for line in sys.stdin:
        logs = line.split(" ")
        if int(logs[-2]) in status_dict.keys() and len(logs) == 9:
            file_size += int(logs[-1])
            status_dict[int(logs[-2])] += 1
        if count % 10 == 0 and count != 0:
            print_output(status_dict, file_size)
        count += 1


def print_output(status_dict, file_size):
    """print output log stats

    Args:
        status_dict (dict): status codes with count
        file_size (int): accummulated file size
    """
    print("File size: {}".format(file_size))
    for k, v in status_dict.items():
        if v > 0:
            print("{}: {}".format(k, v))


try:
    parse_logs()
except KeyboardInterrupt:
    print_output(status_dict, file_size)
