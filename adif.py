##########CONVERT ADI HAM RADIO LOG FILES FROM QRZ TO CSV##########
import csv
import re
from datetime import date
#for prorgess bar
import sys
import os
import time

############GET FILE DATA############
#enter filename/location: C:Temp\KM6HBH@K-0207-20220620.adi
print("Example: C:\Temp\KM6HBH@K-0207-20220620.adi")
importFile = input('Enter location of the adi file:')
adif = open(importFile, 'r')
logLines = adif.readlines()

##########SETUP LISTS AND NAME OF FILE TO SAVE##########
##########SAVES IN SAME FOLDER AS THIS CODE##########
header = []
data = []
headerRow = []
dataRow = []
tempLines = []
tempQso = []

writeTo = "ADIF_to_CSV_" + str(date.today())
print("Saving file to: " + writeTo + ".csv")
writeTo = writeTo + ".csv"

##########START THE BUILD##########
#open the file
f = open(writeTo, 'w', newline='')
writer = csv.writer(f)

#do a quick cleanup of the log and figure out which line to start after header info,
for x in range(len(logLines)):
    logLines[x] = logLines[x].strip()
    logLines[x] = logLines[x].replace("\t", "")
    logLines[x] = logLines[x].replace("\n", "")
 
    
#Go through all lines, and slit/append new ones where multiple tags found on one line.
#show progress
animation = ["[■□□□□□□□□□]","[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]", "[■■■■■□□□□□]", "[■■■■■■□□□□]", "[■■■■■■■□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■□]", "[■■■■■■■■■■]"]
# for i in range(len(animation)):
    # time.sleep(0.2)
    # sys.stdout.write("\r" + animation[i % len(animation)])
    # sys.stdout.flush()
# print("\n")
print("Loading:")

for x in range(len(logLines)):
    #add your own fields in comments or notes by using (()) to create the field
    logLines[x] = logLines[x].replace("((", "Xtra Field <")    
    logLines[x] = logLines[x].replace("))", ":>")
    #find the tags
    findTags = re.findall('<[^<]*?>', logLines[x])
    for y in range(len(findTags)):
        logLines[x] = logLines[x].replace(findTags[y], "<<" + findTags[y])
    newLines = logLines[x].split("<<")
    if len(newLines) > 0:
        for z in range(len(newLines)):
            tempLines.append(newLines[z])


    sys.stdout.write("\r" + animation[int(x/8000) % len(animation)])
    sys.stdout.flush()

  
logLines = tempLines
while("" in logLines):
    logLines.remove("")    

#find end of header
fstart = 0
for x in range(len(logLines)):
    test = (str(logLines[x])).lower().find("<eoh>")
    if test != -1:
        fstart = x + 1
        x = len(logLines) + 1


#build header (aka first row) and cycle through all the lines to make sure all fields are picked up
for x in range(fstart, len(logLines)):
    if (str(logLines[x])).lower() != "<eor>":
        logLines[x] = logLines[x].split(":")
        logLines[x][0] = logLines[x][0].replace("<", "")
        if logLines[x][0] not in headerRow:
            headerRow.append(logLines[x][0])
        sys.stdout.write("\r" + animation[int(x/4000) % len(animation)])
        sys.stdout.flush()    

headerRow.sort()
header.append(headerRow)


#build rows, and add to data to matching column
#row needs to be sorted to match header
tempQso = headerRow.copy()
for x in range(fstart, len(logLines)):
    
    if (str(logLines[x])).lower() != "<eor>":
        tester = 0
        #get rows in qso, sort in a tempQso
        for z in range(len(tempQso)):
            test = str(logLines[x]).find(str(tempQso[z]))
            if test == 2:
                tempQso[z] = str(logLines[x])
                    
                


    if (str(logLines[x])).lower() == "<eor>":
        #append to dataRow
        for y in range(len(tempQso)):
            qsoData = ""
            qsoData = qsoData + str(tempQso[y]).split(">")[-1]
            qsoData = qsoData.replace("']", "")
            dataRow.append(str(qsoData))
        # print(dataRow)  
        # print("______________________")
        data.append(dataRow)
        dataRow = []
        tempQso = headerRow.copy()

print("\n")
print("Rows added:")
print(len(data))

#write the header
writer.writerow(header[0])

#write the data
for x in range(len(data)):
    writer.writerow(data[x])

# close the file
f.close()
# give user time to close:
print("Saved file as: " + writeTo)
k=input("Press 'Enter' to open file and exit this applicaton") 
dir_path = os.path.dirname(os.path.realpath(__file__))
os.startfile(writeTo)

##########TADA##########