import random 

def roll():
    min_value = 1
    max_value = 6

    value = random.randint(1,6)

    return value

while True:
    players = input("How many players will be in the game (2-4)? ").lower()
    
    if players.isdigit():

        players = int(players)
         
        if 1 <= players >= 4 :
           print("the number of players must be between 2 and 4")
        
        else:    
            break
    
    else:
        print("Input a number")
        
max_score = 50

score = [0 for i in  range(players)] 
print(score)

counter = 0
round = 0

while True:
    for i in range(players):
        print("Player", str(i+1) + "'s Turn")
        counter += 1

        if counter%2 == 0:
            round += 1
            print("Round", round)
        else:
            print("Round", round)

        while True:
            action = input("Do you want to roll, hold or quit? ").lower()
        
            if action == "roll":

                value = roll()
                print("You rolled a", value)

                if value == 1:
                    score[i] = 0
                    print("You lost all your points")
                    break
                else:
                    score[i] += value
                    print("Congratulations,You have", score[i], "points,So far")

                    if score[i] >= max_score:
                        print("Player", str(i+1), "wins!")
                        print("Your total score is", score[i],"Player", str(i+1) + "has won the game!")

                        break
                    
            elif action == "hold":
                break

            elif action == "quit":
                quit()
            else:
                print("Invalid input")

