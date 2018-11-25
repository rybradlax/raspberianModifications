import usr_passw
import os
try:
	usr_passw.list
	print("Login to your Blados account!")
	os.system("python login.py")
except AttributeError:
	print("Oh no! You do not have a Blados account, make one here!")
	os.system("python username_passw.py")