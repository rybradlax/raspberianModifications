import usr_passw
login = input("Username:")
if login == usr_passw.list[0]:
    print("Correct username")
    login2 = input("Password:")
    if login2 == usr_passw.list[1]:
        print("Correct Password")
        print("Welcome to your Blados account")
        import sys
        import time

        def spinning_cursor():
            while True:
                for cursor in '|/-\\':
                    yield cursor

        spinner = spinning_cursor()
        for _ in range(50):
           sys.stdout.write(next(spinner))
           sys.stdout.flush()
           time.sleep(0.1)
           sys.stdout.write('\b')
    else:
        ("Incorrect password")
else:
    print("Incorrect username")
