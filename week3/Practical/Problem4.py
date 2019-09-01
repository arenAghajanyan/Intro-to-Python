import argparse
l1=[1,2,3,4,5,6,7,8,8,8]
pars=argparse.ArgumentParser()
pars.add_argument("inp",help="integer",type=int)
args=pars.parse_args()
print(l1)
l1.remove(args.inp)
print(l1)