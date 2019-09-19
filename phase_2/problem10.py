# ###########################
# #    MTH 691 Program 10   ##
# ###########################

import warnings
warnings.simplefilter("ignore")
import pandas as pd
import pathlib
from time import time
import projLists
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

def trick(i,df, k, gamma, option):
    if i < int((k)/2):
        try:
            moving = df.iloc[:k].copy()
            midpoints = df[option].iloc[i]
            moving = moving.drop(moving.iloc[i].name)
            moving_average, std = moving[option].describe()[1],  moving[option].describe()[2]
            strength = abs(midpoints - moving_average)-3*std - gamma
            if strength > 0:
                return [1,strength]
            else:
                return [0,strength]
        except IndexError:
            return [0,0]
    elif i > df.shape[0]-1-int((k)/2):
        try:
            moving = df.iloc[df.shape[0]-1-k:].copy()
            midpoints = df[option].iloc[i]
            moving = moving.drop(moving.iloc[i].name)
            moving_average, std = moving[option].describe()[1],  moving[option].describe()[2]
            strength = abs(midpoints - moving_average)-3*std - gamma
            if strength > 0:
                return [1,strength]
            else:
                return [0,strength]
        except IndexError:
            return [0,0]
    else:
        try:
            moving = df.iloc[i-int((k)/2):i+int((k)/2)].copy()
            midpoints = df[option].iloc[i]
            moving = moving.drop(moving.iloc[int((k)/2)].name)
            moving_average, std = moving[option].describe()[1],  moving[option].describe()[2]
            strength = abs(midpoints - moving_average)-3*std - gamma
            if strength > 0:
                return [1,strength]
            else:
                return [0,strength]
        except IndexError:
            return [0,0]


def k_gamma(df, k, gamma ,option):
    num = len(df)
    outliers = []
    strength = []
    if num <= k:
        return False
    with Pool(os.cpu_count()-4) as p:
        dfs = p.starmap(trick, zip(range(num),repeat(df),repeat(k),repeat(gamma), repeat(option)))
    for i in dfs:
        outliers.append(i[0])
        strength.append(i[1])
    df["Outliers"] = outliers
    df["Strength"] = strength
    return df


def yeda10(filetype, df):
    
    df["Time"] = pd.to_datetime(df["Time"])
    
    #################
    # Plotting time #
    #################      
    
    init_tm = time()
    
    # Directory stuff
    os.chdir(str(pathlib.Path.home()) + "/workspace/")
    dirpath = "/".join(["/space/common/workspace/phase2_output/program10_out/", filetype, date, ticker, option]) + "/"
    pathlib.Path(dirpath).mkdir(parents=True, exist_ok=True)
    
    fig, ax1 = plt.subplots(figsize=(20,8))
    ax1.set_xlabel('Time (UTC)')    
    
    method_name = "K_gamma"
    k, gamma = input("Please input k, gamma: ").split()
    parameters = k + '_' + gamma
    k, gamma = int(k), float(gamma)
#     k, gamma = [20, 1]
    print("Got data. Generating plot...")

    message = ""
    lns1 = []
    lns2 = []
    lns3 = []
    clight = ['#d7f8ff', '#fef2c2', '#e4d1ff', 'lightgreen','#ffe1ff']
    cdark = ['#00bfff', '#ffdb4d', 'purple', 'darkgreen', '#e066ff']
    for venue in venuelist:
        df_CI = df[df[CI] == venue]
        #l1: Raw Data
        df_CI = df_CI[["Time", option]]
        df_CI["Outliers"] = 0
        #l2: Clean Data
        df_CI = k_gamma(df_CI, k, gamma ,option)    
        clean = df_CI[df_CI["Outliers"] == 0]
        #l3: outliers
        ols = df_CI[df_CI["Outliers"] == 1]
        
        
        #l1: Raw Data plot
        l1 = ax1.plot(df_CI["Time"], df_CI["Trade Price"], label = venue + " Raw", color = clight[len(lns1)])
        lns1 = lns1 + l1
#         y1 = df["Trade Price"]
#         y1rg = max(df["Trade Price"]) - min(df["Trade Price"])
#         ax1.set_ylim(min(y1)-3*y1rg, max(y1)+10*y1rg)

        #l2: Clean Data plot
        l2 = ax1.plot(clean["Time"], clean[option], label = venue + " Clean", color = cdark[len(lns2)])
        lns2 = lns2 + l2
        
        # l3: outliers plot
        l3 = ax1.plot(ols["Time"], ols[option],'ro', label = venue + " Outliers", color = 'red')
        lns3 = lns3 + l3


        message = "\n".join([message,
                             "Venue: " + venue,
                             "Method: " + method_name,
                             "Parameters: " + parameters, 
                             "Number of outliers: " + str(ols.shape[0]), 
                             "Total number of observations: " + str(df_CI.shape[0]), 
                             "Percentage outliers: " + str(ols.shape[0] / df_CI.shape[0]),
                             "Cleaned price range:" + str(clean[option].min()) + '-' + str(clean[option].max()),
                             "Raw price range:" + str(df_CI[option].min()) + '-' + str(df_CI[option].max()),
                             "",])
        


    print(message)
    fname = dirpath + ticker + "_" + parameters
    with open(fname + "_statistics.txt", 'w+') as f:
        f.write(message)

    
    if filetype == "B":
        # l4: Volume spread
        try:
            vol['Bid Size Dec']
            vol['Ask Size Dec']
            ax4 = ax1.twinx()
            lns4 = ax4.plot(vol['Time'], vol["Bid Size Dec"] - vol["Ask Size Dec"], color = "lightgreen",
                            linewidth = 0.5, linestyle = '-', label = 'Volume spread')
            ax4.set_ylabel('Volume spread')
    #         y4 = vol["Bid Size Dec"] - vol["Ask Size Dec"]
    #         y4rg = max(y4) - min(y4)
    #         ax4.set_ylim(min(y4) - 0.2*y4rg, max(y4) + 0.1*y4rg)
        except KeyError:
            print("At date " + date + ", ticker" + ticker + " had no quote size data\n")

    ax1.set_xlabel("Time")
    ax1.set_ylabel("Trade Price")
    
    title_date = df.Time[len(df) - 1].strftime('%b %-d, %Y')
    ax1.set_title(ticker + " | " + "Volume | " + title_date)
    ax1.spines['right'].set_color('none')
    ax1.spines['top'].set_color('none')

    #setting major locator
    alldays =  mdates.HourLocator(interval = 1)# 3H interval
    ax1.xaxis.set_major_locator(alldays)
    ax1.xaxis.set_major_formatter(mdates.DateFormatter('%I %p'))

    #setting minor locator
    hoursLoc = mdates.HourLocator(interval=30)
    ax1.xaxis.set_minor_locator(hoursLoc)
    ax1.xaxis.set_minor_formatter(mdates.DateFormatter('%M'))

    #setting legends
    if filetype == "B":
        lns = lns1 + lns2 + lns3 + lns4
    else:
        lns = lns1 + lns2 + lns3
    labs = [l.get_label() for l in lns]
    legend = ax1.legend(lns, labs, loc=0)

    imgname = ticker + "_" + "trades_" + "Volume spread" + filetype + "_" + date + ".png"
    fig.savefig(dirpath + imgname)

    print("Ticker", ticker, "at date", date, "finished in", 
          time() - init_tm, "seconds")

# ##################
# # Main Function ##
# ##################

if __name__ == "__main__":
    try:
        filetype = sys.argv[1]
        date = sys.argv[2]
        ticker = sys.argv[3]
        option = sys.argv[4]
        method = int(sys.argv[5])
    except IndexError:
        print("Program 10: Plot Prices w/o outliers & Volume soread")
        print("Type 'list' to get a list of valid inputs")

        filetype = pf.get_validInput("Type A or B or C or D files: ", 4)
        date = pf.get_validInput("Enter Date in yyyymmdd: ", 0,
                                 filetype=filetype)
        ticker = pf.get_validInput("Enter One Ticker: ", 1)
        ticker = ticker[0]
        option = 'Trade Price'
        
        if (filetype == "A"):
            fileloc = "/space/data/new/PLUSTICK_1619_" + date + ".txt"
            CI = "Contributor Id"
        if (filetype == "B"):
            fileloc = "/space/data/new/PLUSTICK_FI_1356_" + date + ".txt"
            CI = "Contributor Id"
        if (filetype == "C"):
            fileloc = "/space/data/new/PLUSTICK_FUTURES_666_" + date + ".txt"
            CI = "Part Code"
        if (filetype == "D"):
            fileloc = "/space/data/new/PLUSTICK_FUTURES_680_" + date + ".txt"
            CI = "Part Code"
        
        print("Getting data...")
        vol = pf.get_tickerData(fileloc, filetype, ticker, "Q")
        df = pf.get_tickerData(fileloc, filetype, ticker, "T")
        print("Got data. Generating plot...")

        if(vol.empty):
            print("At date " + date + ", ticker" + ticker + " had no quote data\n")
        if(df.empty):
            print("At date " + date + ", ticker" + ticker + " had no trade data\n")

        df[CI] = df[CI].fillna('unknown')
        venuelist = df[CI].unique()
        
    yeda10(filetype, df)


