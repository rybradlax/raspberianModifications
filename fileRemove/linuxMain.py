from time import sleep
import os
from pathlib import Path
waitTime = 60 
p = Path('.')
# learn more abt python file running etc ok and fileDirectory = C:\Users\RyBradLax\Desktop\project\testing
# can make this a command for a terminal if made a function and file = input("Place file directory, and the file here:") becomes a parameter that is formatted, also allows more flexibility in usage yes.
file = input("Place file directory, and the file here:")
file2 = input("Place a directory you want all files within it removed:")
if os.path.isfile(file):
	os.system("sudo rm " + file)
else:
	print("TypeError: File not Found")
if os.path.isfile(file2):
	os.system("sudo find " + file2 + " -type f -exec rm {} \; ")
else:
	print("TypeError: File not Found")
