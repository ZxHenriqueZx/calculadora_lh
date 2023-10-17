import re

NUM_OR_DOT_REGEX = re.compile(r'^[0-9.]$')

def is_num_or_dot(string):
    return bool(NUM_OR_DOT_REGEX.search(string))

def is_valid_number(string):
    valid = False
    try:
        float(string)
        valid = True
    except ValueError:
        valid = False

    return valid

def is_empyt(value):
    return len(value) == 0

