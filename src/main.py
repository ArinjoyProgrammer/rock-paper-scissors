# MODULE IMPORTS ARE HERE
import random


choices = ['rock', 'paper', 'scissor']

computer_choice = random.choice(choices)
user_choice = input("Choose Your Choice Carefully\nrock, paper, or scissor\n")

tie_msg = [f"Oh! That was close! Let's try again! (Tie)\nComputer Choosed - {computer_choice}", f"Oh! That's a Tie (Tie)\nComputer Choosed - {computer_choice}"]

wrong_msg = ["Umm, You choosed a wrong option that is not in the game! (Wrong Choice)", "Try again! I can't recognize (Wrong Choice)", "Your choices are wrong! (Wrong Choice)"]

win_msg = [f"Congradulations! You Won! (Win)\nComputer Choosed - {computer_choice}", f"Oh! You Won! You became a little bit smarter than me! (Win)\nComputer Choosed - {computer_choice}"]

lose_msg = [f"You Lose! Better Luck Next Time (Lose)\nComputer Choosed - {computer_choice}", f"Hehe! Try a little bit hard to beat me! Better Luck Next Time (Lose)\nComputer Choosed - {computer_choice}"]


tie_msg_rn = random.choice(tie_msg)
wrong_msg_rn = random.choice(wrong_msg)
win_msg_rn = random.choice(win_msg)
lose_msg_rn = random.choice(lose_msg)


# OTHER CONDITIONS
if user_choice == computer_choice:
    print(tie_msg_rn)

elif user_choice not in choices:
    print(wrong_msg_rn)

# WIN CONDITIONS
elif computer_choice == 'rock':
    if user_choice == 'paper':
        print(win_msg_rn)

elif computer_choice == 'paper':
    if user_choice == 'scissor':
        print(win_msg_rn)

elif computer_choice == 'scissor':
    if user_choice == 'rock':
        print(win_msg_rn)

# LOSING CONDITIONS
elif computer_choice == 'rock':
    if user_choice == 'scissor':
        print(lose_msg_rn)

elif computer_choice == 'paper':
    if user_choice == 'rock':
        print(lose_msg_rn)

elif computer_choice == 'scissor':
    if user_choice == 'paper':
        print(lose_msg_rn)

# CODE ENDS HERE!
