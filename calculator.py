def get_number(prompt):
    while True:
        value = input(prompt).strip()
        if value.lower() in {'q', 'quit', 'exit'}:
            raise KeyboardInterrupt
        try:
            return float(value)
        except ValueError:
            print('Invalid number. Please enter a valid numeric value or type q to quit.')


def get_operator():
    valid = {
        '+': 'addition',
        '-': 'subtraction',
        '*': 'multiplication',
        '/': 'division',
    }
    while True:
        op = input('Enter operation (+, -, *, /) or q to quit: ').strip()
        if op.lower() in {'q', 'quit', 'exit'}:
            raise KeyboardInterrupt
        if op in valid:
            return op
        print('Invalid operator. Choose +, -, *, or /.')


def calculate(a, b, operator):
    if operator == '+':
        return a + b
    if operator == '-':
        return a - b
    if operator == '*':
        return a * b
    if operator == '/':
        if b == 0:
            raise ZeroDivisionError('Division by zero is not allowed.')
        return a / b
    raise ValueError(f'Unsupported operator: {operator}')


def main():
    print('Simple CLI Calculator')
    print("Type 'q', 'quit', or 'exit' at any prompt to stop.")

    while True:
        try:
            first = get_number('Enter the first number: ')
            op = get_operator()
            second = get_number('Enter the second number: ')
            result = calculate(first, second, op)
            print(f'Result: {first} {op} {second} = {result}')
            print()
        except ZeroDivisionError as error:
            print(f'Error: {error}')
            print()
        except KeyboardInterrupt:
            print('\nGoodbye!')
            break
        except Exception as error:
            print(f'Error: {error}')
            print()


if __name__ == '__main__':
    main()
