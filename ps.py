import random

while True:
    print("Welcome to Rock, Paper and Scissors.")
    choice= input("What'd you choose? Type 'quit' if you don't want to play: ").lower()

    c_opt = ['rock','paper','scissors']
    c_choice = random.choice(c_opt)

    c_pri = print("The computer chose", c_choice)

    if choice == c_choice:
        print ("Tie.")
        break
        
    elif choice == "rock" and c_choice == "paper":
        print ("The computer wins.\n")
        
    elif choice == "rock" and c_choice == "scissors":
        print("You win.\n")
        
    elif choice == "paper" and c_choice == "scissors":
        print("The computer wins.\n")
    
    elif choice == "paper" and c_choice == "rock":
        print("You win.\n")
    
    elif choice == "scissors" and c_choice == "rock":
        print("The computer wins.\n")
    
    elif choice == "scissors" and c_choice == "paper":
        print("You win.\n")
        
    elif choice == "quit":
        print("Bye.")
        break    
        
    else:
        print("Invalid\n")