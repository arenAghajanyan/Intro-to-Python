import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--age", help="insert your age", type=str)
args = parser.parse_args()
if args.age:
    print("Happy Birthday, you are already", args.age, "years old!")