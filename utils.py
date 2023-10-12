def is_valid_number(string):
    valid = False
    try:
        float(string)
        valid = True
    except ValueError:
        valid = False

    return valid
