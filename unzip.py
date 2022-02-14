from itertools import count
from msilib.schema import Directory
import os
from pathlib import Path
from zipfile import ZipFile
import time
start = 0 
def main():
    try:


        zipfilelocation = Path( r"C:\Users\Administrator\Downloads")
        print(zipfilelocation.stem)
        print(zipfilelocation.is_file())


        count = 1
        fileSequence = 1
        if(count>=0):
            
            print(count)
            for file in os.listdir(zipfilelocation):
                try:
                    with ZipFile(file, 'r' ) as zipObj:
                        print("Extracting the files .. ")
                        zipObj.extractall(r'C:\Users\Administrator\extract\\')
                        print("File has been successfully extracted ! ")
                        # print(file.stem)
                        # # os.remove(zipfilelocation.stem)
                        # print("Zip File has been removed now. ")

                    count +=1
                    print(count)
                    time.sleep(4.0)

                    try:
                       
                        renamelocation = Path(r"C:\Users\Administrator\extract\\")
                        print(renamelocation.is_file())
                        print(renamelocation.is_dir())
                        print(renamelocation.suffix) 
                        print(renamelocation.stem)  
                        for file in renamelocation.iterdir():
                            print(file)
                            src = file
                            # print(src)
                            dst = 'Dacx' + str(fileSequence)
                            print(dst)
                            os.rename(src, dst)
                            time.sleep(4.0)
                            fileSequence +=1                  

                    except:

                        print("Unable to RENAME File Location")
                   


                except:
                    print("Unable to run the command unzip")
                    # print(file)
                    print(count)
                    count +=1
                    print(count)
                

        else:
            print("Unable to detect the files in the folder . ")
        
    except:
        print("Loop Ended") 
        main()
        

main()
