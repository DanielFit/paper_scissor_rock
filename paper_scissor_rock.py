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

if decission == "paper":
    if opposition == "scissor":
        print(" oh no! scissor beats paper, try again")
    elif opposition == "rock":
            print(" Awesome! paper beats rock, you win")


if decission == "rock":
    if opposition == "paper":
        print(" oh no! paper beats rock, try again")
    elif opposition == "scissor":
            print(" Awesome! rock beats scissor, you win")


if decission == "scissor":
    if opposition == "rock":
        print(" oh no! rock beats scissor, try again")
    elif opposition == "paper":
            print(" Awesome! scissor beats paper, you win")









