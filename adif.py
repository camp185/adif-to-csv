##########CONVERT ADI HAM RADIO LOG FILES FROM QRZ TO CSV##########
import csv
import re
from datetime import date

#GET FILE DATA
#enter filename/location: C:Temp\KM6HBH@K-0207-20220620.adi
importFile = input('Enter location of adi file:')
adif = open(importFile, 'r')
logLines = adif.readlines()

##########SETUP LISTS AND NAME OF FILE TO SAVE##########
##########SAVES IN SAME FOLDER AS THIS CODE##########
header = []
data = []
headerRow = []
dataRow = []

tempLogLines = ""
writeTo = "ADIF_to_CSV_" + str(date.today())
print("Saving file as: " + writeTo + ".csv")
writeTo = writeTo + ".csv"

##########START THE BUILD##########
#open the file
f = open(writeTo, 'w', newline='')
writer = csv.writer(f)

# print(logLines)
#do a quick cleanup of the log and figure out which line to start after header info,
for x in range(len(logLines)):
    logLines[x] = logLines[x].strip()
    logLines[x] = logLines[x].replace("\t", "")
    logLines[x] = logLines[x].replace("\n", "")
    
tempLines = []  
for x in range(len(logLines)):
    findTags = re.findall('<[^<]*?>', logLines[x])

    for y in range(len(findTags)):
        logLines[x] = logLines[x].replace(findTags[y], "<<" + findTags[y])
    newLines = logLines[x].split("<<")
    if len(newLines) > 0:
        for z in range(len(newLines)):
            tempLines.append(newLines[z])

logLines = tempLines
while("" in logLines):
    logLines.remove("")
# for y in logLines:
    # print(y)
# print(len(logLines))
print(logLines)


fstart = 0
for x in range(len(logLines)):
    test = (str(logLines[x])).lower().find("<eoh>")
    if test != -1:
        fstart = x + 1
        x = len(logLines) + 1

#build header (aka first row), have to cycle through all the lines to make sure all fields are picked up
for x in range(fstart, len(logLines)):
    if (str(logLines[x])).lower() != "<eor>":
        logLines[x] = logLines[x].split(":")
        logLines[x][0] = logLines[x][0].replace("<", "")
        if logLines[x][0] not in headerRow:
            headerRow.append(logLines[x][0])
headerRow.sort()
header.append(headerRow)

#build rows, and add to data to matching column
for x in range(fstart, len(logLines)):
    if (str(logLines[x])).lower() != "<eor>":
        #search which column to add it to.
        for z in range(len(headerRow)):
            test = str(logLines[x]).find(headerRow[z])
            if test == 2:
                #if found, then extract data/split at >
                print(logLines[x])
                logLines[x] = str(logLines[x]).split(">")[-1]
                logLines[x] = logLines[x].replace("']", "")
                dataRow.insert(z,logLines[x])
            else:
                dataRow.append("")
    if (str(logLines[x])).lower() == "<eor>":
        data.append(dataRow)
        dataRow = []
        
print("Rows added:")
print(len(data))

#write the header
writer.writerow(header[0])

#write the data
for x in range(len(data)):
    writer.writerow(data[x])

# close the file
f.close()
##########TADA##########
