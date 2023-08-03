#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None

    best_key = None
    max_score = None

    for key, value in a_dictionary.items():
        if isinstance(value, int):
            if max_score is None or value > max_score:
                max_score = value
                best_key = key

    return best_key
