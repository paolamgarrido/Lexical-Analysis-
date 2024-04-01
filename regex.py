"""
Author: Paola María Garrido Montes 
Date: March 30, 2024
Project: Regular Expression Python Test
Purpose of the project: Lexical analysis parser using 
a regular expression, which can detect the chosen language.
"""

def test_regex(input_string):
    """
    Checks if the input string is part of the language. 

    Args:
        input_string (str): The string to be tested.

    Returns:
        bool: True if the input string follows the language rules.
        bool: False if the input string includes a prohibited sequence, the string 
        was empty or it didn't contain only 0s, 1s and 2s. 
    """

    if len(input_string) == 0:
        return False
    
    for char in input_string:
        if char not in ['0', '1', '2']:
            return False
    
    if ('111' in input_string or
        '222' in input_string or
        '210' in input_string or
        '221100' in input_string or
        '110' in input_string or
        '000' in input_string):
        return False
    
    return True

def main():
    """
    Interact with the user and test input strings.

    Args:
        None.

    Returns:
        None: Exits the program when the user inputs 'exit'. Prints a message 
        indicating whether the input string conforms to the language's syntax.
    """
    while True:
        input_string = input("Enter a string (composed of 0s, 1s, and 2s): ")
        if input_string.lower() == 'exit':
            break
        if test_regex(input_string):
            print("The input string '{}' conforms to the language's syntax.".format(input_string))
        else:
            print("The input string '{}' does not conform to the language's syntax.".format(input_string))

# Runs the main function if the script is executed directly.
if __name__ == "__main__":
    main()