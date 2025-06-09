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

def read_open_bracket(line, index):
    token = {'type': 'PAREN_BEGIN'}
    return token, index + 1

def read_close_bracket(line, index):
    token = {'type': 'PAREN_END'}
    return token, index + 1

def read_abs(line, index):
    token = {'type': 'ABS'}
    return token, index + 3

def read_int(line, index):
    token = {'type': 'INT'}
    return token, index + 3

def read_float(line, index):
    token = {'type': 'FLOAT'}
    return token, index + 5


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
            elif index > 0 and tokens[index - 1]['type'] == 'ABS' or 'INT' or 'FLOAT':
                pass
            else:
                print(f'One before: {tokens[index - 1]}')
                print(f'Invalid syntax at index {index}: {tokens[index]}')
                # print(f'Invalid syntax')
                exit(1)
        index += 1

    # print(f'add_sub answer = {answer}')
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
            # print("reading multiply")
            (token, index) = read_multiply(line, index)
        elif line[index] == '/':
            # print("reading divide")
            (token, index) = read_divide(line, index)
        elif line[index] == '(':
            (token, index) = read_open_bracket(line, index)
        elif line[index] == ')':
            (token, index) = read_close_bracket(line, index)
        elif line[index] == 'a' and line[index+1] == 'b' and line[index+2] == 's': # abs
            (token, index) = read_abs(line, index)
        elif line[index] == 'i' and line[index+1] == 'n' and line[index+2] == 't': # int
            (token, index) = read_int(line, index)
        elif line[index] == 'f' and line[index+2] == 'o' and line[index+4] == 't': # float
            (token, index) = read_float(line, index)
        else:
            print('Invalid character found: ' + line[index])
            exit(1)
        tokens.append(token)
    return tokens

def calculate_tokens(tokens):
    if tokens[0]['type'] != 'PLUS':
        tokens.insert(0, {'type': 'PLUS'}) # Insert a dummy '+' token

    # Handle multiplication and division first
    tokens = calculate_mul_div(tokens)
    # Handle addition and subtraction
    answer = calculate_add_sub(tokens)

    # print(f'cal_answer = {answer}')

    return answer



def evaluate(tokens):
    answer = 0
    tokens.insert(0, {'type': 'PLUS'}) # Insert a dummy '+' token

    while True:
        if not any(token['type'] == 'PAREN_BEGIN' for token in tokens) and not any(token['type'] == 'PAREN_END' for token in tokens):
            break
        index = 0
        while index < len(tokens):
            tmp_tokens = []
            if tokens[index]['type'] == 'PAREN_END':
                seen_index = index # ここまでは読んだ、という意味でindexを記録(この計算が終わったら、この続きから見れば良い)
                index -= 1
                while tokens[index]['type'] != 'PAREN_BEGIN':
                    tmp_tokens.insert(0, tokens[index])
                    index -= 1
                # print(f"tmp_tokens = {tmp_tokens}")

                tmp_answer = calculate_tokens(tmp_tokens)
                has_prefix = False
                if tokens[index - 1]['type'] == 'ABS':
                    tmp_answer = abs(tmp_answer)
                    has_prefix = True
                elif tokens[index - 1]['type'] == 'INT':
                    tmp_answer = int(tmp_answer)
                    has_prefix = True
                elif tokens[index - 1]['type'] == 'FLOAT':
                    tmp_answer = float(tmp_answer)
                    has_prefix = True

                # renew the tokens list
                if has_prefix:
                    # Replace 'PAREN_BEGIN' with the calculated value
                    tokens[index - 1]['type'] = 'NUMBER'
                    tokens[index - 1]['number'] = tmp_answer

                    # Remove the parentheses part
                    tokens = tokens[:index] + tokens[seen_index + 1:]
                else:
                    # Replace 'ABS' or 'INT' or 'FLOAT' with the calculated value
                    tokens[index]['type'] = 'NUMBER'
                    tokens[index]['number'] = tmp_answer

                    # Remove the parentheses part
                    tokens = tokens[:index + 1] + tokens[seen_index + 1:]
            index += 1

    # print(f"tokens = {tokens}")
    answer = calculate_tokens(tokens=tokens)

    return answer


def test(line):
    tokens = tokenize(line)
    # print(f"tokens1 = {tokens}")
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

    # parentheses
    test("1+(2+3)")
    test("1+(2*3)")
    test("(1+2)*3")
    test("(1+2)/3")

    # mixed operations
    test("1+2*3/4")
    test("1/2*3+4")
    test("1+(2*3)/(4+5)*8")
    test("(1+(2+3)+4)/3")

    # abs, int, float
    test("abs(-3)")
    test("int(3.5)")
    test("float(3)")
    test("abs(-3)+int(3.5)*float(3)")
    test("3+(abs(-3)+int(3.4)/float(3))*2")


    print("==== Test finished! ====\n")

run_test()

while True:
    print('> ', end="")
    line = input()
    tokens = tokenize(line)
    answer = evaluate(tokens)
    print("answer = %f\n" % answer)
