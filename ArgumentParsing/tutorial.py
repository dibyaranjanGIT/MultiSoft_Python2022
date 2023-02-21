import argparse

# create an ArgumentParser object
parser = argparse.ArgumentParser(description='Description of your program')

# add arguments to the parser
parser.add_argument('-f', '--file', type=str, help='File path')
parser.add_argument('-n', '--number', type=int, help='Number')

# parse the command-line arguments
args = parser.parse_args()


# To print the arguments
print(args.file)
print(args.number)

# access the values of the arguments
if args.file:
    print(f"File path: {args.file}")
if args.number:
    print(f"Number: {args.number}")


"""
python tutorial.py -f path/to/my/file.txt -n 42
"""