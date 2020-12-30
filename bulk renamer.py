#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import datetime
import re


class colors:

    OKGREEN = '\033[92m'
    MAGENTA = '\033[95m'
    RED = '\033[31m'
    ENDC = '\033[0m'
    YELLOW = "\033[93m"


print (colors.MAGENTA \
    + '[~] Specify the format you want to rename the files in: ' \
    + colors.ENDC)
print (colors.OKGREEN + '[/]' + colors.ENDC + ' 1.Number-Text-Oldname ' \
    + colors.YELLOW + '(e.g. 1.file.txt, 2.file.txt ...)' + colors.ENDC)
print (colors.OKGREEN + '[/]' + colors.ENDC + ' 2.Number-Only ' \
    + colors.YELLOW + '(e.g. 1., 2. ...)' + colors.ENDC)
print (colors.OKGREEN + '[/]' + colors.ENDC + ' 3.Date ' + colors.YELLOW \
    + '(e.g. 2020-12-24, 2012-17-21 ...)' + colors.ENDC)
print (colors.OKGREEN + '[/]' + colors.ENDC + ' 4.UPPERCASE ' \
    + colors.YELLOW + '(e.g. ROCKYOU.TXT, HELLO.JPG ...)' + colors.ENDC)
print (colors.OKGREEN + '[/]' + colors.ENDC + ' 5.lowercase ' \
    + colors.YELLOW + '(e.g. rockyou.txt, hello.jpg ...)' + colors.ENDC)
print (colors.OKGREEN + '[/]' + colors.ENDC + ' 6.Search/Replace ' \
    + colors.YELLOW + '(e.g. rockyou.txt --> lockyou.txt ...)\n' \
    + colors.ENDC)

user_rename_type = int(input('Format: '))

global path, listfolders_path, renamed_file, source_file, filename


def pathValid():
    path = os.path.normpath(input(colors.MAGENTA + '[~]' + colors.ENDC
                            + ' Select your directory: (press enter for current directory)')) + '/'
    if os.path.isdir(path):
        listfolders_path = os.listdir(path)
        for (count, filename) in enumerate(listfolders_path, 1):
            source_file = path + filename
            renamed_file_numbering = str(count)
            if user_rename_type == 1:
                renamed_file_numbering = path + renamed_file_numbering \
                    + '.' + filename
                os.rename(source_file, renamed_file_numbering)
            elif user_rename_type == 2:
                renamed_file_numbering = path + renamed_file_numbering
                os.rename(source_file, renamed_file_numbering)

        for file_name in listfolders_path:
            old_file_path = os.path.join(path, file_name)
            if user_rename_type == 3:
                date_taken = \
                    datetime.datetime.today().strftime('%d-%b-%Y')
                new_file_name = date_taken + ' ' + file_name
                new_file_path = os.path.join(path, new_file_name)
                os.rename(old_file_path, new_file_path)
            if user_rename_type == 4:
                new_file_name = file_name.upper()
                new_file_path = os.path.join(path, new_file_name)
                os.rename(old_file_path, new_file_path)
            if user_rename_type == 5:
                new_file_name = file_name.lower()
                new_file_path = os.path.join(path, new_file_name)
                os.rename(old_file_path, new_file_path)

        if user_rename_type == 6:
            userInput = input('Search the string you want to replace: ')
            replaceInput = \
                input('Replacement for the searched string: ')
            for file_searchreplace_name in listfolders_path:
                old_file_path = os.path.join(path,
                        file_searchreplace_name)
                new_file_name = \
                    file_searchreplace_name.replace(userInput,
                        replaceInput)
                new_file_path = os.path.join(path, new_file_name)
                os.rename(old_file_path, new_file_path)
    else:

        print ('Not a valid directory')
        pathValid()


pathValid()
