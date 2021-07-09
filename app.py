print("Welcome to my demo game")
name = input("What is your name? ")
age = int(input("What is your age? "))

print("Hello ",  name,  " you are ",  age,  " years old.")

health = 10

if age >= 18:
    print("You are old enough to play this game!")

    want_to_play = input("Do you want to play? ").lower()
    if want_to_play == "yes":
        print("Let's play!")
        print("You are starting with", health, "health.")
        left_or_right = input("First choice... Left or Right (left/right)? ").lower()
        if left_or_right == "left":
            ans = input("Nice, you follow the path and reach a lake... "
                        "Do you swim across or go around (across/around)? ").lower()
            if ans == "around":
                print("You went around and reached the other side of the lake.")
            elif ans == "across":
                print("You managed to get across the lake but were bit by a fish and lost 5 health.")
                health -= 5
                print("You currently have", health, "health")

            ans = input("You notice a house and a river."
                        "Which one do you head towards? (river/house)? ")
            if ans == "house":
                print("You enter the house and attacked by the owner. You lose 5 health")
                health -= 5
                print("You currently have", health, "health")

                if health <= 0:
                    print("You currently have 0 health... you lost the game")
                else:
                    print("You manage to run away and head towards a hill.")
                    print("You sit on top of the hill... you win the game.")
            elif ans == "river":
                print("You fell in the river and lost...")
        else:
            print("You fell down and lost...")

    else:
        print("Come back and play next time!")
else:
    print("You aren't old enough to play this game...")