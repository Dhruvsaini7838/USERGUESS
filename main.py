import random
randnumber = random.randint(1,100)
Userguess = None
guesses = 0
while (Userguess!=randnumber):
    Userguess=int(input("ENTER YOUR GUESS(B/W 1-100) : "))
    guesses +=1
    if (Userguess==randnumber):
        print("YOU GUESSED IT RIGHT")
    else:
        if(Userguess> randnumber):
            print("YOU GUESSED IT WRONG!  ENTER SMALLER NO:")
        else:
            print("YOU GUSESSED IT WRONG!  ENTER LARGER NO:")

print(f"YOU GUESSED THE NUMBER IN {guesses} GUESSES ")