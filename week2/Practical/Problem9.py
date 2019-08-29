import argparse
parser = argparse.ArgumentParser()
parser.add_argument("script", help="script", type=str)
parser.add_argument("int1", help="integer", type=int)
parser.add_argument("int2", help="integer", type=int)
args = parser.parse_args()
print("The given text: "+args.script)
print("Start index:",args.int1)
print("End index:",args.int2)
a=args.int1
b=args.int2
c=args.script
print("Output string: ")
print(c[a::b])