# ###########################
# #    MTH 691 Program X   ##
# ###########################

import pandas as pd
import plotly.offline as py
import plotly.graph_objs as go
import pathlib
from time import time
from glob import glob
import projfuncs as pf
import os
import sys
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import projLists

def ppppp6(fileloc, filetype, ticker):
    init_tm = time()

    # Make dir
    fsplit = fileloc.split('_')
    date = fsplit[len(fsplit) - 1][:-4]
    os.chdir(str(pathlib.Path.home()) + "/workspace/")
    dirpath = "phase1_output/program6_out/plotly/" + filetype + "/" + date + "/"
    pathlib.Path(dirpath).mkdir(parents=True, exist_ok=True)

    #print(ticker)
    data = pf.get_tickerData(fileloc, filetype, ticker, "T")
    #print("Got data. Generating plot...")

    #################
    # Plotting time #
    #################    
    if(data.empty):
        print(date + ", ticker " + ticker + " no trade data\n", file=txt)
        #data.write(date + ", ticker " + ticker + " no trade data\n")
        return
    else:
        print(date + ", ticker " + ticker + " no trade data\n", file=txt)
        #data.write(date + ", ticker " + ticker + " had trade data\n")
        return


# ##################
# # Main Function ##
# ##################

# +
if __name__ == "__main__":
    #try:
        #filetype = sys.argv[1]
        #date = sys.argv[3]
        #ticker = sys.argv[4]
        #option = sys.argv[4]
    #except IndexError:
        #print("Program 2: Plot Trade Prices (aggregated)")
        #print("Type 'list' to get a list of valid inputs")

        filetype = pf.get_validInput("Type C or D files: ", 4)
        #date = pf.get_validInput("Enter Date in yyyymmdd: ", 0,
                                # filetype=filetype)
        #ticker = pf.get_validInput("Enter F2:XBT or F2:BTC +\?19 Ticker: ", 1)
        #ticker = ticker[0]
        
        if (filetype == "A"):
            projLists.file_list = sorted(glob("/space/data/new/PLUSTICK_1619_*"))
        if (filetype == "B"):
            projLists.file_list = sorted(glob("/space/data/new/PLUSTICK_FI_1356_*"))
        if (filetype == "C"):
            projLists.file_list = sorted(glob("/space/data/new/PLUSTICK_FUTURES_666_*"))
            tickers = ["F2:XBT\F19","F2:XBT\G19","F2:XBT\J19","F2:XBT\H19"]
        if (filetype == "D"):
            projLists.file_list = sorted(glob("/space/data/new/PLUSTICK_FUTURES_680_*"))
            tickers = ["F2:XBT\H20","F2:XBT\H19","F2:XBT\M19",r"F2:XBT\U19","F2:XBT\Z19","F2:BTC\J19","F2:BTC\F19","F2:BTC\M19","F2:BTC\H19","F2:BTC\G19"]

        txt=open("../Test/data.txt",'w+') 

        
        for fileloc in projLists.file_list:
            with open(fileloc, 'r') as finput:
                for line in finput:
                    if (line.startswith("H")):
                        mylist = []
                        mylist.append(line.split('|')[2])
                        for ticker in tickers:
                            if (ticker in mylist):
                                ppppp6(fileloc, filetype, ticker)
        txt.close()
        
        
        
       # while True:
       #     option = input("Enter 'plotly' or 'matplotlib':")
        #    if (option in ['plotly', 'matplotlib']):
       #         break
       #     else:
       #         print("Invalid option")
        
        
        
        
        
    #if (filetype1 == "A"):
    #    fileloc1 = "/space/data/new/PLUSTICK_1619_" + date + ".txt"
    #if (filetype1 == "B"):
    #    fileloc1 = "/space/data/new/PLUSTICK_FI_1356_" + date + ".txt"
    #if (filetype2 == "C"):
    #    fileloc2 = "/space/data/new/PLUSTICK_FUTURES_666_" + date + ".txt"
    #if (filetype2 == "D"):
     #   fileloc2 = "/space/data/new/PLUSTICK_FUTURES_680_" + date + ".txt"
    #if (option == "plotly"):
    #    program6(fileloc1, fileloc2, filetype1, filetype2, ticker)
   # else:
     #   yeda6(fileloc1, fileloc2, filetype1, filetype2, ticker)
