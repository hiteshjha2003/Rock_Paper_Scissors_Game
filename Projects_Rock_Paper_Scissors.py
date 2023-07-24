#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random
import time

rock = 1
paper = 2
scissors=3


names = {rock:"Rock" , paper: "Paper" , scissors:"Scissors"}
rules = {rock:scissors   ,paper : rock , scissors:paper}


player_score = 0
computer_score = 0



def start():
    print("Let's play the game of ROCK PAPER and SCISSORS")
    while game():
        pass
    scores()
    

def game():
    player = move()
    computer = random.randint(1,3)
    result(player , computer)
    return play_again()


def move():
    while True:
        print
        player = input("Rock = 1\n Paper = 2 \n Scissors = 3")
        try:
            player  = int(player)
            if player in(1,2,3):
                return player
        except ValueError:
            pass
        print("OOPs! I didn't understand that .Please Enter 1 ,2 , 3:")

        

def result(player , computer):
    print("1.....")
    time.sleep(0.5)
    print("2.....")
    time.sleep(0.5)
    print("3!")
    time.sleep(0.5)
    print("Computer throw {0}".format(names[computer]))
    global player_score  , computer_score
    if player == computer:
        print("Tie Game")
    else:
        if rules[player] == computer:
            print("Your victory has been assured:")
            player_score+=1
        else:
            print("The Computer laughs  as you  realise you have been defeated")
            computer_score +=1
    

    
    
def play_again():
    answer = input("Would you like to play again ? y/n:")
    if answer in ("y" , "Y" , "Yes" , "yes" , "of course" , "YES"):
        return answer
    else:
        print("Thank you very much for playing this game  , See you next time bbbyeeee!!!!!!!!!!")
        

        
def scores():
    global player_score  , computer_score
    print("High Scores:")
    print("Player:" , player_score)
    print("Computer:" , computer_score)

    
    
if  __name__ == '__main__':
    start()
    
    
    


# In[3]:


"""





CHATGPT Code :----------------->
    |
    |
    |
    |
    V
    
 """   


# In[ ]:


import random

def get_user_choice():
    while True:
        user_choice = input("Enter your choice (rock, paper, scissors): ").lower()
        if user_choice in ["rock", "paper", "scissors"]:
            return user_choice
        print("Invalid choice. Please choose again.")

def get_computer_choice():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif user_choice == "rock":
        return "You win!"if computer_choice == "scissors" else "Computer wins!"
    elif user_choice == "paper":
        return "You win!" if computer_choice == "rock" else "Computer wins!"
    elif user_choice == "scissors":
        return "You win!" if computer_choice == "paper" else "Computer wins!"

def play_game():
    print("Welcome to Rock, Paper, Scissors!")
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        print(f"\nYou chose: {user_choice}")
        print(f"Computer chose: {computer_choice}\n")
        print(determine_winner(user_choice, computer_choice))

        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    play_game()


# In[ ]:




