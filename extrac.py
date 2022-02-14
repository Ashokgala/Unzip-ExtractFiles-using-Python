# import os
# import shutil

# source_folder = r"D:\ashok\test\test\dacx\var\ameyo\dacxdata\voicelogs\DefaultCC\2022-01-27\biradar.kishan@theporter.in\\"
# destination_folder = r'D:\ashok\test\files\\'

# # fetch all files
# for file_name in os.listdir(source_folder):
#     # construct full file path
#     source = source_folder + file_name
#     destination = destination_folder + file_name
#     # copy only files
#     if os.path.isfile(source):
#         shutil.copy(source, destination)
#         print('copied', file_name)

import os
import shutil
RootDir1 = r'C:\Users\Administrator\Downloads\\'
TargetFolder = r'C:\Users\Administrator\Convin\\'
for root, dirs, files in os.walk((os.path.normpath(RootDir1)), topdown=False):
        for name in files:
            if name.endswith('.wav'):
                print("Found !")
                SourceFolder = os.path.join(root,name)
                shutil.copy2(SourceFolder, TargetFolder)

            else:
                print("File not found")




    