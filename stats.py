import time, sys, os, traceback, inspect
import numpy as np

def listDir(folder):
       
       tikList = time.time()    
       try:
              f=open(os.path.join(curDir,"fileList.txt"), "a+")
              for root, dirs, files in os.walk(folder):
                     for name in dirs:
                            f.write(str(os.path.join(root, name)) + "\n")
                     for name in files:
                            f.write(str(os.path.join(root, name)) + "\n")
       except Exception as e:
              er = "Error Occurred: "+ str(e)
              f.write(er + "\n")
              f.write(traceback.format_exc() + "\n")
              print(er)

       print("Listing completed")
       tokList = time.time()
       timer(tikList, tokList)
       return

def csvLoad(loadName, loadDelim, loadSkip):
       
       tikLoad = time.time()
       try:
              fileSize = round(os.path.getsize(loadName)/1048576, 2)
              print("Loading file: ", loadName, fileSize, "MB")
              data = np.loadtxt(open(loadName, "rb"), delimiter = loadDelim, skiprows = loadSkip)
              print("Memory used by array: ", round(data.nbytes/1048576, 3), " MB")

       except Exception as e:
              er = "Error Occurred: "+ str(e)
              print(er)

       print("Listing completed")
       tokLoad = time.time()
       timer(tikLoad, tokLoad)
       return data


def csvSave(saveName, saveData, saveDelim, saveHeader):
      
       tikSave = time.time()
       try:
              np.savetxt(saveName, saveData, delimiter=saveDelim, header = saveHeader)
              fileSize = round(os.path.getsize(saveName)/1048576, 3)
              print("Saved file: ", saveName, fileSize, "MB")
       except Exception as e:
              er = "Error Occurred: "+ str(e)
              print(er)
       tokSave = time.time()
       timer(tikSave, tokSave)

def timer(startTime, endTime):
       caller = inspect.stack()[1][3]
       print("Time elapsed (sec) for : ", caller, endTime-startTime)
       return

if __name__== '__main__':
       
       curDir= os.path.dirname(__file__)
       print("Current Directory: ", curDir)
       listDir(curDir)
       loadName = "F:\Test\Block1.xls"
       loadDelim = "\t"
       loadSkip = 17
       a = csvLoad(loadName, loadDelim, loadSkip)
       saveName = "test.csv"
       saveData = a
       saveDelim = ","
       saveHeader = "Header"
       csvSave(saveName, saveData, saveDelim, saveHeader)
       print("Complete")

