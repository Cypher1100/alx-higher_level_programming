#!/usr/bin/python3
def multiple_returns(sentence):
    senlength = len(sentence)

    if (senlength == 0):
        strtuple = (senlength, None)
    else:
        new_tuple = (senlength, sentence[0])

    return (strtuple)
