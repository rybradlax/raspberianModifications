#3
#!/usr/bin/
# class
class Calc:
    def mult(x, y):
        answer = x * y
        print("%s times %s is %s" % (x, y, answer))
        return
    m = mult
    def add(x, y):
        answer2 = x + y
        print("%s plus %s is %s" % (x, y, answer2))
        return
    a = add
    def sub(x, y):
        answer3 = x - y
        print("%s minus %s is %s" % (x, y, answer3))
        return
    s = sub
    def div(x, y):
        answer4 = x/y
        print("%s divided by %s is %s" % (x, y, answer4))
        return
    d = div
 
