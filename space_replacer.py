import re

def replace(text):
    modified_text = re.sub(r'\s', '-', text)
    return modified_text

# Get user input
text = input("Enter a string with spaces: ")

# Use the function to replace spaces with hyphens
print("Modified string:",replace(text))
