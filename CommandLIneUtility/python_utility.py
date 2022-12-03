import argparse
import sys

def calculator(args):
    if args.o == 'add':
        return args.x + args.y
    elif args.o == "mul":
        return args.x * args.y
    elif args.o == "div":
        return args.x / args.y
    elif args.o == "dif":
        return args.x - args.y
    else:
        return "Something wrong!"

if __name__ == "__main__":
    parser = argparse.ArgumentParser() # Creating an instance
    parser.add_argument('--x', type=float, default=1.0,
                        help="Pass in the value of first number")
    parser.add_argument('--y', type=float, default=1.0,
                        help="Pass in the value of second number")

    parser.add_argument('--o', type=str, default='add',
                        help="Pass in the function to be called")

    args = parser.parse_args() # This statement parses all the argument add here

    sys.stdout.write(str(calculator(args)))


# How to run this utility
# python python_utility.py --x 4 --y 6 --o add