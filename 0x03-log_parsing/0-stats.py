#!/usr/bin/python3
"""
Log Parsing
"""

import sys


def parse_logs():
    """defines logic to parse logs
    """
    count = 1
    file_size = 0
    status_dict = {200: 0,
                   301: 0,
                   400: 0,
                   401: 0,
                   403: 0,
                   404: 0,
                   405: 0,
                   500: 0}
    try:
        for line in sys.stdin:
            logs = line.split(" ")
            try:
                if int(logs[-2]) in status_dict.keys():
                    file_size += int(logs[-1])
                    status_dict[int(logs[-2])] += 1
                if count % 10 == 0 and count != 0:
                    print_output(status_dict, file_size)
                count += 1
            except ValueError:
                continue
        print_output(status_dict, file_size)
    except KeyboardInterrupt:
        print_output(status_dict, file_size)
        raise


def print_output(status_dict, file_size):
    """print output log stats

    Args:
        status_dict (dict): status codes with count
        file_size (int): accummulated file size
    """
    print("File size: {}".format(file_size))
    for k, v in status_dict.items():
        if v != 0:
            print("{}: {}".format(k, v))


if __name__ == '__main__':
    parse_logs()
