usr = input("What will your username be?")
passw = input("What will your password be?")
usr_pass = [usr, passw]
file = open("usr_passw.py", "w")
file.write("list = %s" % (usr_pass))
file.close()
