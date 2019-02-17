# Import the Necessary Packages
from random import randint
from random import choice
import time
import string

while True:
    x = choice(string.ascii_letters)
    y = "@"
    z = randint(1, 10)
    print(x)
    time.sleep(1)
    print(y)
    time.sleep(1)
    print(z)
    time.sleep(1)


