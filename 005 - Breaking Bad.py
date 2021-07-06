import random
import math

def play():
    user = input("Choose your character!\n\
'w' for Walter, 'j' for Jessie, \
'h' for Hank, 'g' for Gus\n")

    computer = random.choice(['w', 'j', 'h', 'g'])

    if user == computer:
        return 'You have DRAWN! "This is scientifically impossible!"'

    # w > g, h > j, j > w, g > h
    if is_win_wg(user, computer):
        return 'You have WON! "Say my name!"'

    if is_win_hj(user, computer):
        return 'You have WON! "They\'re not rocks. They\'re minerals!"'

    if is_win_jw(user, computer):
        return 'You have WON! "Yeah, Mr White! Science!"'

    if is_win_gh(user, computer):
        return 'You have WON! "A man provides!"'

    return 'You have LOST! "Stay out of my territory!"'

def is_win_wg(player, opponent):
    # return true if player wins.
    # w > g, h > j, j > w, g > h
    if (player == 'w' and opponent == 'g'):
        return True

def is_win_hj(player, opponent):
    # return true if player wins.
    # w > g, h > j, j > w, g > h
    if (player == 'h' and opponent == 'j'):
        return True

def is_win_jw(player, opponent):
    # return true if player wins.
    # w > g, h > j, j > w, g > h
    if (player == 'j' and opponent == 'w'):
        return True

def is_win_gh(player, opponent):
    # return true if player wins.
    # w > g, h > j, j > w, g > h
    if (player == 'g' and opponent == 'h'):
        return True

print(play())