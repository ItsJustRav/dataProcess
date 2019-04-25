import time, sys
import numpy as np


def csvLoad(loadName, loadDelim, loadSkip):
       
       tikload = time.time()
       try:
              data = np.loadtxt(open(loadName, "rb"), delimiter = loadDelim, skiprows = loadSkip)
#              print(data)
              print("Memory used by array: ", data.nbytes/1024, " KB")

       except Exception as e:
              er = "Error Occurred: "+ str(e)
              print(er)

       print("Listing completed")
       tokload = time.time()
       print("Time elapsed for loading (sec): ", tokload-tikload)
       return data


def csvSave(saveName, saveData, saveDelim, saveHeader):
      
       tiksave = time.time()
       try:
              np.savetxt(saveName, saveData, delimiter=saveDelim, header = saveHeader)

       except Exception as e:
              er = "Error Occurred: "+ str(e)
              print(er)

       print("Saving completed")
       toksave = time.time()
       print("Time elapsed for saving (sec): ", toksave-tiksave)


if __name__== '__main__':

        loadName = "Block1.xls"
        loadDelim = "\t"
        loadSkip = 17
        print("Data file name: ", loadName)
        a = csvLoad(loadName, loadDelim, loadSkip)
        saveName = "test.csv"
        saveData = a
        saveDelim = ","
        saveHeader = "Header"
        csvSave(saveName, saveData, saveDelim, saveHeader)
        print("Data saved as: ", saveName)

