# -*- coding: utf-8 -*-
# ###########################
# #    MTH 691 Program 6-Quote   ##
# ###########################

import pandas as pd
import plotly.offline as py
import plotly.graph_objs as go
import pathlib
from bullet import Bullet, ScrollBar, colors, emojis
from time import time
import Projfuncs as pf
import projLists
import os
import sys
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from scipy.interpolate import spline

def program6(fileloc1, fileloc2, filetype1, filetype2, ticker):
    init_tm = time()

    # Make dir
    fsplit = fileloc1.split('_')
    date = fsplit[len(fsplit) - 1][:-4]
    os.chdir(str(pathlib.Path.home()) + "/workspace/")
    dirpath = "/space/common/workspace/phase1_output/program6Q_out/plotly/" + filetype1 + "/" + filetype2 + "/" + date + "/"
    pathlib.Path(dirpath).mkdir(parents=True, exist_ok=True)

    print("Getting data...")
    data1 = pf.get_tickerData(fileloc1, filetype1, "X:SXBTUSD", "Q")
    print(ticker)
    data2 = pf.get_tickerData(fileloc2, filetype2, ticker, "Q")
    print("Got data. Generating plot...")

    #################
    # Plotting time #
    #################    
    if(data1.empty or data2.empty):
        print("At date " + date + ", ticker" + ticker + " had no quote data\n")
        return

    trace = go.Scatter(x = data1.Time, y = data2["Bid Price"] - data1["Bid Price"])

    title_date = data1.Time[len(data1) - 1].strftime('%b %-d, %Y')
    layout = go.Layout(xaxis={'title': 'Time (UTC)', 'type': 'date',
                            'tickformat': '%I:%M:%S %p'},
                       yaxis={'title': 'Spread'},
                       title=ticker + " | " + "Spread | " + title_date)
    
    fig = go.Figure(data = [trace], layout = layout)
    # Output the plot
    imgname = ticker + "_" + "spread_" + filetype1 + "_" + filetype2 + "_" + date
    py.plot(fig, 
            filename=dirpath + imgname + ".html", 
            image="png",
            image_filename=imgname,
            image_width=1024,
            image_height=768,
            auto_open=False, 
            show_link=False)
    
    print("Ticker", ticker, "at date", date, "finished in", 
          time() - init_tm, "seconds")

def yeda6(fileloc1, fileloc2, filetype1, filetype2, ticker):
    init_tm = time()

    # Make dir
    fsplit = fileloc1.split('_')
    date = fsplit[len(fsplit) - 1][:-4]
    os.chdir(str(pathlib.Path.home()) + "/workspace/")
    dirpath = "/space/common/workspace/phase1_output/program6Q_out/matplotlib/" + filetype1 + "/" + filetype2 + "/" + date + "/"
    pathlib.Path(dirpath).mkdir(parents=True, exist_ok=True)

    print("Getting data...")
    df1 = pf.get_tickerData(fileloc1, filetype1, "X:SXBTUSD", "Q")
    print("X:SXBTUSD", ticker)
    df2 = pf.get_tickerData(fileloc2, filetype2, ticker, "Q")
    print("Got data. Generating plot...")

    #################
    # Plotting time #
    #################
    if(df1.empty or df2.empty):
        print("At date " + date + ", ticker" + ticker + " had no trade data\n")
        return

    
    #f=interpolate.interp1d(df2.Time, df2["Trade Price"],kind="slinear")
    # ‘slinear’, ‘quadratic’ and ‘cubic’ refer to a spline interpolation of first, second or third order)
    #timenew=df1["Time"]
    #timenew=timenew[timenew<=max(df2["Time"]) & timenew>=min(df2["Time"])]
    #df2new=f(timenew)
    
    # pl.plot(df1["Time"],df2new,label=str(kind))

    df2.dropna(axis=0, how="any")
    df1.dropna(axis=0, how="any")
    
    df2["Time"][0]=df1["Time"][0]
    df2["Time"][len(df2["Time"])-1]=df1["Time"][len(df1["Time"])-1]
    
    f=interpolate.interp1d(df2["Time"], df2["Bid Price"],kind="zero")
    
    df2new=f(df1["Time"])
    
    
    df1.Time = pd.to_datetime(df1.Time, unit='s')
    df2.Time = pd.to_datetime(df2.Time, unit='s')
    
    #df1["Time"] = pd.to_datetime(df1["Time"])
    #df2["Time"] = pd.to_datetime(df2["Time"])
    
    #df2["Time"][0]=df1["Time"][0]
    #df2["Time"][-1]=df1["Time"][-1]


    
    
    #print(len(df2["Time"]))
    #print(len(df2["Trade Price"]))
    #print(max(df1["Time"]))
    #print(max(df2["Time"]))
    #print(df1["Time"][len(df1["Time"])-1])
    #print(df2["Time"][len(df2["Time"])-1])
    
    
    
    
    
    title_date = (df1["Time"][len(df1["Time"]) - 1]).strftime('%b %-d, %Y')
    #df2new=spline(df2["Time"], df2["Trade Price"],df1["Time"])
    
    
    df1 = df1.set_index("Time")
    df1["Bid Price"] = df1["Bid Price"] - df2new
    dfgroupby = df1[["Bid Price", "Contributor Id" ]].groupby("Contributor Id")
    fig,ax = plt.subplots(figsize = (20,8))
    dfgroupby["Bid Price"].plot(ax = ax, legend = True)
    

    #fig, ax = plt.subplots(figsize=(20,8))
    #ax.plot(df1.Time, df1["Trade Price"], color = "red", linewidth = 1.0, linestyle = '-')
    #ax.plot(df2.Time, df2["Trade Price"], color = "blue", linewidth = 1.0, linestyle = '-')
    
    
    
    ax.set_xlabel('Time (UTC)')
    ax.set_ylabel('Price')

    
    ax.set_title(ticker + " | " + "Spread | " + title_date)
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')

    #setting major locator
    alldays = mdates.HourLocator(interval = 1) # 3H interval
    ax.xaxis.set_major_locator(alldays)
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%I %p'))

    #setting minor locator
    hoursLoc = mdates.HourLocator(interval=30)
    ax.xaxis.set_minor_locator(hoursLoc)
    ax.xaxis.set_minor_formatter(mdates.DateFormatter('%M'))
    ax.legend()

    imgname = ticker + "_" + "spread_" + filetype1 + "_" + filetype2 + "_" + date + ".png"
    fig.savefig(dirpath + imgname)

    print("Ticker", ticker, "at date", date, "finished in", 
          time() - init_tm, "seconds")

# ##################
# # Main Function ##
# ##################

# +
if __name__ == "__main__":
    print("Program 6: Plot the Quote Spread")
    print("Type 'list' to get a list of valid inputs")
    TYPE1 = Bullet(
        prompt="\nPlease choose a filetype: ",
        choices=["A", "B"],
        indent=0,
        align=5,
        margin=2,
        bullet=">",
        bullet_color=colors.bright(colors.foreground["green"]),
        word_color=colors.bright(colors.foreground["yellow"]),
        word_on_switch=colors.bright(colors.foreground["green"]),
        background_color=colors.background["black"],
        background_on_switch=colors.background["black"],
        pad_right=5
    )

    filetype1 = TYPE1.launch()

    print("You chose:", filetype1)

    filetype1 = pf.get_validInput(filetype1, 4)

#        filetype1 = pf.get_validInput("Type A or B files: ", 4)
    TYPE2 = Bullet(
        prompt="\nPlease choose a filetype: ",
        choices=["C", "D"],
        indent=0,
        align=5,
        margin=2,
        bullet=">",
        bullet_color=colors.bright(colors.foreground["green"]),
        word_color=colors.bright(colors.foreground["yellow"]),
        word_on_switch=colors.bright(colors.foreground["green"]),
        background_color=colors.background["black"],
        background_on_switch=colors.background["black"],
        pad_right=5
    )

    filetype2 = TYPE2.launch()
    if filetype2 == "C":
        ticker_list = projLists.list_666
    else:
        ticker_list = projLists.list_680
        
    print("You chose:", filetype2)

    filetype2 = pf.get_validInput(filetype2, 4)

#        filetype2 = pf.get_validInput("Type C or D files: ", 4)
    DATE = Bullet(
        prompt="\nPlease choose a filetype: ",
        choices= projLists.file_list,
        indent=0,
        align=5,
        margin=2,
        bullet=">",
        bullet_color=colors.bright(colors.foreground["green"]),
        word_color=colors.bright(colors.foreground["yellow"]),
        word_on_switch=colors.bright(colors.foreground["green"]),
        background_color=colors.background["black"],
        background_on_switch=colors.background["black"],
        pad_right=5
    )

    date = DATE.launch()    

    
    date = pf.get_validInput(date, 0,filetype=filetype2)
#        date = pf.get_validInput("Enter Date in yyyymmdd: ", 0,
#                                 filetype=filetype2)
    jjj = []
    for i in ticker_list:
        if i in projLists.ticker_list:
            jjj.append(i)

    TICKER = Bullet(
        prompt="\nPlease choose a filetype: ",
        choices= ticker_list,
        indent=0,
        align=5,
        margin=2,
        bullet=">",
        bullet_color=colors.bright(colors.foreground["green"]),
        word_color=colors.bright(colors.foreground["yellow"]),
        word_on_switch=colors.bright(colors.foreground["green"]),
        background_color=colors.background["black"],
        background_on_switch=colors.background["black"],
        pad_right=5
    )

    ticker = TICKER.launch()      
    
    ticker = pf.get_validInput(ticker, 1)
    ticker = ticker[0]


    OPTION = Bullet(
        prompt="\nPlease choose a filetype: ",
        choices= ["plotly", "matplotlib"],
        indent=0,
        align=5,
        margin=2,
        bullet=">",
        bullet_color=colors.bright(colors.foreground["green"]),
        word_color=colors.bright(colors.foreground["yellow"]),
        word_on_switch=colors.bright(colors.foreground["green"]),
        background_color=colors.background["black"],
        background_on_switch=colors.background["black"],
        pad_right=5
    )

    option = OPTION.launch()      
        
if (filetype1 == "A"):
    fileloc1 = "/space/data/new/PLUSTICK_1619_" + date + ".txt"
if (filetype1 == "B"):
    fileloc1 = "/space/data/new/PLUSTICK_FI_1356_" + date + ".txt"
if (filetype2 == "C"):
    fileloc2 = "/space/data/new/PLUSTICK_FUTURES_666_" + date + ".txt"
if (filetype2 == "D"):
    fileloc2 = "/space/data/new/PLUSTICK_FUTURES_680_" + date + ".txt"

if (option == "plotly"):
    program6(fileloc1, fileloc2, filetype1, filetype2, ticker)
else:
    yeda6(fileloc1, fileloc2, filetype1, filetype2, ticker)
