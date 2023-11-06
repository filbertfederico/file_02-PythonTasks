import sys

class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

# Global variables for the token and index
token = ""
index = 0

def get_next_token(input_str):
    global token, index
    if index < len(input_str):
        token = input_str[index]
        index += 1
    else:
        token = ""
    return token

def parse_expression(input_str):
    get_next_token(input_str)
    node = parse_term(input_str)
    while token in ('+', '-'):
        operator = token
        get_next_token(input_str)
        right = parse_term(input_str)
        node = Node(operator, node, right)
    return node

def parse_term(input_str):
    node = parse_factor(input_str)
    while token in ('*', '/', '%', '^'):
        operator = token
        get_next_token(input_str)
        right = parse_factor(input_str)
        node = Node(operator, node, right)
    return node

def parse_factor(input_str):
    global token
    if token == '(':
        get_next_token(input_str)
        node = parse_expression(input_str)
        if token == ')':
            get_next_token(input_str)
        else:
            error("Mismatched parentheses")
    elif token.isdigit():
        temp = ''
        while token.isdigit() and index < len(input_str):
            temp += token
            get_next_token(input_str)
        if token.isdigit():
            temp += token
            get_next_token(input_str)
        node = Node(temp)
    else:
        error("Invalid token: " + token)
    return node

def evaluate(node):
    if node.value.isdigit():
        return int(node.value)
    left = evaluate(node.left)
    right = evaluate(node.right)
    if node.value == '+':
        return left + right
    elif node.value == '-':
        return left - right
    elif node.value == '*':
        return left * right
    elif node.value == '/':
        if right == 0:
            error("Division by zero")
        return left / right
    elif node.value == '%':
        if right == 0:
            error("Modulo by zero")
        return left % right
    elif node.value == '^':
        return left ** right

def error(message="Error"):
    print(message)
    sys.exit(1)

def display_parse_tree(node, level=0):
    if node:
        print("  " * level + node.value)
        display_parse_tree(node.left, level + 1)
        display_parse_tree(node.right, level + 1)

def main():
    global token, index
    print("A RECURSIVE-DESCENT CALCULATOR WITH PARSE TREE AND ERROR DETECTION.")
    print("\t the valid operations are +, - , *, /, %, ^")
    print("Enter the calculation string, e.g. '34 + 6 * 56', '2^2/2%1'")
    input_str = input()  # Load input as a string
    input_str = input_str.replace(" ", "")  # Remove spaces from the input string
    index = 0

    try:
        parse_tree = parse_expression(input_str)
        print("Parse Tree:")
        display_parse_tree(parse_tree)

        result = evaluate(parse_tree)
        print("Result =", result)
    except Exception as e:
        error(str(e))

if __name__ == "__main__":
    main()