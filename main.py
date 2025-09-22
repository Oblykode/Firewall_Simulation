import random

def roll():
    Min_value = 1 
    Max_value= 6 
    roll = random.randint(Min_value , Max_value)

    return roll 

while True:
    Players = input("Enter the number of player you want 2 - 4: " )
    if Players.isdigit():
        Players = int(Players)
        if 2 <= Players <=4:
            break
        else:
            print("enter the number between 2 - 4: ")
    else :
        print("enter a valid number")

Max_scores = 50
Players_score = [0 for i in range(Players)]

while max(Players_score) < Max_scores:
    for i in range(Players):
        print("\n Player" , i + 1 ,"turn has just started \n")
        Current_score = 0 
        while True:
            Should_roll = input("do you want to roll ? ")
            if Should_roll.lower() != "y" :
                break 
            
            Value = roll()
            

            if Value == 1 :
                print("you rolled" , Value )
                print("your turn is done")
                break
            else :
                Current_score += Value
                print("you rolled a : ", Value )
            
            print("your current score is : " , Current_score)
        Players_score[i] += Current_score
        print("your current score is ; ",Players_score[i])
        break

Max_scores = max(Players_score)
winning_idx =  Players_score.index(Max_scores)
print("Player number" ,winning_idx +1 , "is the winner with a score of : " ,Max_scores)


    


