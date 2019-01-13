print("Welcome to Guess the Word! Write all words and letters as lowercase, and no numbers or symbols.")
while True:
    var1 = input("Input word for Scrabble game ")
    for letter in var1:
        print(letter)
    list1 = list(var1)
    tup1 = ("a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z")
    var2 = input("Would you like to solve the word or input letters? (l/w)(Letters are a work in progress, please only do word) ")
    if var2 == "w":
        var3 = input("Guess the word! ")
        if var3 == (var1):
                print("Correct Word!")
        else:
                print("Incorrect word!")
                var2 = input("Would you like to solve the word or input letters? (l/w) ")
    elif var2 == "l":
        var4 = input("Guess a letter! ")
        if var4 == list1:
            print("Correct letter!")
            var2 = input("Would you like to solve the word or input letters? (l/w) ")
        else:
            print("Incorrect letter!")
            var2 = input("Would you like to solve the word or input letters? (l/w) ")
