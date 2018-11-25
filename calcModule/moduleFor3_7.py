#3.6-3.7.1
#!/usr/bin/
# class
class Calc:
    def mult(x, y):
        answer = x * y
        print("{1}, times {2}, is {3}".format(x, y, answer))
        return
    m = mult
    def add(x, y):
        answer2 = x + y
        print("{1}, plus {2}, is {3}".format(x, y, answer2))
        return
    a = add
    def sub(x, y):
        answer3 = x - y
        print("{1}, minus {2}, is {3}".format(x, y, answer3))
        return
    s = sub
    def div(x, y):
        answer4 = x/y
        print("{1}, divided by {2}, is {3}".format(x, y, answer4))
        return
    d = div
