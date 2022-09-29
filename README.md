# adif-to-csv
  Convert ADIF files from:  LoTW, QRZ, HAMRS, MacLoggerDX, WINLOG32, N3FJP's Amateur Contact Log, plus various others to CSV using Python.
  Author: Robert Campbell, camp185@gmail.com, KM6HBH

Requirements: 
  Python and a log file in adif format: logname.adi

To Run: 
  Save adif.py locally. 
  Run, fill prompt by entering location of adi file, example: C:\Users\km6hbh\Downloads\km6hbh-log.adi
  A CSV file will be created titled: ADIF_to_CSV_YYYY_MM_DD.csv
  File is saved in the same folder/location as adif.py.
  
  Run times are dependent on details of your log. LoTW log (24 fields) with 500 contacts, a 2-3 seconds. QRZ log (50 fields) with 500 contacts, 15 seconds.
