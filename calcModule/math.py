def math(x,y,z):
    if z == "m":
        answer = x * y
    if z == "a":
        answer = x + y
    if z == "s":
        answer = x - y
    if z == "d":
        answer = x/y
    if z == "e":
        answer = x ** y
    return(answer)

while True:
    input1 = input("Say m,a,s,d, or e for multiply, add, subtract, divide, or exponential form")
    print("Now input 2 integers")
    input2 = input("Input one number here")
    input3 = input("Input another number here")
    input2 = int(input2)
    input3 = int(input2)
    answer = math(input2,input3,input1)
    print(answer)

