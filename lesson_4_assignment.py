from random import randrange

# Create a function to get the users weapon
def get_user_weapon():
    print("\n--- SELECT YOUR WEAPON. ---")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")

    user_choice = int(input("Enter your Weapon: "))
    return user_choice

# Create a function to get the opponents weapon
def get_opponent_weapon():
    opponent_choice = randrange(1, 4)
# 4 in the randrange is exclusive
    return opponent_choice

# Lastly, create a determine winner function
def determine_winner(user_choice, opponent_choice):
    if user_choice == opponent_choice:
        print("It's a tie!")

    elif user_choice == 1 and opponent_choice == 3:
        print("Result: You win, Rock smashes Scissors.")
    elif user_choice == 3 and opponent_choice == 1:
        print("Result: You lose, Rock smashes Scissors.")
    elif user_choice == 3 and opponent_choice == 2:
        print("Result: You win, Scissors cuts Paper.")
    elif user_choice == 2 and opponent_choice == 3:
        print("Result: You lose, Scissors cuts Paper.")     
    elif user_choice == 2 and opponent_choice == 1:
        print("Result: You win, Paper covers Rock.")
    elif user_choice == 1 and opponent_choice == 2:
        print("Result: You lose, Paper covers Rock.")

def main():
    # Use a loop to allow the user to select if they would like to continue playing the game
    play_again = "y"
    
    while play_again.lower() == "y":
        user_weapon = get_user_weapon()
        opponent_weapon = get_opponent_weapon()
        determine_winner(user_weapon, opponent_weapon)
        
        play_again = input("\nWant to play again? (y/n): ")
        
    print("\nCompleted by Lincoln Reeves.")

if __name__ == "__main__":
    main()
