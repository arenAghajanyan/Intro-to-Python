import argparse
import datetime
import time
parser = argparse.ArgumentParser()
parser.add_argument("--year", help="no",type=int)
parser.add_argument("--day", help="no",type=int)
args = parser.parse_args()
now=datetime.datetime.now()
print(now)


if(args.day!=None):
    td1=datetime.timedelta(days=args.day) 
    print("Given days:",args.day)
  
else:
    print("Given days: not given")
now+=td1
if(args.year!=None):
    td1=datetime.timedelta(days=args.year*365.25)
    print("Given years:",args.year)
else:
    print("Given years: not given")
now+=td1
print("Final date:",now)