# Rock-Paper-Scissor Game

import random
name=input("Enter your name: ")
print("Lets Start the game :",name)
print("you have 5 chance  only  : ")

words=['R','r','P','p','S','s']


while(True):
    com_point=0
    player_point=0
    i=0
    while(i<5):
        user=input("    Choose Rock(R) / Paper(P) / Scissors(S) :  ")
        word= random.choice(words)
        print("Computer choice: ",word)
        if(((user=='R' or user=='r') and (word=='s' or word=='S'))or ((user=='s' or user=='S') and (word=='p' or word=='P')) or ((user=='p' or user=='P') and (word=='r' or word=='R'))):
            player_point+=1
        elif(user==word):
            continue
        else:
            com_point+=1
        i+=1
    print("your score: ",player_point)
    print("computer score: ",com_point)
    if(player_point>com_point):
        print(name,"win")
    else:
        print(name,"loose")
    if(input("press 'c' to continue: ")not in('cC')):
        break
    
        
    

