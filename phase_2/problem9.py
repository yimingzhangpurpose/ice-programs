import warnings
warnings.simplefilter("ignore")
import pandas as pd
from matplotlib import pyplot as plt
import matplotlib.dates as mdates
from multiprocessing import Pool 
import glob
import pathlib
from itertools import repeat
import projfuncs as pf
import os
import sys
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

if __name__ == "__main__":
    try:
        filetype = sys.argv[1]
        date = sys.argv[2]
        ticker = sys.argv[3]
        option1 = sys.argv[4]
        venue = sys.argv[5]
        method = int(sys.argv[6])
        if (option1 in ["Trade", "Bid", "Ask"]):
            if (option1 == "Trade"):
                option2 = "T"
            else:
                option2 = "Q"                                
        else:
            print("Invalid Input")
        option = option1 + " Price"
        if (filetype == "A"):
            fileloc = "/space/data/new/PLUSTICK_1619_" + date + ".txt"
        if (filetype == "B"):
            fileloc = "/space/data/new/PLUSTICK_FI_1356_" + date + ".txt"
        if (filetype == "C"):
            fileloc = "/space/data/new/PLUSTICK_FUTURES_666_" + date + ".txt"
        if (filetype == "D"):
            fileloc = "/space/data/new/PLUSTICK_FUTURES_680_" + date + ".txt"
        
        df = pf.get_tickerData(fileloc, filetype, ticker,  option2)
        
    except IndexError:
        print("Type 'list' to get a list of valid inputs")

        filetype = pf.get_validInput("Type A or B or C or D files: ", 4)
        date = pf.get_validInput("Enter Date in yyyymmdd: ", 0,
                                 filetype=filetype)
        ticker = pf.get_validInput("Enter One Ticker: ", 1)
        ticker = ticker[0]
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

        df = pf.get_tickerData(fileloc,  filetype, ticker, option2)
        option = option1 + " Price"

        df[CI] = df[CI].fillna('unknown')
        venuelist = df[CI].unique()        

                
        while True:
            method = 1
            if method in range(1, 4):
                break

    df = df[["Time", option]]
    df["Outliers"] = 0
    if (df.empty):
        print("Not enough data, quiting")

        
    elif method == 1:
        method_name = "K_gamma"
        k, gamma = input("Please input k, gamma: ").split()
        parameters = k + '_' + gamma
        k, gamma = int(k), float(gamma)       
        df = k_gamma(df, k, gamma ,option)


#    if (method != 3):
        # Directory stuff
        os.chdir(str(pathlib.Path.home()) + "/workspace/")
        dirpath = "/".join(["/space/common/workspace/phase2_output/program9_out", filetype, date, ticker, option1, method_name]) + "/"
        pathlib.Path(dirpath).mkdir(parents=True, exist_ok=True)
                
        df["Time"] = pd.to_datetime(df["Time"],errors = 'ignore')
        df1 = df[df["Outliers"] == 1]
        clean = df[df["Outliers"] == 0]
        message = "\n".join(["Method: " + method_name,
                             "Parameters: " + parameters, 
                             "Number of outliers: " + str(df1.shape[0]), 
                             "Total number of observations: " + str(df.shape[0]), 
                             "Percentage outliers: " + str(df1.shape[0] / df.shape[0]),
                             "Cleaned price range:" + str(min(clean[option])) + "-" + str(max(clean[option])),
                             "Raw price range:" + str(min(df[option])) + '-' + str(max(clean[option]))])
        print(message)
        fname = dirpath + ticker + '_aggregate_' + parameters
        with open(fname + "_statistics.txt", 'w+') as f:
            f.write(message)    

        fig,ax = plt.subplots(figsize = (16,9))
        ax.plot(df["Time"],df[option], label = "Raw price", color = '#dcdcdc')
        ax.plot(clean["Time"],clean[option], label = "Cleaned price")
        ax.plot(df1["Time"], df1[option],'ro', label = "Outliers", color = 'red')
        ax.set_xlabel("Time")
        ax.set_ylabel("Price")
        ax.set_title(" | ".join([ticker, option, date, method_name]))
        ax.spines['right'].set_color('none')
        ax.spines['top'].set_color('none')
        #setting major locator
        alldays =  mdates.HourLocator(interval = 3)# 3H interval
        ax.xaxis.set_major_locator(alldays)
        ax.xaxis.set_major_formatter(mdates.DateFormatter('%I %p'))
        ax.legend()
        fig.savefig(fname + ".png")
        df1.drop(columns=["Outliers"], inplace=True)
        df1.to_csv(fname + ".csv")
