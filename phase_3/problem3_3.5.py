# ###########################
# #    MTH 691 Program 3.5  ##
# ###########################

import pandas as pd
import plotly.offline as py
import plotly.graph_objs as go
import pathlib
from time import time
import projfuncs as pf
import os
import sys
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import time, datetime
import numpy as np

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
sns.set()


def call(fileloc, filetype, ticker):

    # Make dir
    fsplit = fileloc.split('_')
    date = fsplit[len(fsplit) - 1][:-4]
    os.chdir(str(pathlib.Path.home()) + "/workspace/")
    dirpath = "phase3_output/program3.1_out/" 
    pathlib.Path(dirpath).mkdir(parents=True, exist_ok=True)

    print("Getting data...")
    df = pf.get_tickerData(fileloc, filetype, ticker, "T")
    print("Got data. Generating plot...")
    return(df)


def get_date_list(begin_date, end_date):
    date_list = [x.strftime('%Y%m%d') for x in list(pd.date_range(start = begin_date, end = end_date))]
    return date_list


# ##################
# # Main Function ##
# ##################

if __name__ == "__main__":
    try:
        filetype = sys.argv[1]
        ticker = sys.argv[2]
        option = sys.argv[3]
    except IndexError:
        print("Program 3.1: Plot Trade Prices (aggregated)")
        print("Type 'list' to get a list of valid inputs")

        filetype = "A"
        ticker = "X:SXBTUSD"       

    b = pd.DataFrame()
    Date = get_date_list('20190101','20190131')
    for date in Date:
        try:
            if (filetype == "A"):
                fileloc = "/space/data/new/PLUSTICK_1619_" + date + ".txt"
            if (filetype == "B"):
                fileloc = "/space/data/new/PLUSTICK_FI_1356_" + date + ".txt"
            if (filetype == "C"):
                fileloc = "/space/data/new/PLUSTICK_FUTURES_666_" + date + ".txt"
            if (filetype == "D"):
                fileloc = "/space/data/new/PLUSTICK_FUTURES_680_" + date + ".txt"
            df1 = call(fileloc, filetype, ticker)
            # df2 = call(fileloc, filetype, ticker2)
            df1 = df1.iloc[-1:,1:2]
            # df2 = df2.iloc[-1:,0:2]
            b = b.append(df1)
            # crypto_price = crypto_price.append(df2)
        except:
            pass
        continue
    #print(b)
    #print(b.shape)
    #print(b.T)
    #b=b.T
    #b.rename(index={'Trade Price':'b'},inplace=True)
    #b.columns = ['1', '2', '3']
    print(b)


b.describe()

a = b.describe()
z = a.iloc[2]
b1 = z[0]
b1

if __name__ == "__main__":
    try:
        filetype = sys.argv[1]
        ticker = sys.argv[2]
        option = sys.argv[3]
    except IndexError:
        print("Program 3.1: Plot Trade Prices (aggregated)")
        print("Type 'list' to get a list of valid inputs")

        filetype = "A"
        ticker = "X:SXBTUSD"       

    c = pd.DataFrame()
    Date = get_date_list('20190201','20190228')
    for date in Date:
        try:
            if (filetype == "A"):
                fileloc = "/space/data/new/PLUSTICK_1619_" + date + ".txt"
            if (filetype == "B"):
                fileloc = "/space/data/new/PLUSTICK_FI_1356_" + date + ".txt"
            if (filetype == "C"):
                fileloc = "/space/data/new/PLUSTICK_FUTURES_666_" + date + ".txt"
            if (filetype == "D"):
                fileloc = "/space/data/new/PLUSTICK_FUTURES_680_" + date + ".txt"
            df1 = call(fileloc, filetype, ticker)
            # df2 = call(fileloc, filetype, ticker2)
            df1 = df1.iloc[-1:,1:2]
            # df2 = df2.iloc[-1:,0:2]
            c = c.append(df1)
            # crypto_price = crypto_price.append(df2)
        except:
            pass
        continue
    #print(b)
    #print(b.shape)
    #print(b.T)
    #b=b.T
    #b.rename(index={'Trade Price':'b'},inplace=True)
    #b.columns = ['1', '2', '3']
    print(c)

c.describe()

a = c.describe()
z = a.iloc[2]
c1 = z[0]
c1

if __name__ == "__main__":
    try:
        filetype = sys.argv[1]
        ticker = sys.argv[2]
        option = sys.argv[3]
    except IndexError:
        print("Program 3.1: Plot Trade Prices (aggregated)")
        print("Type 'list' to get a list of valid inputs")

        filetype = "A"
        ticker = "X:SXBTUSD"       

    d = pd.DataFrame()
    Date = get_date_list('20190301','20190331')
    for date in Date:
        try:
            if (filetype == "A"):
                fileloc = "/space/data/new/PLUSTICK_1619_" + date + ".txt"
            if (filetype == "B"):
                fileloc = "/space/data/new/PLUSTICK_FI_1356_" + date + ".txt"
            if (filetype == "C"):
                fileloc = "/space/data/new/PLUSTICK_FUTURES_666_" + date + ".txt"
            if (filetype == "D"):
                fileloc = "/space/data/new/PLUSTICK_FUTURES_680_" + date + ".txt"
            df1 = call(fileloc, filetype, ticker)
            # df2 = call(fileloc, filetype, ticker2)
            df1 = df1.iloc[-1:,1:2]
            # df2 = df2.iloc[-1:,0:2]
            d = d.append(df1)
            # crypto_price = crypto_price.append(df2)
        except:
            pass
        continue
    #print(b)
    #print(b.shape)
    #print(b.T)
    #b=b.T
    #b.rename(index={'Trade Price':'b'},inplace=True)
    #b.columns = ['1', '2', '3']
    print(d)

d.describe()

a = d.describe()
z = a.iloc[2]
d1 = z[0]
d1

if __name__ == "__main__":
    try:
        filetype = sys.argv[1]
        ticker = sys.argv[2]
        option = sys.argv[3]
    except IndexError:
        print("Program 3.1: Plot Trade Prices (aggregated)")
        print("Type 'list' to get a list of valid inputs")

        filetype = "A"
        ticker = "X:SXBTUSD"       

    e = pd.DataFrame()
    Date = get_date_list('20190401','20190430')
    for date in Date:
        try:
            if (filetype == "A"):
                fileloc = "/space/data/new/PLUSTICK_1619_" + date + ".txt"
            if (filetype == "B"):
                fileloc = "/space/data/new/PLUSTICK_FI_1356_" + date + ".txt"
            if (filetype == "C"):
                fileloc = "/space/data/new/PLUSTICK_FUTURES_666_" + date + ".txt"
            if (filetype == "D"):
                fileloc = "/space/data/new/PLUSTICK_FUTURES_680_" + date + ".txt"
            df1 = call(fileloc, filetype, ticker)
            # df2 = call(fileloc, filetype, ticker2)
            df1 = df1.iloc[-1:,1:2]
            # df2 = df2.iloc[-1:,0:2]
            e = e.append(df1)
            # crypto_price = crypto_price.append(df2)
        except:
            pass
        continue
    #print(b)
    #print(b.shape)
    #print(b.T)
    #b=b.T
    #b.rename(index={'Trade Price':'b'},inplace=True)
    #b.columns = ['1', '2', '3']
    print(e)

e.describe()

a = e.describe()
z = a.iloc[2]
e1 = z[0]
e1

plt.plot(["Jan","Feb","March","April"],[b1,c1,d1,e1])
plt.ylabel('monthly std')
plt.show()


















