import os, glob, sys
import datetime 

class colors:
    OKGREEN = '\033[92m'
    MAGENTA = '\033[95m'
    RED = '\033[31m'
    ENDC = '\033[0m'

print(colors.MAGENTA+'[~] Specify the format you want to rename the files in: '+colors.ENDC)
print(colors.OKGREEN+'[/]'+colors.ENDC+' 1.Number-Text-Oldname '+colors.RED+'(e.g. 1.file.txt, 2.file.txt ...)'+colors.ENDC) 
print(colors.OKGREEN+'[/]'+colors.ENDC+' 2.Number-Only '+colors.RED+'(e.g. 1., 2. ...)'+colors.ENDC)
print(colors.OKGREEN+'[/]'+colors.ENDC+' 3.Date '+colors.RED+'(e.g. 2020-12-24, 2012-17-21 ...)\n'+colors.ENDC)
user_rename_type = int(input('Format: '))

global path, listfolders_path, renamed_file, source_file, filename

path = input(colors.MAGENTA+'[~]'+colors.ENDC+' Select your directory: ')+'/'
if os.path.isdir(path):
    listfolders_path  = os.listdir(path)
    for count, filename in enumerate(listfolders_path,1): 
        source_file = path+filename
        renamed_file_numbering = str(count)
        if user_rename_type == 1: 
            renamed_file_numbering = path+renamed_file_numbering+'.'+filename
            os.rename(source_file, renamed_file_numbering)
        elif user_rename_type == 2:
            renamed_file_numbering = path+renamed_file_numbering
            os.rename(source_file, renamed_file_numbering)

    if user_rename_type == 3:
        file_names = os.listdir(path)
        for file_name in file_names:
            old_file_path = os.path.join(path, file_name)
            date_taken =  datetime.datetime.today().strftime ('%d-%b-%Y')
            new_file_name = date_taken + file_name
            new_file_path = os.path.join(path, new_file_name)
            os.rename(old_file_path, new_file_path)
else:
    print("Not a valid directory")
    exit()