#!/usr/bin/env python
# coding: utf-8
# %%

# ###########################
# # program 3.6 ##
# ###########################

# %%


import numpy as np
import pandas as pd
import plotly.offline as py
import plotly.graph_objs as go
import pathlib
from time import time
import datetime as dt
import os
import sys
import projfuncs36 as pf
import projLists as pl
import matplotlib.pyplot as plt
import matplotlib.dates as mdates


# %%


def get_date_list(begin_date,end_date):
    date_list = [x.strftime('%Y%m%d') for x in list(pd.date_range(start=begin_date, end=end_date))]
    return date_list


# %%


def get_spot(filetype, rf, datelist):
    
    init_tm = time()

    ticker = "X:SXBTUSD"
    CI = "Contributor Id"
    Spot = pd.DataFrame()
    Ep = pd.DataFrame()
    
    if (filetype == "A"):
        venuelist = ['CNB', 'CTC', 'KKN']    
        while True:
            print("Venue list: ", venuelist)
            venue = input("Enter one venue from the list above: ")
            if venue in venuelist:
                break
            else:
                print("Wrong venue") 
    if (filetype == "B"):
        print('B had no venue data. Ignore venue choice.')

    for date in datelist:
        if (filetype == "A"):
            fileloc = "/space/data/new/PLUSTICK_1619_" + date + ".txt"
        if (filetype == "B"):
            fileloc = "/space/data/new/PLUSTICK_FI_1356_" + date + ".txt"
        try:
            s = pf.get_tickerData(fileloc, filetype, ticker, "T")
            if (filetype == "A"):
                s = s[s[CI]==venue].iloc[-1]
            else:
                s = s.iloc[-1]
            Spot = Spot.append(s[['Time','Trade Price']])
            interval = dt.datetime.strptime(enddate, '%Y%m%d'
                    ) - dt.datetime.strptime(str(s['Time'])[0:-3],
                                                 '%Y-%m-%d %H:%M:%S.%f')
            x = interval.days
            p = s['Trade Price'] * ( 1 + rf * ( x/365 ) )
            Ep = Ep.append(pd.DataFrame([[s['Time'], p]]), ignore_index=True)
        except:
            continue

    if Spot.empty:
        print("Venue had no spot price data.")
        raise SystemExit
    else:
        Ep.columns = ['Time','Trade Price']
    print('Spot and theoretical data finished in ', time()-init_tm, 'seconds.')
    return(Spot, Ep, venue)


# %%


def get_fut(filetype, ticker, datelist):
    
    init_tm = time()
    Fut = pd.DataFrame()
    
    for date in datelist:
        if (filetype == "C"):
            fileloc = "/space/data/new/PLUSTICK_FUTURES_666_" + date + ".txt"
        if (filetype == "D"):
            fileloc = "/space/data/new/PLUSTICK_FUTURES_680_" + date + ".txt"
        try:
            f = pf.get_tickerData(fileloc, filetype, ticker, "T")
            f = f.iloc[-1]
            f['Trade Price']
            Fut = Fut.append(f[['Time','Trade Price']])
        except:
            continue
    if Fut.empty:
        print("Venue had no future price data.")
    print('Future data finished in ', time()-init_tm, 'seconds')
    return(Fut)


# %%


def yeda36(spot, future, Ep, venue, f_ticker, filetype1, filetype2):
    
    #################
    # Plotting time #
    #################
    init_tm = time()
    
    # Make dir
    os.chdir(str(pathlib.Path.home()) + "/workspace/")
    #/space/common/workspace/
    dirpath = "/space/common/workspace/phase3_output/program6_out/" + filetype1 + '_' + filetype2 + "/"
    pathlib.Path(dirpath).mkdir(parents=True, exist_ok=True)
    
    Spot["Time"] = pd.to_datetime(Spot["Time"])
    Fut["Time"] = pd.to_datetime(Fut["Time"])
    Ep["Time"] = pd.to_datetime(Ep["Time"])

    fig, ax = plt.subplots(figsize=(20,8))
    ax.plot(Spot['Time'], Spot['Trade Price'],color = "blue", linewidth = 1.0, 
            linestyle = '-', label = 'Spot')
    ax.plot(Fut['Time'], Fut['Trade Price'],color = "red", linewidth = 1.0,
            linestyle = '-', label = 'Futures')
    ax.plot(Ep['Time'], Ep['Trade Price'],color = "green", linewidth = 1.0,
            linestyle = '-', label = 'Theoretical')
    
    ax.set_xlabel('Date (UTC)')
    ax.set_ylabel('Price')
    
    ax.set_title('Bitcoin Spot | Future(EXP:' + f_ticker[7:10] + ") | Theoretical price")
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')

    ax.legend()
    imgname = "S:" + venue + "_" + f_ticker + ".png"
    fig.savefig(dirpath + imgname)

    print("Ticker", f_ticker, "finished in", time() - init_tm, "seconds")


# ##################
# # Main Function ##
# ##################

# %%





# %%


if __name__ == "__main__":
    try:
        s_filetype = sys.argv[1]
        f_filetype = sys.argv[2]
        venue = sys.argv[3]
        f_ticker = sys.argv[4]
        rf = sys.argv[5]
    except IndexError:
        print("Program 3.6: Plot spot/future/theoretical price of Bitcoin")
        s_filetype = pf.get_validInput("Type A or B files: ", 4)
        f_filetype = pf.get_validInput("Type C or D files: ", 4)
        
        ## TICKER
        if (f_filetype == "C"):
            tickerlist = pl.list_666
        if (f_filetype == "D"):
            tickerlist = pl.list_680
        dic = pd.DataFrame([['01','F'], ['02','G'], ['03','H'], ['04','J'], ['05','K'],
                            ['06','M'], ['07','N'], ['08','Q'], ['09','U'], ['10','V'],
                            ['11','X'], ['12','Z']], columns = ['Month', 'Futures'])
        while True:
            message = '\n'.join([" Jan - F     Feb - G     Mar - H    Apr - J",
                                 " May - K    June - M    July - N    Aug - Q",
                                 "Sept - U     Oct - V     Nov - X    Dec - Z",
                                 "Available future of different EXP:",
                                 str(tickerlist)])
            print(message)
            f_ticker = input("Enter one ticker from the list above: ")
            if f_ticker in tickerlist:
                break
            else:
                print("Wrong ticker")
        
        ## RISK-FREE RATE
        rf = eval(input("Enter risk-free rate on annual-basis = 0.02: "))
        
        year = 2000 + int(f_ticker[8:10])
        endm = int(dic[dic['Futures']==f_ticker[7]]['Month'])
        for x in range(1, endm + 1):
            if 12 == x:
                enddate = (dt.datetime(year, 12, 31)).strftime("%Y%m%d")
            else:
                enddate = (dt.datetime(year, x+1, 1) - dt.timedelta(days = 1)).strftime("%Y%m%d")
        if (dt.datetime.strptime('20190429','%Y%m%d') - dt.datetime.strptime(enddate,'%Y%m%d')).days >= 0:
            Date = get_date_list('20190101',enddate)
        else:
            Date = get_date_list('20190101','20190429')
        
    print("Getting data...")
    Spot, Ep, venue = get_spot(s_filetype, rf, Date)
    Fut = get_fut(f_filetype, f_ticker, Date)
    
    yeda36(Spot, Fut, Ep, venue, f_ticker, s_filetype, f_filetype)
#     print(Spot)
#     print(Ep)
#     F2:XBT\F19

