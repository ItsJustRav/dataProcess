import os, traceback, time

def listDir(folder):
        
        f=open(os.path.join(curDir,"fileList.txt"), "a+")
        
        try:
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
        return

if __name__== '__main__':

        tik = time.time()
        curDir= os.path.dirname(__file__)
        print("Current Directory: ", curDir)
        listDir(curDir)
        tok = time.time()
        print("Time Elapsed (sec): ", tok-tik)
