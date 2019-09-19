# For safety, but not needed
ticker_list = ["X:SXBTXRP", "X:SXBTUST", "X:SXBTCAD", "X:SXBTCNY", "X:SXBTEUR", 
               "X:SXBTJPY", "X:SXBTMXN", "X:SXBTGBP", "X:SXBTRUB", "X:SXBTSGD", 
               "X:SXBTUSD", "X:SETHXBT", "X:SETHUST", "X:SETHCAD", "X:SETHCNY", 
               "X:SETHEUR", "X:SETHGBP", "X:SETHJPY", "X:SETHMXN", "X:SETHUSD", 
               "X:SLTCXBT", "X:SLTCUST", "X:SLTCCNY", "X:SLTCEUR", "X:SLTCGBP", 
               "X:SLTCJPY", "X:SLTCMXN", "X:SLTCUSD", "X:SXRPXBT", "X:SXRPEUR", 
               "X:SXRPJPY", "X:SXRPMXN", "X:SXRPUSD", "X:SDAHXBT", "X:SDAHEUR", 
               "X:SDAHGBP", "X:SDAHUSD", "X:SBCHXBT", "X:SBCHETH", "X:SBCHUST", 
               "X:SBCHEUR", "X:SBCHJPY", "X:SBCHGBP", "X:SBCHUSD", ]

file_list = []

# Could consider writing a get_venueList function
venue_list = ["BBK", "BFX", "BMX", "BSO", "BST", "BTC", "BCC", "BDC", "CEX", 
              "CNK", "CFL", "CNO", "EXM", "GPX", "ITB", "OKC", "OKX", "TRK", 
              "UNC", "VLT", "ZAF", "CNB", "CTC", "IGML", "KKN"]

region_list = ["ASI", "EUR", "NAM"]

# ################################
# Column names for Type A files #
# ################################

typeA_Qcols = ['#D=Q', 'Tas Seq', 'Activity Datetime', 'Bid Price', 'Bid Size',
               'Ask Price', 'Ask Size', 'Quote Cond_1', 'Contributor Id',
               'Region Code', 'City Code', 'Quote Datetime',
               'Exch Message Timestamp']

typeA_Tcols = ['#D=T', 'Tas Seq', 'Activity Datetime', 'Trade Price',
               'Trade Size', 'Trade Cond_1', 'Contributor Id', 'Region Code',
               'City Code', 'Trade Datetime', 'Exch Message Timestamp',
               'Trade Cond_2', 'Trade Cond_3', 'Trade Official Time', 
               'Trade Cond_4', 'Trade Cond_5', 'Extended Trade Cond',
               'Trade Official Date', 'Retransmission Flag']

# Column names to remove from A

typeA_Qcols_rm = ['#D=Q', 'Tas Seq', 'Quote Cond_1', 'Quote Datetime', 
                  'Exch Message Timestamp']

typeA_Tcols_rm = ['#D=T', 'Tas Seq',  'Trade Cond_1', 'Trade Datetime', 
                  'Exch Message Timestamp', 'Trade Cond_2', 'Trade Cond_3',
                  'Trade Official Time', 'Trade Cond_4', 'Trade Cond_5', 
                  'Extended Trade Cond', 'Trade Official Date', 
                  'Retransmission Flag']

# ################################
# Column names for Type B files #
# ################################

typeB_Qcols = ['#D=Q', 'Tas Seq', 'Activity Datetime', 'Ask Price', 
               'Bid Price', 'Quote Datetime', 'Quote Official Time',
               'Exch Message Timestamp', 'Bid Size Dec', 'Ask Size Dec', 
               'Contributor Id', 'Quote Official Date', 'Region Code', 
               'City Code', 'Quote Cond_4']

typeB_Tcols = ['#D=T', 'Tas Seq', 'Activity Datetime', 'Trade Price', 
               'Trade Datetime', 'Exch Message Timestamp', 'Trade Size Dec',
               'Trade Vol Dec', 'Contributor Id', 'Trade Official Date',
               'Trade Official Time', 'Region Code', 'City Code', 
               'Retransmission Flag','Trade Contributor ID','Trade Region Code','Trade City Code']


# Column names to remove from B

typeB_Qcols_rm = ['#D=Q', 'Tas Seq', 'Quote Datetime', 'Quote Official Time',
               'Exch Message Timestamp', 'Quote Official Date', 'Quote Cond_4']

typeB_Tcols_rm = ['#D=T', 'Tas Seq', 'Trade Datetime', 'Exch Message Timestamp', 
                  'Trade Official Date', 'Trade Official Time', 
                  'Retransmission Flag']

# ################################
# Column names for Type C files #
# ################################

typeC_Qcols = ['#D=Q', 'Tas Seq','Rnr End Exch Seq', 'Activity Datetime', 'Bid Price', 'Bid Size',
               'Ask Price', 'Ask Size', 'Quote Cond_1', 'Part Code', 'Quote Datetime',
               'Exch Message Timestamp']

typeC_Tcols = ['#D=T', 'Tas Seq','Rnr End Exch Seq', 'Activity Datetime', 'Trade Price',
               'Trade Size', 'Trade Cond_1', 'Part Code', 'Vwap', 'Trade Datetime', 'Exch Message Timestamp',
               'Trade Cond_2', 'Trade Cond_3', 'Trade Official Time', 
               'Trade Cond_4', 'Trade Cond_5', 'Extended Trade Cond',
               'Trade Official Date', 'Retransmission Flag']

typeC_Bcols = ['#D=B', 'Tas Seq','Rnr End Exch Seq', 'Activity Datetime', 'Bid Price', 'Bid Size','Bid Part Code',
               'Ask Price', 'Ask Size', 'Ask Part Code','Exch Message Timestamp']

# Column names to remove from C

typeC_Qcols_rm = ['#D=Q', 'Tas Seq','Rnr End Exch Seq', 'Quote Cond_1', 'Quote Datetime', 
                  'Exch Message Timestamp']

typeC_Tcols_rm = ['#D=T', 'Tas Seq','Rnr End Exch Seq', 'Trade Cond_1', 'Vwap', 'Trade Datetime', 
                  'Exch Message Timestamp', 'Trade Cond_2', 'Trade Cond_3',
                  'Trade Official Time', 'Trade Cond_4', 'Trade Cond_5', 
                  'Extended Trade Cond', 'Trade Official Date', 
                  'Retransmission Flag']

typeC_Bcols_rm = ['#D=B', 'Tas Seq', 'Rnr End Exch Seq', 'Exch Message Timestamp']

# ################################
# Column names for Type D files #
# ################################

typeD_Qcols = ['#D=Q', 'Tas Seq','Rnr End Exch Seq', 'Activity Datetime', 'Bid Price', 'Bid Size',
               'Ask Price', 'Ask Size', 'Quote Cond_1', 'Part Code', 'Quote Datetime',
               'Exch Message Timestamp']

typeD_Tcols = ['#D=T', 'Tas Seq','Rnr End Exch Seq', 'Activity Datetime', 'Trade Price',
               'Trade Size', 'Trade Cond_1', 'Part Code', 'Vwap', 'Trade Datetime', 'Exch Message Timestamp',
               'Trade Cond_2', 'Trade Cond_3', 'Trade Official Time', 
               'Trade Cond_4', 'Trade Cond_5', 'Extended Trade Cond',
               'Trade Official Date', 'Retransmission Flag']

typeD_Bcols = ['#D=B', 'Tas Seq','Rnr End Exch Seq', 'Activity Datetime', 'Bid Price', 'Bid Size','Bid Part Code',
               'Ask Price', 'Ask Size', 'Ask Part Code','Exch Message Timestamp']

# Column names to remove from D

typeD_Qcols_rm = ['#D=Q', 'Tas Seq','Rnr End Exch Seq', 'Quote Cond_1', 'Quote Datetime', 
                  'Exch Message Timestamp']

typeD_Tcols_rm = ['#D=T', 'Tas Seq','Rnr End Exch Seq', 'Trade Cond_1', 'Vwap', 'Trade Datetime', 
                  'Exch Message Timestamp', 'Trade Cond_2', 'Trade Cond_3',
                  'Trade Official Time', 'Trade Cond_4', 'Trade Cond_5', 
                  'Extended Trade Cond', 'Trade Official Date', 
                  'Retransmission Flag']

typeD_Bcols_rm = ['#D=B', 'Tas Seq', 'Rnr End Exch Seq', 'Exch Message Timestamp']

# file_list = glob("data/PLUSTICK_FI_1356_*") #Might not need sorted()

# For type A files
# file_list = sorted(glob("data/PLUSTICK_1619_*")) #Might not need sorted()

# For Type A files
# venue_list = ["CNB", "CTC", "IGML", "KKN", "ALL"]

# For Type B files
# region_list = ["NAM", "EUR", "ALL"]

list_666 =["F2:XBT\\F19","F2:XBT\\G19","F2:XBT\\J19","F2:XBT\\H19"]
list_680 =["F2:XBT\\H20","F2:XBT\\H19","F2:XBT\\M19","F2:XBT\\U19","F2:XBT\\Z19",
            "F2:BTC\\J19","F2:BTC\\F19","F2:BTC\\M19","F2:BTC\\H19","F2:BTC\\G19"]
