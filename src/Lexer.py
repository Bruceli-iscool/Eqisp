# A simple lexer
# Breaks down equations like 1 + 1 = 5 into tokens
tokens = [
    'INTEGER', 'OPERATOR'
]

# Function to tokenize input line
def tokenize(inputLine):
    tokens = []  # List to store tokens
    current_token = ""  # String to accumulate characters for a token

    for char in inputLine:
        if char.isdigit():
            current_token += char  # Accumulate digits for an integer token
        elif char in ('+', '-', '*', '/'):
            if current_token:
                tokens.append(('INTEGER', int(current_token)))  # Add integer token if present
                current_token = ""  # Reset current token
            tokens.append(('OPERATOR', char))  # Add operator token
        elif char == ' ':
            if current_token:
                tokens.append(('INTEGER', int(current_token)))  # Add integer token if present
                current_token = ""  # Reset current token

    # Append the last integer token if any
    if current_token:
        tokens.append(('INTEGER', int(current_token)))

    return tokens
# I realized that helper functions just complicate things

