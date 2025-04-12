"""  
            Develop game of "Char Chitthi" 
Randomly assign roles to four players.

Identify the Wajir from the assigned roles.

Find the Sipahi and Chor, since Wajir must choose between them.

The Wajir makes a random guess between Sipahi and Chor.

Check if the guess is correct:

If correct, the Chor is caught.

If incorrect, the Chor escapes.
"""
# import random

# roles = ['raja','wajir','sipahi','chor']
# random.shuffle(roles)

# player1,player2,player3,player4= random.sample(roles,4)
# print(player1,player2,player3,player4)

import random

# Define roles
roles = ['raja', 'wajir', 'sipahi', 'chor']

# Shuffle roles randomly
random.shuffle(roles)

# Assign roles to players
players = {
    "Player 1": roles[0],
    "Player 2": roles[1],
    "Player 3": roles[2],
    "Player 4": roles[3]
}

wajir_player = [player for player, role in players.items() if role == 'wajir'][0]
sipahi_chor = [player for player, role in players.items() if role in ['sipahi', 'chor']]



# Display assigned roles
print("Roles assigned:")
for player, role in players.items():
    print(f"{player}: {role}")

print(f"\n{wajir_player} is the Wajir!")
print(f"\nWajir must choose between these players: {sipahi,chor}")

    
















