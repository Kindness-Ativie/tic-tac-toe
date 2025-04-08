import itertools
from random import choice

players: list[str] = []
instructions: str = input('Welcome to the best tic tac toe of your life. >_>/ x vs. o -> Click any key to start!')
player_x: str = input('Who will be x?: ')
player_o: str = input('Who will be o?: ')
players.extend([player_x, player_o])


adjs: list[str] = ['happy', 'snappy', 'mysterious', 'great', 'little', 'awesome', 'funny', 'comical', 'sassy']

welcome_screen: str = f'''
COMMENCE INTENSE TIC TAC TOE <_* @_A/
{player_x.upper()} as the {choice(adjs)} X VS. {player_o.upper()} as the {choice(adjs)} O
'''

print(welcome_screen)


# game set up


spots: dict = {
    'a': '__',
    'b': '__',
    'c': '__',
    'd': '__',
    'e': '__',
    'f': '__',
    'g': '__',
    'h': '__',
    'i': '__'
}

board: str = f'''

 {spots['a']} {spots['b']} {spots['c']} 
 {spots['d']} {spots['e']} {spots['f']}
 {spots['g']} {spots['h']} {spots['i']}

'''

available_plays: str = '''
a b c
d e f 
g h i
'''


winning_configurations: list[str] = ['abc', 'def', 'ghi',
                                     'adg', 'beh', 'cfi',
                                     'aei', 'gec']

player = itertools.cycle(players)
used_spots: list[str] = []
while True:
    current_player: str = next(player)
    if current_player == player_x:
        symbol: str = 'X'
    else:
        symbol: str = 'O'
    print('The great board )_)/')
    print(board)

    print('Spots left. *_+')
    for spot in used_spots:
        available_plays = available_plays.replace(spot, ' ')
    print(available_plays)

    my_spot: str = (input(f'Where would you like to put your {symbol} {current_player}? : '))
    spots[f'{my_spot}'] = symbol
    used_spots.append(my_spot)

    # convert to string
    # if string is at that index
    # save index, grab index of variable list and adjust it to symbol
