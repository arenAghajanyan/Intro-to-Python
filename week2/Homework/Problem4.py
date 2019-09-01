import argparse
parser = argparse.ArgumentParser()
parser.add_argument("st", help="",type=str)
args = parser.parse_args()
a=args.st.lower().count("usa")
print("The given text:", args.st)
print("The USA count is:", a)
print("The new string:",args.st.lower().replace("USA","Armenia").replace("usa","Armenia"))