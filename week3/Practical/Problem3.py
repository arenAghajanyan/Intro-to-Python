import argparse
l2=[12,3456,1314,1,0,3]
pars = argparse.ArgumentParser()
pars.add_argument("inp", help="input",type=int)
args = pars.parse_args()
print(l2)
print("Number of",args.inp,"=",l2.count(args.inp))