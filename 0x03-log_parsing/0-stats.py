#!/usr/bin/env python3
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
    status_dict = {}

    for line in sys.stdin:
        logs = line.split(" ")
        if int(logs[7]) not in status_dict.keys():
            status_dict[int(logs[7])] = 0
        file_size += int(logs[-1])
        status_dict[int(logs[7])] += 1
        if count == 10:
            print_output(status_dict, file_size)
            count = 0
        count += 1


def print_output(status_dict, file_size):
    """print output log stats

    Args:
        status_dict (dict): status codes with count
        file_size (int): accummulated file size
    """
    print("File size: {}".format(file_size))
    od = OrderedDict(sorted(status_dict.items()))
    for k, v in od.items():
        print("{}: {}".format(k, v))


if __name__ == '__main__':
    try:
        parse_logs()
    except KeyboardInterrupt:
        print_output(status_dict, file_size)
