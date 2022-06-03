import random
while True:
    user_action=input("Enter a choice (r for rock p for paper and s for scissors)")
    r=str("rock")
    p=str("paper")
    s=str("scissors")
    actions=["rock","paper","scissors"]
    comp_actions=random.choice(actions)
    print(f"\n PLAYER:''{user_action}, CPU: '' {comp_actions}.\n")
    if user_action==comp_actions:
     print("Both Players selected{user_action}. It is a tie ! ")
    elif user_action =="r":
        if comp_actions=="s":
            print("Rock smashes scissors ! You win")
        else:
            print("Paper Covers rock ! You lose")
    elif user_action =="p":
        if comp_actions=="r":
            print("Paper Covers rock ! You win")
        else:
            print("Scissors cuts paper ! You lose")
    elif user_action =="s":
        if comp_actions=="p":
            print("Scissors cuts paper ! You win")
        else:
            print("Rock smashes scissors ! You lose")
    elif user_action != "r"and user_action !="s" and user_action!="p":
        print("You have entered a wrong command")

    playagain=input("Play again? (y/n):")
    if playagain.lower() !="y":
         break