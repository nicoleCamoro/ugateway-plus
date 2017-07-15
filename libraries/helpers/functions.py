
def convert_key_val_pairs(keyval_array):

    result = {}
    for pair in keyval_array:
        result[pair[0]] = pair[1]
    return result