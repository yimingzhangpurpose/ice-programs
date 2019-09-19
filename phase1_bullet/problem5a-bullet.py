# ###########################
# #    MTH 691 Program 5   ##
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
    dirpath = "/space/common/workspace/phase1_output/program5a_out/" + filetype + "/" + date + "/" + quotetype + "/"
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
    if (filetype == "A"):
        CI = "Contributor Id"
    if (filetype == "B"):
        CI = "Contributor Id"
    if (filetype == "C"):
        CI = "Part Code"
    if (filetype == "D"):
        CI = "Part Code"
    traces = []
    data[CI] = data[CI].fillna('un')
    for venue in data[CI].unique():
        trace = go.Scatter(x = data.Time[data[CI] == venue], 
                           y = data[quotetype + " Price"][data[CI] == venue],
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
    dirpath = "/space/common/workspace/phase1_output/program5a_out/" + filetype + "/" + date + "_" + quotetype + "/"
    pathlib.Path(dirpath).mkdir(parents=True, exist_ok=True)

    print("Getting data...")
    df = pf.get_tickerData(fileloc, filetype, ticker, "Q")
    print("Got data. Generating plot...")
    df["Time"] = pd.to_datetime(df["Time"])
    df = df.set_index("Time")
    dfgroupby = df[[quotetype + " Price", CI ]].groupby(CI)
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

# +
if __name__ == "__main__":
    print("Program 5a: Plot Bid or Ask Prices by Venue")

    TYPE = Bullet(
        prompt="\nPlease choose a filetype: ",
        choices=["A", "B", "C", "D"],
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

    filetype = TYPE.launch()

    print("You chose:", filetype)

    filetype = pf.get_validInput(filetype, 4)
    
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
    
    date = pf.get_validInput(date, 0,filetype=filetype)

    TICKER = Bullet(
        prompt="\nPlease choose a filetype: ",
        choices= projLists.ticker_list,
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

    QUOTETYPE = Bullet(
        prompt="\nPlease choose a filetype: ",
        choices= ["Bid", "Ask"],
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

    quotetype = QUOTETYPE.launch()     
    
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

