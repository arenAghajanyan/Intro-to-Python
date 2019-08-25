import argparse
parser = argparse.ArgumentParser()
parser.add_argument("script", help="script", type=str)
args = parser.parse_args()
print("The given string: "+args.script)
print("All lowercase: "+args.script.lower())
print("All uppercase: "+args.script.upper())