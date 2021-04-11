import random

def play():
    user = input("What do you chose? (r) is of rock, (p) is for paper, (s) is for scissors")
    computer = random.choice(['r', 'p', 's'])

  
    if user == computer:
        return 'It is a draw'

    if win(user, computer):
        return 'You won'   


    return 'You lost'    



def win(me, oponent):
       if (me == 'p' and oponent == 'r') or (me == 's' and oponent == 'p') or (me == 'r' and oponent == 's'):
           return True        



           