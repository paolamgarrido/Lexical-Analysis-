"""
Author: Paola María Garrido Montes
Date: March 30, 2024
Project: Python's Built-in Module for Regular Expression 
Purpose of the project: Test if the regular expression is correct. 
"""

import re


def test_regex(input_string):
    """
    Test whether the input string conforms to the language
    defined by the regular expression.

    Args:
        input_string (str): The string to be tested.

    Returns:
        None: Prints a message indicating whether the input 
        string is part of the language. 
    """
    pattern = r'(?!.*111|.*222|.*210|.*221100|.*110|.*000)[012]+'
    if re.match(pattern, input_string):
        print("The input string '{}' conforms to the language's syntax.".format(input_string))
    else:
        print("The input string '{}' does not conform to the language's syntax.".format(input_string))


def main():
    """
    Interact with the user and test input strings.

    Args:
        None.

    Returns:
        None: Exits the program when the user inputs 'exit'.
    """
    while True:
        input_string = input("Enter a string composed of 0s, 1s, and 2s: ")
        if input_string.lower() == 'exit':
            break
        test_regex(input_string)


# Runs the main function if the script is executed directly.
if __name__ == "__main__":
    main()