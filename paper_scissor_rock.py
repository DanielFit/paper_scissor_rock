import random
import time


print ("\n Hello and welcome to paper, scissor, rock!\n")
name = input("Enter your name: ")
print("Hello " + name + "! Best of Luck!")
time.sleep(2)
print("The game is about to start!\n Let's play paper, scissor, rock!!")
time.sleep(3)

def main():
    global choices
    global opposition
    global display
    global play_game
choices = ["paper", "scissor", "rock"]
opposition = random.choice(choices)
display = '[] 8< O'
play_game = ""


def play_loop():
    global play_game
    play_game = input("Do You want to play again? y = yes, n = no \n")
    while play_game not in ["y", "n", "Y", "N"]:
        play_game = input("Do You want to play again? y = yes, n = no \n")
    if play_game == "y":
        main()
    elif play_game == "n":
        print("Thanks For Playing! We expect you back again!")
        exit()


play_game= input("Do You want to play again? y = yes, n = no \n")

while play_game not in ["y", "n","Y","N"]:
        play_game = input("Do You want to play again? y = yes, n = no \n")
        if play_game == "y":
         main()

        elif play_game == "n":
         print("Thanks For Playing! We expect you back again!")
        exit()

def paper_scissor_rock():
 global play_game
decission = input("choose from paper, scissor or rock: " + display + " Enter your decission: \n")

if decission == opposition:
    print ("draw")
    play_loop()

if decission == "paper":
    if opposition == "scissor":
        print(" oh no! scissor beats paper, try again")
        play_loop()
    elif opposition == "rock":
            print(" Awesome! paper beats rock, you win")
    play_loop()


if decission == "rock":
    if opposition == "paper":
        print(" oh no! paper beats rock, try again")
        play_loop()
    elif opposition == "scissor":
            print(" Awesome! rock beats scissor, you win")
    play_loop()


if decission == "scissor":
    if opposition == "rock":
        print(" oh no! rock beats scissor, try again")
        play_loop()
    elif opposition == "paper":
            print(" Awesome! scissor beats paper, you win")
    play_loop()


main()
paper_scissor_rock()








