# adif-to-csv
  Convert ADIF files from:  LoTW, QRZ, HAMRS, MacLoggerDX, WINLOG32, N3FJP's Amateur Contact Log, plus various others to CSV using Python.
  Author: Robert Campbell, camp185@gmail.com, KM6HBH

Requirements: 
  A log file in adif format: logname.adi. Two ways to currently run. If you have Python installed, just run adif.py, otherwise Window users can run adif.exe.

To Run: 
  Save adif.py or adif.exe locally. 
  
  Note: the file adif.exe is currenlty missing credentilas so you will need to allow that to work.
  Fun Note: Create custom fields in your log book comments. Example, in QRZ I log a comment when making a POTA contact like ((POTA)) the park number. This conveter script will search the comments, and create an extra field called POTA, and then include the extar info after the field name. You could use it for anything like ((SOTA)) or ((ICOMS)) or whatever.
  
  To run, fill prompt by entering location of adi file, example: C:\Users\km6hbh\Downloads\km6hbh-log.adi
  A CSV file will be created titled: ADIF_to_CSV_YYYY_MM_DD.csv
  File is saved in the same folder/location as adif.py and will automatically open the csv file when you close/end application.
  
  Run times are dependent on details of your log. LoTW log (24 fields) with 500 contacts, a 2-3 seconds. QRZ log (50 fields) with 500 contacts, 15 seconds. 

  Troubleshooting: I recently rand this on my own QRZ log that has 4,500+ QSO. Error. I then just converted the file to ANSI, problem fixed. Notepad++ can easily do this for you.
