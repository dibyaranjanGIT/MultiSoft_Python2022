import argparse
parser = argparse.ArgumentParser()

parser.add_argument('--x', type=float, default=1.0,
                        help="Enter a number ")

args = parser.parse_args()

num = int(args.x)

for i in range(num+1):
    i_str = str(i)
    len_i = len(i_str)
    s = [int(j)**len_i for j in i_str]
    sum = 0
    for k in s:
        sum = k+sum
    if sum == i:
        print(i, 'is an armstrong number.')