import argparse
import sys

def calc(args):
    if args.o == 'add':
        return args.x + args.y

    elif args.o == 'mul':
        return args.x * args.y

    elif args.o == 'sub':
        return args.x - args.y

    elif args.o == 'div':
        return args.x / args.y

    else:
        return "Something went wrong"

if __name__ == '__main__':
    # The argparse module’s support for command-line interfaces is built around an instance of argparse.ArgumentParser.
    # It is a container for argument specifications and has options that apply the parser as whole:
    parser = argparse.ArgumentParser()

    # The ArgumentParser.add_argument() method attaches individual argument specifications to the parser
    parser.add_argument('--x', type=float, default=1.0,
                        help="Enter first number. This is a utility for calculation")

    parser.add_argument('--y', type=float, default=1.0,
                        help="Enter second number. This is a utility for calculation")

    parser.add_argument('--o', type=str, default="add",
                        help="This is a utility for calculation")

    # The ArgumentParser.parse_args() method runs the parser and places the extracted data in a
    args = parser.parse_args()
    sys.stdout.write(str(calc(args)))


# >python main.py --x 10 --y 20 --o add