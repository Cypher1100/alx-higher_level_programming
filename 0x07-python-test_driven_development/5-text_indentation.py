#!/usr/bin/python3
"""
This module houses a function that  prints a text with 2 new lines after each of these characters: ., ? and :
"""
def text_indentation(text):
    """
    This function prints a text with 2 new lines after each ".", "?", or ":"

    Text must be a string, otherwise raise a TypeError exception with the message "text must be a string"
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    
    counter = 0
    while counter < len(text) and text[counter] == " ":
        counter += 1

    while counter < len(text):
        print(text[counter], end="")
        if text[counter] == "\n" or text[counter] in ".?:":
            if text[counter] in ".?:":
                 print("\n")
            counter += 1
            while count < len(text) and text[count] == " ":
                counter += 1
            continue
        counter += 1
