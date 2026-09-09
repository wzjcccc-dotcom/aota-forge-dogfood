import argparse
import json
import sys
from .core import add, subtract, multiply, divide

def main():
    parser = argparse.ArgumentParser(prog="calc")
    parser.add_argument("command", choices=["add", "sub", "mul", "div"], help="operation")
    parser.add_argument("a", help="first operand")
    parser.add_argument("b", help="second operand")
    parser.add_argument("--json", action="store_true", help="json output")
    args = parser.parse_args()

    try:
        a = float(args.a) if "." in args.a else int(args.a)
        b = float(args.b) if "." in args.b else int(args.b)
        # Try to parse as numbers, but handle invalid
        # If they are not numbers, the above will fail for int/float, but we need to handle
    except ValueError:
        msg = f"invalid numeric input: {args.a!r}, {args.b!r}"
        if args.json:
            print(json.dumps({"error": msg}))
        else:
            print(f"error: {msg}", file=sys.stderr)
        sys.exit(1)

    # Need to handle case where a or b are not numeric strings that contain letters
    # The above int/float parsing will work for valid numbers, but for invalid like "foo", it raises ValueError

    try:
        if args.command == "add":
            result = add(a, b)
        elif args.command == "sub":
            result = subtract(a, b)
        elif args.command == "mul":
            result = multiply(a, b)
        elif args.command == "div":
            result = divide(a, b)
    except ZeroDivisionError as e:
        msg = "division by zero"
        if args.json:
            print(json.dumps({"error": msg}))
        else:
            print(f"error: {msg}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        msg = str(e)
        if args.json:
            print(json.dumps({"error": msg}))
        else:
            print(f"error: {msg}", file=sys.stderr)
        sys.exit(1)

    if args.json:
        print(json.dumps({"result": result}))
    else:
        print(result)

if __name__ == "__main__":
    main()
