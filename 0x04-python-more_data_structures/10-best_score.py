#!/usr/bin/python3
def best_score(a_dictionary):

    if not a_dictionary:
        return (None)
    else:
        for item, value in a_dictionary.items():
            name = item
            data = value
            break

        for keyDict, valueDict in a_dictionary.items():
            if valueDict > data:
                data = valueDict
                name = keyDict
        return (name)
