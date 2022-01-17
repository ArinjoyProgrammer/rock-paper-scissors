# MODULE IMPORTS ARE HERE
import random
import variables


# OTHER CONDITIONS
if variables.user_choice == variables.computer_choice:
    print(variables.tie_msg_rn)

elif variables.user_choice not in variables.choices:
    print(variables.wrong_msg_rn)

# WIN CONDITIONS
elif variables.computer_choice == 'rock':
    if variables.user_choice == 'paper':
        print(variables.win_msg_rn)

elif variables.computer_choice == 'paper':
    if variables.user_choice == 'scissor':
        print(variables.win_msg_rn)

elif variables.computer_choice == 'scissor':
    if variables.user_choice == 'rock':
        print(variables.win_msg_rn)

# LOSING CONDITIONS
elif variables.computer_choice == 'rock':
    if variables.user_choice == 'scissor':
        print(variables.lose_msg_rn)

elif variables.computer_choice == 'paper':
    if variables.user_choice == 'rock':
        print(variables.lose_msg_rn)

elif variables.computer_choice == 'scissor':
    if variables.user_choice == 'paper':
        print(variables.lose_msg_rn)

# CODE ENDS HERE!
