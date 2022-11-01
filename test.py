import os

list_directory = os.listdir('.')
filelists = []
for directory in list_directory:
    # os.path 模块稍后会讲到
    if(os.path.isfile(directory)):
        filelists.append(directory)
