#!python
from argparse import ArgumentParser

def net_worth(years_working=3,monthly_income=24000):
    return years_working*monthly_income*1.2
if __name__=='__main__':
    parser=ArgumentParser()
    parser.add_argument('-y --years',action='store',dest='years',help='years you have been working',type=float)
    parser.add_argument('-m --monthly-income',action='store',dest='income',help='your monthly income',type=float)
    args=parser.parse_args()
    print("Your net worth working for {0} years, earning {1} your \n Net Worth should be :\t {2}".format(args.years,args.income,net_worth(args.years,args.income)))

