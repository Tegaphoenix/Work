import sys

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero is not allowed."
    return x / y

def greet(name):
    return f"Hello, {name}!"

def main():
    if len(sys.argv) < 2:
        print("Usage: python script.py <command> [arguments]")
        print("Commands:")
        print("  add <x> <y> - Adds x and y")
        print("  subtract <x> <y> - Subtracts y from x")
        print("  multiply <x> <y> - Multiplies x and y")
        print("  divide <x> <y> - Divides x by y")
        print("  greet <name> - Greets the user by name")
        sys.exit(1)

    command = sys.argv[1]

    if command == 'add':
        if len(sys.argv) != 4:
            print("Usage: python script.py add <x> <y>")
            sys.exit(1)
        x = float(sys.argv[2])
        y = float(sys.argv[3])
        print(f"Result: {add(x, y)}")

    elif command == 'subtract':
        if len(sys.argv) != 4:
            print("Usage: python script.py subtract <x> <y>")
            sys.exit(1)
        x = float(sys.argv[2])
        y = float(sys.argv[3])
        print(f"Result: {subtract(x, y)}")

    elif command == 'multiply':
        if len(sys.argv) != 4:
            print("Usage: python script.py multiply <x> <y>")
            sys.exit(1)
        x = float(sys.argv[2])
        y = float(sys.argv[3])
        print(f"Result: {multiply(x, y)}")

    elif command == 'divide':
        if len(sys.argv) != 4:
            print("Usage: python script.py divide <x> <y>")
            sys.exit(1)
        x = float(sys.argv[2])
        y = float(sys.argv[3])
        result = divide(x, y)
        print(f"Result: {result}")

    elif command == 'greet':
        if len(sys.argv) != 3:
            print("Usage: python script.py greet <name>")
            sys.exit(1)
        name = sys.argv[2]
        print(greet(name))

    else:
        print("Unknown command.")
        sys.exit(1)

if __name__ == "__main__":
    main()
