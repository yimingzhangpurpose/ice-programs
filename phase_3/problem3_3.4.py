#!/usr/bin/env python
# coding: utf-8
# %% [markdown]
# ###########################
# #    MTH 691 Program 3.4  ##
# ###########################

# %%


import warnings
warnings.simplefilter("ignore")
import pandas as pd
import pathlib
from time import time
import projLists as pl
import projfuncs as pf
import os
import sys
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from multiprocessing import Pool 
import glob
from itertools import repeat
import subprocess
from sklearn.ensemble import IsolationForest


# %%


def yeda34(fileloc, filetype, date, option1, option2, tickerlist):
      
    init_tm = time()

    val_ticker = []
    for ticker in tickerlist:
        df = pf.get_tickerData(fileloc, filetype, ticker, option2)
        if(df.empty):
            print('empty')
            continue
        try:
            if option1 == "Trade":
                vol = df['Trade Size Dec']
            if option1 == "Ask":
                vol = df['Ask Size Dec']
            if option1 == "Bid":
                vol = df['Bid Size Dec']    
        except KeyError:
            continue
        val_ticker.append(ticker)

    if not val_ticker:
        print("At date " + date + ", instrument " + ins + " had no " + option1 + " volume size data\n")
        raise SystemExit
    
    print("Getting data...")
    while True:
        print("Valid ticker:", val_ticker)
        ticker = input("Enter ticker: ")
        if ticker in val_ticker:
            break
        else:
            print("Invalid Input") 
    
    #################
    # Plotting time #
    #################    
    
    # Directory stuff
    os.chdir(str(pathlib.Path.home()) + "/workspace/")
    dirpath = "/".join(["/space/common/workspace/phase3_output/program4_out", filetype, date, ticker]) + "/"
    pathlib.Path(dirpath).mkdir(parents=True, exist_ok=True)

    print("Generatting plot...")
    
    fig, ax = plt.subplots(figsize=(20,8))
    ax.set_xlabel('Time (UTC)') 
    ax.set_ylabel('Volume')
    
    df = pf.get_tickerData(fileloc, filetype, ticker, option2)
    if option1 == "Trade":
        vol = df['Trade Size Dec']
    if option1 == "Ask":
        vol = df['Ask Size Dec']
    if option1 == "Bid":
        vol = df['Bid Size Dec']   
    df["Time"] = pd.to_datetime(df["Time"])
    ax.plot(df['Time'], vol, linewidth = 0.5, linestyle = '-', label = ticker)

    title_date = df.Time[len(df) - 1].strftime('%b %-d, %Y')
    ax.set_title(ticker + " | " + option1 + " Volume | " + title_date)
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')

    #setting major locator
    alldays =  mdates.HourLocator(interval = 1)# 3H interval
    ax.xaxis.set_major_locator(alldays)
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%I %p'))

    #setting minor locator
    hoursLoc = mdates.HourLocator(interval=30)
    ax.xaxis.set_minor_locator(hoursLoc)
    ax.xaxis.set_minor_formatter(mdates.DateFormatter('%M'))
    
    ax.legend()
    imgname = ticker + "_" + option1 + "_" + "Volume" + filetype + "_" + date + ".png"
    fig.savefig(dirpath + imgname)

    print("Ticker", ticker, "at date", date, "finished in", 
          time() - init_tm, "seconds")


# %%


if __name__ == "__main__":
    try:
        filetype = sys.argv[1]
        date = sys.argv[2]
        ins = sys.argv[3]
        option1 = sys.argv[4]
    except IndexError:
        print("Program 3.4: Plot Trade/Ask/Bid Volume")
        print("Type 'list' to get a list of valid inputs")
        
        filetype = pf.get_validInput("Type A or B or C or D files: ", 4)
        date = pf.get_validInput("Enter Date in yyyymmdd: ", 0,
                                 filetype=filetype)
        while True:
            tl = pl.ticker_list
            Ins = []
            for x in tl:
                if len(x) == 9:
                    Ins.append(x[3:6])
            print("Instruments:", pd.unique(Ins))
            ins = input("Enter one instrument: ")
            if ins in Ins:
                break
            else:
                print("Invalid Input")
                
        while True:
            option1 = input("Enter Trade, Bid, or Ask: ")
            if (option1 in ["Trade", "Bid", "Ask"]):
                if (option1 == "Trade"):
                    option2 = "T"
                else:
                    option2 = "Q"                                
                break
            else:
                print("Invalid Input")  
        
    if (filetype == "A"):
        fileloc = "/space/data/new/PLUSTICK_1619_" + date + ".txt"
    if (filetype == "B"):
        fileloc = "/space/data/new/PLUSTICK_FI_1356_" + date + ".txt"
    if (filetype == "C"):
        fileloc = "/space/data/new/PLUSTICK_FUTURES_666_" + date + ".txt"
    if (filetype == "D"):
        fileloc = "/space/data/new/PLUSTICK_FUTURES_680_" + date + ".txt"
    
    tickerlist = []
    for x in tl:
        if len(x) == 9 and x[3:6] == ins:
            tickerlist.append(x)
    
    yeda34(fileloc, filetype, date, option1, option2, tickerlist)


# 
