#!/usr/bin/python3
"""Method to determine if all boxes can be opened"""


def canUnlockAll(boxes):
    """Method to determine if all boxes can be opened

    args:
        boxes: list of lists

    """
    keys = [0]
    for key in keys:
        for key in boxes[key]:
            if key not in keys and key < len(boxes):
                keys.append(key)
    if len(keys) == len(boxes):
        return True
    return False
