import argparse
pars=argparse.ArgumentParser()
pars.add_argument("st1",help="no",type=str)
pars.add_argument("st2",help="no",type=str)
args=pars.parse_args()
di1={'key1':'hi','key2':'bee','key3':'lol'}
print(di1)
di1[args.st1]=args.st2
print(di1)