import pandas as pd
from itertools import repeat
import pathlib
import os
import sys
from datetime import datetime
from time import time
import projfuncs as pf
import projLists

def set_numbers(dft, dfq, df, tcols, qcols, size, ticker,region,contributors, filetype):
    if (filetype == "A"):
        CI = "<CONTRIBUTOR.ID>"
        RC = "<REGION.CODE>"
    if (filetype == "B"):
        CI = "<CONTRIBUTOR.ID>"
        RC = "<REGION.CODE>"
    if (filetype == "C"):
        CI = "<PART.CODE>"
        RC ="<RNR.END.EXCH.SEQ>"
    if (filetype == "D"):
        CI = "<PART.CODE>"
        RC = "<RNR.END.EXCH.SEQ>"
    dft = pd.DataFrame(dft, columns=tcols)                    
    dft[size] = dft[size].apply(pd.to_numeric, errors='ignore')
    dft[size] = dft[size].fillna(0)
    dfq = pd.DataFrame(dfq, columns=qcols)    
    region.extend(list(dft[RC].unique()))
    region.extend(list(dfq[RC].unique()))
    contributors.extend(list(dft[CI].unique()))
    contributors.extend(list(dfq[CI].unique()))
    df.at[ticker,"Q-ALL"] = dfq.shape[0]
    df.at[ticker,"T-ALL"] = dft.shape[0]
    if dft.empty:
        df.at[ticker,"V-ALL"] = 0.0
    else:
        df.at[ticker,"V-ALL"] = dft[size].sum()
    for param in [RC,CI]:                   
        tgroupby = dft[[size,param]].groupby(param).agg(["sum","count"])
        qgroupby = dfq[[qcols[0],param]].groupby(param).agg("count")
        l1 = list(qgroupby.index);l2 = list(tgroupby.index)
        l1.extend(l2)
        l3 = list(set(l1))
        l1 = list(qgroupby.index)
        for contributor in l3:
            if contributor not in l1:
                df.at[ticker, "Q-"+contributor] = 0
                df.at[ticker, "T-"+contributor] = tgroupby[size].at[contributor, "count"]
                df.at[ticker, "V-"+contributor] = tgroupby[size].at[contributor, "sum"]                
            elif contributor not in l2:
                df.at[ticker, "Q-"+contributor] = qgroupby[qcols[0]].at[contributor]
                df.at[ticker, "T-"+contributor] = 0
                df.at[ticker, "V-"+contributor] = 0
            else:
                df.at[ticker, "Q-"+contributor] = qgroupby[qcols[0]].at[contributor]
                df.at[ticker, "T-"+contributor] = tgroupby[size].at[contributor, "count"]
                df.at[ticker, "V-"+contributor] = tgroupby[size].at[contributor, "sum"]

def qtvcounts(fileloc, filetype):
    if (filetype == "B"):
        size = '<TRADE.SIZE.DEC>'
    else:
        size = "<TRADE.SIZE>"
    dfq = []; dft = [];region = [];contributors = [];col = []
    i = 0
    df = pd.DataFrame()
    with open(fileloc, "r") as f:
        for line in f:
            if (line.startswith('#D=Q')):
                qcols = line.strip('\n').split('|')
                i = i+1
            if (line.startswith('#D=T')):
                tcols =  line.strip('\n').split('|')
                i = i+1
            if (i==2):
                break
        for line in f:
            if (line.startswith("H")):
                if (len(dft) == 0)&(len(dfq)==0):
                    ticker = line.split("|")[2]
                    continue
                else:
                    init_tm = time()
                    set_numbers(dft,dfq,df,tcols, qcols, size, ticker,region,contributors,filetype)
                    print(ticker, "made in", time() - init_tm, "seconds" )
                    ticker = line.split("|")[2]
                    dfq = []; dft = []
            if (line.startswith("T")):
                dft.append(line.strip('\n').split('|'))
            if (line.startswith("Q")):
                dfq.append(line.strip('\n').split('|'))
    set_numbers(dft, dfq, df, tcols, qcols, size, ticker,region,contributors,filetype)
    region = list(set(region));contributors = list(set(contributors))
    region.extend(contributors)
    l = ["ALL"] + region
    for i in range(len(l)):
        col.append("Q-"+l[i])
        col.append("T-"+l[i])
        col.append("V-"+l[i])
    df = df[col]
    return df

if __name__ == "__main__":
    try:
        filetype, date = sys.argv[1], sys.argv[2]
    except IndexError:
        filetype = pf.get_validInput("Type A or B or C or D files: ", 4)
        date = pf.get_validInput("Enter Date in yyyymmdd: ", 0,
                                filetype=filetype)

    if (filetype == "A"):
                fileloc = "/space/data/new/PLUSTICK_1619_" + date + ".txt"
    if (filetype == "B"):
                fileloc = "/space/data/new/PLUSTICK_FI_1356_" + date + ".txt"
    if (filetype == "C"):
                fileloc = "/space/data/new/PLUSTICK_FUTURES_666_" + date + ".txt"
    if (filetype == "D"):
                fileloc = "/space/data/new/PLUSTICK_FUTURES_680_" + date + ".txt"
    os.chdir(str(pathlib.Path.home()) + "/workspace/")
    dirpath = "/space/common/workspace/phase1_output/program4_out/" + filetype + "/"
    pathlib.Path(dirpath).mkdir(parents=True, exist_ok=True)

    init_tm = time()
    df = qtvcounts(fileloc, filetype)
    df.to_csv(dirpath + "program4_out_" + filetype + "_" + date + ".csv")
    print("csv made in", time() - init_tm, "seconds")
    '''
    df = qtvcounts("/space/data/new/PLUSTICK_1619_20180420.txt", "A")
    df.to_csv("~/pworkspace/test.csv")
    '''
