import argparse

parser = argparse.ArgumentParser()

parser.add_argument("name", help="Tipe in your name.", type=str)
args = parser.parse_args()

print ("Welcome, ", args.name + "!")