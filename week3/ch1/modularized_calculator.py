#! /usr/bin/python3

def read_number(line, index):
    number = 0
    while index < len(line) and line[index].isdigit():
        number = number * 10 + int(line[index])
        index += 1
    if index < len(line) and line[index] == '.':
        index += 1
        decimal = 0.1
        while index < len(line) and line[index].isdigit():
            number += int(line[index]) * decimal
            decimal /= 10
            index += 1
    token = {'type': 'NUMBER', 'number': number}
    return token, index


def read_plus(line, index):
    token = {'type': 'PLUS'}
    return token, index + 1


def read_minus(line, index):
    token = {'type': 'MINUS'}
    return token, index + 1

def read_multiply(line, index):
    token = {'type': 'MULTIPLY'}
    return token, index + 1

def read_divide(line, index):
    token = {'type': 'DIVIDE'}
    return token, index + 1

def calculate_mul_div(tokens):
    index = 0
    while index < len(tokens):
        if tokens[index]['type'] == 'NUMBER':
            if index > 0 and tokens[index - 1]['type'] == 'MULTIPLY':
                tokens[index - 2]['number'] *= tokens[index]['number']
                tokens.pop(index)
                tokens.pop(index - 1)
                index -= 1
            elif index > 0 and tokens[index - 1]['type'] == 'DIVIDE':
                # Check for divisionn by zero
                if tokens[index]['number'] == 0:
                    print("Error: Division by zero")
                    exit(1)
                tokens[index - 2]['number'] /= tokens[index]['number']
                tokens.pop(index)
                tokens.pop(index - 1)
                index -= 1
            else:
                index += 1
        else:
            index += 1
    return tokens

def calculate_add_sub(tokens):
    # print(f'tokens = {tokens}')
    index = 0
    answer = 0
    while index < len(tokens):
        if tokens[index]['type'] == 'NUMBER':
            if index > 0 and tokens[index - 1]['type'] == 'PLUS':
                answer += tokens[index]['number']
            elif index > 0 and tokens[index - 1]['type'] == 'MINUS':
                answer -= tokens[index]['number']
            else:
                print(f'Invalid syntax')
                exit(1)
        index += 1
    return answer


def tokenize(line):
    tokens = []
    index = 0
    while index < len(line):
        # print(f"idx={line[index]}")
        if line[index].isdigit():
            (token, index) = read_number(line, index)
        elif line[index] == '+':
            (token, index) = read_plus(line, index)
        elif line[index] == '-':
            (token, index) = read_minus(line, index)
        elif line[index] == '*':
            print("reading multiply")
            (token, index) = read_multiply(line, index)
        elif line[index] == '/':
            print("reading divide")
            (token, index) = read_divide(line, index)
        else:
            print('Invalid character found: ' + line[index])
            exit(1)
        tokens.append(token)
    return tokens


def evaluate(tokens):
    answer = 0
    tokens.insert(0, {'type': 'PLUS'}) # Insert a dummy '+' token

    # Handle multiplication and division first
    tokens = calculate_mul_div(tokens)

    # Handle addition and subtraction
    answer = calculate_add_sub(tokens)

    return answer


def test(line):
    tokens = tokenize(line)
    actual_answer = evaluate(tokens)
    expected_answer = eval(line)
    if abs(actual_answer - expected_answer) < 1e-8:
        print("PASS! (%s = %f)" % (line, expected_answer))
    else:
        print("FAIL! (%s should be %f but was %f)" % (line, expected_answer, actual_answer))


# Add more tests to this function :)
def run_test():
    print("==== Test started! ====")
    # addition and subtraction
    test("1+2")
    test("1.0+2.1-3")
    test("12345678+87654321")

    # multiplication
    test("1+2*3")
    test("1.2+2*3")
    test("1+2.3*4")
    test("1+2*3.4")
    test("0*4")
    test("12345678*87654321")

    # division
    test("1+2/3")
    test("1.2+2/3")
    test("1+2.3/4")
    test("1+2/3.4")
    test("0/4")
    test("12345678/87654321")

    # mixed operations
    test("1+2*3/4")
    test("1/2*3+4")


    print("==== Test finished! ====\n")

run_test()

while True:
    print('> ', end="")
    line = input()
    tokens = tokenize(line)
    answer = evaluate(tokens)
    print("answer = %f\n" % answer)
