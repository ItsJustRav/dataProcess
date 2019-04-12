import os, traceback

def listDir(folder):
        
        f=open("fileList.txt", "a+")
        
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

        print("Complete")
        return

if __name__== '__main__':
        curDir= os.getcwd()
        print(curDir)
        listDir(curDir)
