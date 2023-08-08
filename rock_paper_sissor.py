
import random 

def play():
    user = input("Choose. 'r' rock, 'p' paper, 's' sissor")
    computer = random.choice(['r', 'p', 's'])

    if user == computer :
        return "Tie"
    # r>s, s>p , p>r
    if is_win( user, computer):
        return 'You Won!'
    
    return 'You Lost'

def is_win( player, opponent):
    # return true , if player wins 
    if (player == 'r' and opponent =='s') or (player == 's' and opponent == 'p') \
        or (player == 'p' and opponent =='r'):
        return True 

print(play())








