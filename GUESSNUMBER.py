""" TAKE A NUMBER BY GUESSING """
import random
print("SCORE OUT OF 100")
n = int(input("enter the last limit:"))
b = random.randint(0, n)
c = int(input("guess the number"))
s = 100

if b == c:
    print(b, "ANSWER IS CORRECT")
    print("score is ", s)
else:
    while(b != c):
        s = s-10
        if c > b:
            print("(HINT)your guess is larger than actual number try again")
            if b % 2 == 0:
                print("ANSWER is an even number")
            elif b % 2 != 0:
                print("ANSWER is an odd number")
        elif c < b:
            print("(HINT)your guess is smaller than the actual number try again ")
            if b % 2 == 0:
                print("ANSWER is an even number")
            elif b % 2 != 0:
                print(" is an odd number")
        print(f"INCORRECT ANSWER {c} ")
        print(f" (after marks reduction) CURRENT SCORE :{(s)}")
        c = int(input("enter the number again:"))
        if (b == c):
            print(b, "ANSWER IS CORRECT")
            print("final score is :", s, "SUCCESS")
            break
        if s == 0:
            print("SCORE IS ZERO ")
            break
