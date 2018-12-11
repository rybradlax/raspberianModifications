from time import sleep
import os

waitTime = 14400
while 2 > 1:
	os.system("sudo find file -type f -exec rm {} \; ")
    sleep(waitTime)      
