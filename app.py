print("Welcome to my demo game")
name = input("What is your name? ")
age = int(input("What is your age? "))

print("Hello ",  name,  " you are ",  age,  " years old.")

if age >= 18:
    print("You are old enough to play this game!")

    want_to_play = input("Do you want to play? ")
    if want_to_play == "yes":
        print("Let's play!")
    else:
        print("Come back and play next time!")
else:
    print("You aren't old enough to play this game...")