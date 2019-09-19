library(data.table)
library(forecast)
library(tsoutliers)

args = commandArgs(trailingOnly = TRUE)

# 1 ticker
# 2 venue
# 3 option
# 4 date
# 5 dirpath
# 6 cval

ticker = args[1]
venue = args[2]
option = args[3]
date = args[4]
dirpath = args[5]
cval = as.numeric(args[6])

tempdir = paste(path.expand("~/workspace/"), "temp/tmp1.csv", sep = '')

df = fread(tempdir, data.table = F)
CTC = ts(df)

setwd(dirpath)

model = auto.arima(CTC)
resid = residuals(model)
pars = coefs2poly(model)
outliers = locate.outliers(resid, pars, types = c("AO", "IO"), cval = cval)
ao = outliers[outliers$type == "AO", "ind"]
io = outliers[outliers$type == "IO", "ind"]

title = paste(ticker, venue, option, date, "AO / IO", sep = ' | ')
png(paste(ticker, '_', venue, "_", toString(cval), ".png", sep = ''), width = 1028, height = 768)
plot(CTC, main = title, xlab = "Time Index", ylab = "Price")
points(ao, CTC[ao], col = 'red', pch = 20, cex = 1.25)
points(io, CTC[io], col = 'blue', pch = 20, cex = 1.25)

fname = paste(ticker, '_', venue, "_", toString(cval), ".csv", sep = '')
write.csv(outliers, fname, row.names = F)

sink(paste(ticker, '_', venue, "_", toString(cval), "_statistics.txt", sep = ''))
message = paste("Method: ARIMA Based",
                paste("Critical Value:", toString(cval)),
                paste("Number of outliers:", toString(nrow(outliers))),
                paste("Total number of observations:", toString(length(CTC))),
                paste("Percentage outliers:", toString(nrow(outliers) / length(CTC))), 
                sep = '\n')
cat(message)

