is_running = True

while is_running:
    player_1 = input('Enter choice 1 : ')
    player_2 = input('Enter choice 2 : ')
    if player_1 == 'scissors':
        if player_2 == 'rock':
            print('Player 2 won!')
        elif player_2 == 'paper':
            print('Player 1 won!')
    elif player_1 == 'rock':
        if player_2 == 'scissors':
            print('Player 1 won!')
        elif player_2 == 'paper':
            print('Player 2 won!')
    elif player_1 == 'paper':
        if player_2 == 'rock':
            print('Player 1 won!')
        elif player_2 == 'scissors':
            print('Player 2 won!')
    else:
        print('There was a Tie!')
    x = input('Do you want to play another game? ')
    if x == 'No' or x == 'no':
        is_running = False

lst = []
lst.append('Woho')
s='Hello'
s.lower()