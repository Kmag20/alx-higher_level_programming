#!/usr/bin/python3

def best_score(a_dictionary):
    """ Returns a key with the biggest integer value """
    if len(a_dictionary) == 0 or not isinstance(a_dictionary, dict):
        return None
    max_value = max(a_dictionary.values())
    for key, val in a_dictionary.items():
        if val == max_value:
            return (key)
    return None
