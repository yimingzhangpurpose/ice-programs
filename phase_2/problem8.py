# ###########################
# #    MTH 691 Program 8   ##
# ###########################

import pandas as pd
import plotly.offline as py
import plotly.graph_objs as go
import pathlib
from time import time
import projLists
import projfuncs as pf
import os
import sys
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

def program8(fileloc, filetype, ticker):
    init_tm = time()

    # Make dir
    fsplit = fileloc.split('_')
    date = fsplit[len(fsplit) - 1][:-4]
    os.chdir(str(pathlib.Path.home()) + "/workspace/")
    dirpath = "/space/common/workspace/phase2_output/program8_out/plotly/" + filetype + "/" + date + "/"
    pathlib.Path(dirpath).mkdir(parents=True, exist_ok=True)

    print("Getting data...")
    data1 = pf.get_tickerData(fileloc, filetype, ticker, "Q")
    data2 = pf.get_tickerData(fileloc, filetype, ticker, "T")
    print("Got data. Generating plot...")

    #################
    # Plotting time #
    #################

    if(data1.empty):
        print("At date " + date + ", ticker" + ticker + " had no quote data\n")
        return

    # Plotting the data
    trace = go.Scatter(x = data1.Time, y = data1["Bid Size Dec"] - data1["Ask Size Dec"],
                        line = {'color': 'red'}, name = "Volume Spread")
    
    
    title_date = data1.Time[len(data1) - 1].strftime('%b %-d, %Y')
    layout = go.Layout(xaxis={'title': 'Time (UTC)', 'type': 'date',
                            'tickformat': '%I:%M:%S %p'},
                       yaxis={'title': 'Volume'},
                       title=ticker + " | Quotes | " + title_date)
    
    fig = go.Figure(data = [trace], layout = layout)

    # Output the plot
    imgname = ticker + "_" + "quotes_" + "Volume_" + filetype + "_" + date
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

def program82(fileloc, filetype, ticker):
    init_tm = time()

    # Make dir
    fsplit = fileloc.split('_')
    date = fsplit[len(fsplit) - 1][:-4]
    os.chdir(str(pathlib.Path.home()) + "/workspace/")
    dirpath = "/space/common/workspace/phase2_output/program8_out/plotly/" + filetype + "/" + date + "/"
    pathlib.Path(dirpath).mkdir(parents=True, exist_ok=True)

    print("Getting data...")
    data1 = pf.get_tickerData(fileloc, filetype, ticker, "Q")
    data2 = pf.get_tickerData(fileloc, filetype, ticker, "T")
    print("Got data. Generating plot...")

    #################
    # Plotting time #
    #################

    if(data2.empty):
        print("At date " + date + ", ticker" + ticker + " had no trade data\n")
        return

    # Plotting the data
    trace = go.Scatter(x = data2.Time, y = data2["Trade Price"],
                        line = {'color': 'blue'}, name = "Trade Price")
    
    
    title_date = data2.Time[len(data2) - 1].strftime('%b %-d, %Y')
    layout = go.Layout(xaxis={'title': 'Time (UTC)', 'type': 'date',
                            'tickformat': '%I:%M:%S %p'},
                       yaxis={'title': 'Trade Price'},
                       title=ticker + " | Trade | " + title_date)
    
    fig = go.Figure(data = [trace], layout = layout)

    # Output the plot
    imgname = ticker + "_" + "quotes_" + "Trade Price_" + filetype + "_" + date
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
    
def yeda8(fileloc, filetype, ticker):
    init_tm = time()

    # Make dir
    fsplit = fileloc.split('_')
    date = fsplit[len(fsplit) - 1][:-4]
    os.chdir(str(pathlib.Path.home()) + "/workspace/")
    dirpath = "/space/common/workspace/phase2_output/program8_out/matplotlib/" + filetype + "/" + date + "/"
    pathlib.Path(dirpath).mkdir(parents=True, exist_ok=True)

    print("Getting data...")
    df1 = pf.get_tickerData(fileloc, filetype, ticker, "Q")
    df2 = pf.get_tickerData(fileloc, filetype, ticker, "T")
    print("Got data. Generating plot...")

    #################
    # Plotting time #
    #################
    
    if(df1.empty):
        print("At date " + date + ", ticker" + ticker + " had no quote data\n")
    if(df2.empty):
        print("At date " + date + ", ticker" + ticker + " had no trade data\n")
        return

    fig, ax = plt.subplots(figsize=(20,8))
    ax.plot(df1.Time, df1['Ask Size Dec'],color = "blue", linewidth = 1.0, 
            linestyle = '-', label = 'Ask Volume')
    ax.plot(df1.Time, df1['Bid Size Dec'],color = "red", linewidth = 1.0, 
            linestyle = '-', label = 'Bid Volume')
    ax.set_xlabel('Time (UTC)')
    ax.set_ylabel('Volume')
    title_date = df1.Time[len(df1) - 1].strftime('%b %-d, %Y')
    ax.set_title(ticker + " | " + "Volume | " + title_date)
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
    imgname = ticker + "_" + "quotes_" + "Volume" + filetype + "_" + date + ".png"
    fig.savefig(dirpath + imgname)

    print("Ticker", ticker, "at date", date, "finished in", 
          time() - init_tm, "seconds")

    
def yeda2(fileloc, filetype, ticker):
    init_tm = time()

    # Make dir
    fsplit = fileloc.split('_')
    date = fsplit[len(fsplit) - 1][:-4]
    os.chdir(str(pathlib.Path.home()) + "/workspace/")
    dirpath = "/space/common/workspace/phase2_output/program8_out/matplotlib/" + filetype + "/" + date + "/"
    pathlib.Path(dirpath).mkdir(parents=True, exist_ok=True)

    print("Getting data...")
    df = pf.get_tickerData(fileloc, filetype, ticker, "T")
    print("Got data. Generating plot...")

    #################
    # Plotting time #
    #################
    if(df.empty):
        print("At date " + date + ", ticker" + ticker + " had no trade data\n")
        return

    fig, ax = plt.subplots(figsize=(20,8))
    ax.plot(df.Time, df["Trade Price"], color = "red", linewidth = 1.0, 
            linestyle = '-')
    ax.set_xlabel('Time (UTC)')
    ax.set_ylabel('Price')

    title_date = df.Time[len(df) - 1].strftime('%b %-d, %Y')
    ax.set_title(ticker + " | " + "Trades | " + title_date)
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

    imgname = ticker + "_" + "trades_" + filetype + "_" + date + ".png"
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
    except IndexError:
        print("Program 3: Plot Bid and Ask Prices (aggregated)")
        print("Type 'list' to get a list of valid inputs")

        filetype = pf.get_validInput("Type A or B or C or D files: ", 4)
        date = pf.get_validInput("Enter Date in yyyymmdd: ", 0,
                                 filetype=filetype)
        ticker = pf.get_validInput("Enter One Ticker: ", 1)
        ticker = ticker[0]

        while True:
            option = input("Enter 'plotly' or 'matplotlib':")
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
        program8(fileloc, filetype, ticker)
        program82(fileloc, filetype, ticker)
    else:
        yeda8(fileloc, filetype, ticker)
        yeda2(fileloc, filetype, ticker)

