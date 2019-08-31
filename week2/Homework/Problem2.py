import argparse
parser = argparse.ArgumentParser()
parser.add_argument("st", help="",type=str)
args = parser.parse_args()
a=len(args.st)
a-=1
a/=2
a=int(a)
print("The given text:", args.st)
b=args.st[(a-1):(a+2)]
print("Middle 3 characters:", b)
print("The new string:",args.st[:(a-1)]+b.upper()+args.st[a+2:])