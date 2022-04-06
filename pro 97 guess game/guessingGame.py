import random
number=random.randint(1,9)
print("Number guessing game")
chances =0
print("Guess a number between 1-9")
while chances < 5:
    guess = int(input("Enter your guess:-"))

    if guess==number:
        print("Congratulations YOU WON!!")
        break
    elif guess < number :
        print("Your guess was too low:Guess a number higher than ",guess)

    else:
        print("your guess was too high :Guess the number lower than",guess)

    chances +=1
if not chances < 5:
    print("you losse !!!!! the number is",number)                