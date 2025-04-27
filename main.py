import random 

items_list = ["Rock", "Paper", "Scissor"]

def game_logic():
    user = input("\nEnter your Move(Rock, Paper, Scissor): ").capitalize()
    comp = random.choice(items_list)

    if user not in items_list:
        print(f"❌ Invalid Move! Please choose Rock, Paper, or Scissor.")

    else:
        print(f"\nFinal Result: ")
        print(f"👤 User's Move: {user}")
        print(f"💻 Computer's Move: {comp}")

        if user == comp:
            print("=>😅 Both Chooses Same: Match Tie")

        elif user == "Rock":
            if comp == "Paper":
                print("=>🥲 Paper covers Rock: Computer Win")
            else:
                print("=>😁 Rock smashes Scissor: User Win")

        elif user == "Paper":
            if comp == "Rock":
                print("=>😁 Paper covers Rock: User Win")
            else:
                print("=>🥲 Scissor cuts Paper: Computer Win")

        elif user == "Scissor":
            if comp == "Paper":
                print("=>😁 Scissor cuts Paper: You Win")
            else:
                print("=>🥲 Rock smashes Scissor: Computer Win")

while True: 
    game_logic()
    play_again = input("\n=> Do you want to Play again(y/n): ").lower()
    if play_again != "y":
        print(f"Thanks for Playing 👏")
        break
