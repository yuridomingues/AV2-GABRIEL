"""This code will decode a enemy message and print"""

# Limitations: 250 input message, 100 return message

import re

def decoder() -> str:
    """Function to extract segments based on the logic and return the hidden message"""
    hidden_message: str = str(input("Insert the enemy message: "))
    # The message is limited to 250 chars
    if len(hidden_message) > 250:
        return "The message is limited to 250 chars"
    # Ignoring interferences and separating for the logic
    pattern = r"(\d+)([a-zA-Z]*)"
    matches = re.findall(pattern, hidden_message)
    result = ""
    for number, letters in matches:
        if int(number) > 100:
            result += letters
    if len(result) < 100:
        return result
    else:
        return "The message is too long"
print(decoder())
