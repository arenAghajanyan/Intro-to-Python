import argparse
pars=argparse.ArgumentParser()
pars.add_argument("inp",help="no",type=int)
args=pars.parse_args()
set1={1,2,3,4,5}
print(set1)
set1.remove(args.inp)
print(set1)