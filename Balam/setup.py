import os
import re
from os.path import expanduser

''''
note: change path of os.walk to where your shortcut files are
note: to change name of your application for "open" + application command go to helpers file and open 
      setup_application.txt and change the name before the "=" sign to your preffered name, if your preffered 
      name contains whitespace, change whitespace to underscore.
note: make sure the names are in lowercase
note: to add additional apps, go to where your shortcut apps path is and copy the path and add to setup_application.txt.
note: follow the format in the setup_application.txt file
'''
# setup application
directory = os.getcwd()
home = expanduser("~")
path = rf"{directory}\helpers\setup_application.txt"

with open(path, 'w') as myfile:
    for root, dirs, files in os.walk(r'C:\ProgramData\Microsoft\Windows\Start Menu\Programs'):
        for file in files:
            if file.endswith(".lnk"):
                # make name for path
                file_name = ((os.path.basename(os.path.join(root, file)).split('.lnk'))[0])
                file_name = " ".join((re.sub(r'[^a-zA-Z.\s]', '', file_name)).split()).lower().replace(' ', '_')
                #write to text file
                myfile.write(f'{file_name}={os.path.join(root, file)}\n')

with open(path, 'a') as myfile:
    for root, dirs, files in os.walk(rf'{home}\AppData\Roaming\Microsoft\Windows\Start Menu\Programs'):
        for file in files:
            if file.endswith(".lnk"):
                # make name for path
                file_name = ((os.path.basename(os.path.join(root, file)).split('.lnk'))[0])
                file_name = " ".join((re.sub(r'[^a-zA-Z.\s]', '', file_name)).split()).lower().replace(' ', '_')
                #write to text file
                myfile.write(f'{file_name}={os.path.join(root, file)}\n')

path = os.system(f'sort {path} /o {path}')