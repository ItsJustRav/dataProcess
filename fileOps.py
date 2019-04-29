import time, sys, os, traceback, inspect, logging
import numpy as np

def listDir(path):
       
       tikList = time.time()    
       try:
              f = open(os.path.join(path,"fileList.txt"), "a+")
              for root, dirs, files in os.walk(path):
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
       
def fileFilter(fileType, path, ifSave):

       try:
              title = "Filtered file list by file type: %s" % fileType
              print(title)
              f = open(os.path.join(path,"fileList.txt"), "r")
              filteredFiles = []
              end = fileType + "\n"
       
              for files in f:
                     if files.endswith(end):
                            filteredFiles.append(files.rstrip())
                                   
              if ifSave == "yes":
                     n = "fileteredList_%s.txt" % fileType
                     delim = ''
                     csvSave(n, filteredFiles, delim, title, "%s")

       
       except Exception as e:
              er = "Error Occurred: "+ str(e)
              print(e)
       
       return filteredFiles

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


def csvSave(saveName, saveData, saveDelim, saveHeader, dataFormat):
      
       tikSave = time.time()
       try:
              np.savetxt(saveName, saveData, delimiter=saveDelim, header = saveHeader, fmt=dataFormat)
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
       
       path= os.path.dirname(__file__)
       print("Current Directory: ", path)
       listDir(path)
       loadName = "/home/rav/Test/Block1.xls"
       loadDelim = "\t"
       loadSkip = 17
       a = csvLoad(loadName, loadDelim, loadSkip)
       saveName = "test.csv"
       saveData = a
       saveDelim = ","
       saveHeader = "Header"
       dataFormat = "%.5f"
       csvSave(saveName, saveData, saveDelim, saveHeader, dataFormat)
       fileType = ".xls"
       ifSave = "yes"
       fileFilter(fileType, path, ifSave)
       print("Complete")

