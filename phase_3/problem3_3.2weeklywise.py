# ###########################
# #    MTH 691 Program 3-2   ##
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
    dirpath = "phase3_output/program3.2_out/" 
    pathlib.Path(dirpath).mkdir(parents=True, exist_ok=True)

    print("Getting data...")
    df = pf.get_tickerData(fileloc, filetype, ticker, "T")
    print("Got data. Generating plot...")
    return(df)


def get_date_list(begin_date, end_date):
    date_list = [x.strftime('%Y%m%d') for x in list(pd.date_range(start = begin_date, end = end_date, freq = 'W'))]
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
        print("Program 3.2: Plot Trade Volume (aggregated)")
        print("Type 'list' to get a list of valid inputs")

        filetype = "B"
        ticker = "X:SXBTUSD"       

    b = pd.DataFrame()
    Date = get_date_list('20190101','20190501')
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
            df1 = df1.iloc[-1:,3:4]
            # df2 = df2.iloc[-1:,0:2]
            b = b.append(df1)
            # crypto_price = crypto_price.append(df2)
        except:
            pass
        continue
    #print(b)
    #print(b.shape)
    #print(b.T)
    b=b.T
    b.rename(index={'Trade Vol Dec':'b'},inplace=True)
    b.columns = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16']
    print(b)


if __name__ == "__main__":
    try:
        filetype = sys.argv[1]
        ticker = sys.argv[2]
        option = sys.argv[3]
    except IndexError:
        print("Program 3.2: Plot Trade Volume (aggregated)")
        print("Type 'list' to get a list of valid inputs")

        filetype = "B"
        ticker = "X:SDAHUSD"       

    c = pd.DataFrame()
    Date = get_date_list('20190101','20190501')
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
            df1 = df1.iloc[-1:,3:4]
            # df2 = df2.iloc[-1:,0:2]
            c = c.append(df1)
            # crypto_price = crypto_price.append(df2)
        except:
            pass
        continue
    #print(b)
    #print(b.shape)
    #print(b.T)
    c=c.T
    c.rename(index={'Trade Vol Dec':'c'},inplace=True)
    c.columns = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16']
    print(c)


if __name__ == "__main__":
    try:
        filetype = sys.argv[1]
        ticker = sys.argv[2]
        option = sys.argv[3]
    except IndexError:
        print("Program 3.2: Plot Trade Volume (aggregated)")
        print("Type 'list' to get a list of valid inputs")

        filetype = "B"
        ticker = "X:SLTCUSD"       

    d = pd.DataFrame()
    Date = get_date_list('20190101','20190501')
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
            df1 = df1.iloc[-1:,3:4]
            # df2 = df2.iloc[-1:,0:2]
            d = d.append(df1)
            # crypto_price = crypto_price.append(df2)
        except:
            pass
        continue
    #print(b)
    #print(b.shape)
    #print(b.T)
    d=d.T
    d.rename(index={'Trade Vol Dec':'d'},inplace=True)
    d.columns = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16']
    print(d)


if __name__ == "__main__":
    try:
        filetype = sys.argv[1]
        ticker = sys.argv[2]
        option = sys.argv[3]
    except IndexError:
        print("Program 3.2: Plot Trade Volume (aggregated)")
        print("Type 'list' to get a list of valid inputs")

        filetype = "B"
        ticker = "X:SXRPUSD"       

    e = pd.DataFrame()
    Date = get_date_list('20190101','20190501')
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
            df1 = df1.iloc[-1:,3:4]
            # df2 = df2.iloc[-1:,0:2]
            e = e.append(df1)
            # crypto_price = crypto_price.append(df2)
        except:
            pass
        continue
    #print(b)
    #print(b.shape)
    #print(b.T)
    e=e.T
    e.rename(index={'Trade Vol Dec':'e'},inplace=True)
    e.columns = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16']
    print(e)


# # if __name__ == "__main__":
#     try:
#         filetype = sys.argv[1]
#         ticker = sys.argv[2]
#         option = sys.argv[3]
#     except IndexError:
#         print("Program 3.2: Plot Trade Volume (aggregated)")
#         print("Type 'list' to get a list of valid inputs")
#
#         filetype = "B"
#         ticker = "X:SBCHUSD"       
#
#     f = pd.DataFrame()
#     Date = get_date_list('20190101','20190501')
#     for date in Date:
#         try:
#             if (filetype == "A"):
#                 fileloc = "/space/data/new/PLUSTICK_1619_" + date + ".txt"
#             if (filetype == "B"):
#                 fileloc = "/space/data/new/PLUSTICK_FI_1356_" + date + ".txt"
#             if (filetype == "C"):
#                 fileloc = "/space/data/new/PLUSTICK_FUTURES_666_" + date + ".txt"
#             if (filetype == "D"):
#                 fileloc = "/space/data/new/PLUSTICK_FUTURES_680_" + date + ".txt"
#             df1 = call(fileloc, filetype, ticker)
#             # df2 = call(fileloc, filetype, ticker2)
#             df1 = df1.iloc[-1:,3:4]
#             # df2 = df2.iloc[-1:,0:2]
#             f = f.append(df1)
#             # crypto_price = crypto_price.append(df2)
#         except:
#             pass
#         continue
#     #print(b)
#     #print(b.shape)
#     #print(b.T)
#     f=f.T
#     f.rename(index={'Trade Vol Dec':'f'},inplace=True)
#     f.columns = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13']
#     print(f)


if __name__ == "__main__":
    try:
        filetype = sys.argv[1]
        ticker = sys.argv[2]
        option = sys.argv[3]
    except IndexError:
        print("Program 3.2: Plot Trade Volume (aggregated)")
        print("Type 'list' to get a list of valid inputs")

        filetype = "B"
        ticker = "X:SETHUSD"       

    g = pd.DataFrame()
    Date = get_date_list('20190101','20190501')
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
            df1 = df1.iloc[-1:,3:4]
            # df2 = df2.iloc[-1:,0:2]
            g = g.append(df1)
            # crypto_price = crypto_price.append(df2)
        except:
            pass
        continue
    #print(b)
    #print(b.shape)
    #print(b.T)
    g=g.T
    g.rename(index={'Trade Vol Dec':'g'},inplace=True)
    g.columns = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16']
    print(g)


output = b.append(c)
output = output.append(d)
output = output.append(e)
#output = output.append(f)
output = output.append(g)
output

output1=output.T
output1

output1.columns = ['X:SXBTUSD', 'X:SDAHUSD', 'X:SLTCUSD', 'X:SXRPUSD', 'X:SETHUSD']

corr = output1.corr()
corr

fig, ax = plt.subplots(figsize=(16, 16))
sns.heatmap(data=corr, square=True , annot=True, cbar=True, ax=ax)
ax.set_title("Correlation Matrix", fontsize=16)
dirpath = "phase3_output/program3.2_out/"
imgname = "phase3_3.2weeklywise" + ".png"
fig.savefig(dirpath + imgname)
