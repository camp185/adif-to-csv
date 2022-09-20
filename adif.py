import csv
from datetime import date
importFile = input('Enter location of adi file:')
# importFile = 'km6hbh.168644.20220404042222.adi'

adif = open(importFile, 'r')
logLines = adif.readlines()
header = []
data = []
headerRow = []
dataRow = []
print(len(logLines))
writeTo = str(date.today())
print("Saving file as: " + writeTo + ".csv")
writeTo = writeTo + ".csv"
# open the file in the write mode
f = open(writeTo, 'w', newline='')
writer = csv.writer(f)

#do a quick cleanup and figure out which line to start
for x in range(len(logLines)):
    logLines[x] = logLines[x].strip()
fstart = 0
for x in range(len(logLines)):
    test = str(logLines[x]).find("<eoh>")
    if test != -1:
        fstart = x
        x = len(logLines) + 1
           
        
    
#build header, have to cycle through all the lines to make sure all fields are picked up
for x in range(fstart, len(logLines)):
    if logLines[x] != "<eor>" and logLines[x] != "":
        logLines[x] = logLines[x].split(":")
        logLines[x][0] = logLines[x][0].replace("<", "")
        if logLines[x][0] not in headerRow:
            headerRow.append(logLines[x][0])
headerRow.sort() 
header.append(headerRow)

# x = txt.find("welcomes")
# list.insert(position, element)

#build rows, and add to data to matching column
for x in range(fstart, len(logLines)):
    if logLines[x] != "<eor>" and logLines[x] != "":
        #search which column to add it to.
        for z in range(len(headerRow)):
            test = str(logLines[x]).find(headerRow[z])
            # if test > -1:
            if test == 2:
                #if found, then extract data/split at >
                logLines[x] = str(logLines[x]).split(">")[-1]
                logLines[x] = logLines[x].replace("']", "")
                dataRow.insert(z,logLines[x])
            else:
                dataRow.append("")
            
    if logLines[x] == "<eor>":
        data.append(dataRow)
        dataRow = []

print(len(data))

# write the header
writer.writerow(header[0])

#write the data
for x in range(len(data)):
    writer.writerow(data[x])

# write the data

# close the file
f.close()
