# ###########################
# #    MTH 691 Program 5   ##
# ###########################

import pandas as pd
import plotly.offline as py
import plotly.graph_objs as go
import pathlib
from time import time
import projfuncs as pf
import os
import sys

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

def program5a(fileloc, filetype, ticker, quotetype):
    init_tm = time()

    # Make dir
    fsplit = fileloc.split('_')
    date = fsplit[len(fsplit) - 1][:-4]
    os.chdir(str(pathlib.Path.home()) + "/workspace/")
    dirpath = "phase1_output/program5a_out/plotly/" + filetype + "/" + date + "/" + quotetype + "/"
    pathlib.Path(dirpath).mkdir(parents=True, exist_ok=True)

    print("Getting data...")
    data = pf.get_tickerData(fileloc, filetype, ticker, "Q")
    print("Got data. Generating plot...")

    #################
    # Plotting time #
    #################

    if(data.empty):
        print("At date " + date + ", ticker" + ticker + " had no trade data\n")
        return

    # Make a trace for each venue
    traces = []
    for venue in data["Contributor Id"].unique():
        trace = go.Scatter(x = data.Time[data["Contributor Id"] == venue], 
                           y = data[quotetype + " Price"][data["Contributor Id"] == venue],
                           name = venue)
        traces.append(trace)

    title_date = data.Time[len(data) - 1].strftime('%b %-d, %Y')
    layout = go.Layout(xaxis={'title': 'Time (UTC)', 'type': 'date',
                                'tickformat': '%I:%M:%S %p'},
                       yaxis={'title': quotetype},
                    title=ticker + " | " + quotetype + " | " + title_date)
    
    fig = go.Figure(data = traces, layout = layout)

    # Output the plot
    imgname = ticker + "_" + "quotes_" + quotetype + "_" + filetype \
              + "_" + date
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

def zzg(fileloc, filetype, ticker, quotetype):
    init_tm = time()

    # Make dir
    fsplit = fileloc.split('_')
    date = fsplit[len(fsplit) - 1][:-4]
    os.chdir(str(pathlib.Path.home()) + "/workspace/")
    dirpath = "phase1_output/program5a_out/matplotlib/" + filetype + "/" + date + "_" + quotetype + "/"
    pathlib.Path(dirpath).mkdir(parents=True, exist_ok=True)

    print("Getting data...")
    df = pf.get_tickerData(fileloc, filetype, ticker, "Q")
    print("Got data. Generating plot...")
    df["Time"] = pd.to_datetime(df["Time"])
    df = df.set_index("Time")
    dfgroupby = df[[quotetype + " Price", "Contributor Id" ]].groupby("Contributor Id")
    fig,ax = plt.subplots(figsize = (20,8))
    dfgroupby[quotetype+" Price"].plot(ax = ax, legend = True)
    ax.set_xlabel('Time (UTC)')
    ax.set_ylabel(quotetype + " Price")
    title_date = df.index[len(df) - 1].strftime('%b %-d, %Y')
    ax.set_title(ticker + " | " + quotetype + " | " + title_date)
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
    imgname = ticker + "_" + quotetype + '_' + filetype + "_" + date + ".png"
    fig.savefig(dirpath + imgname)

    print("Ticker", ticker, "at date", date, "finished in", 
          time() - init_tm, "seconds")
###################
## Main Function ##
###################

if __name__ == "__main__":
    
    try:
        filetype = sys.argv[1]
        date = sys.argv[2]
        ticker = sys.argv[3]
        quotetype = sys.argv[4]
        option = sys.argv[5]
    except IndexError:
        print("Program 5a: Plot Bid or Ask Prices by Venue")
        print("Type 'list' to get a list of valid inputs")

        filetype = pf.get_validInput("Type A or B or C or D files: ", 4)
        date = pf.get_validInput("Enter Date in yyyymmdd: ", 0,
                                 filetype=filetype)
        ticker = pf.get_validInput("Enter One Ticker: ", 1)
        ticker = ticker[0]

        while True:
            quotetype = input("Enter Bid or Ask: ")
            if (quotetype in ["Bid", "Ask"]):
                break
            print("Invalid Input")

        while True:
            option = input("Enter 'plotly' or 'matplotlib': ")
            if (option in ['plotly', 'matplotlib']):
                break
            else:
                print("Invalid option")

    if (filetype == "A"):
        fileloc = "/space/data/new/PLUSTICK_1619_" + date + ".txt"
    if (filetype == "B"):
        fileloc = "/space/data/new/PLUSTICK_FI_1356_" + date + ".txt"
    if (filetype == "C"):
        fileloc = "/space/data/new/PLUSTICK_FUTURES_666_" + date + ".txt"
    if (filetype == "D"):
        fileloc = "/space/data/new/PLUSTICK_FUTURES_680_" + date + ".txt"
    if (option == "plotly"):       

        program5a(fileloc, filetype, ticker, quotetype)
    else:
        zzg(fileloc, filetype, ticker, quotetype)
