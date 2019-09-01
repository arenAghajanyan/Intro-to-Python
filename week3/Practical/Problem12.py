import argparse
pars=argparse.ArgumentParser()
pars.add_argument("inp",help="no",type=int)
args=pars.parse_args()
set3={1,2,3,4,5}
list1=list(set3)
b=min(list1)
c=max(list1)
a=args.inp
if(a>list1[0] and a<list1[-1]):
    print(True)
else:
    print(False)