import random


# This should bea class but is just a function for ease of example.
def fc_fight(fight_club_players):
    # Set some initial variables
    fcf_return_array = []
    p1 = fight_club_players[0]
    p1_score = random.randint(0, 100)
    p2 = fight_club_players[1]
    p2_score = random.randint(0, 100)

    # Allocate weapons
    fcf_return_array.append(f'{p1.weapon}')
    fcf_return_array.append(f'{p2.weapon}')

    # add winners / losers to array
    # TODO instead of sending the px.member_obj - could jsut send the p1 / p2 objects in entirety.
    if p1_score > p2_score:
        winner = p1.member_obj
        loser = p2.member_obj
        winner_obj = p1
    else:
        winner = p2.member_obj
        loser = p1.member_obj
        winner_obj = p2

    fcf_return_array.append(winner)
    fcf_return_array.append(loser)
    fcf_return_array.append(winner_obj)
    # Return the array
    return fcf_return_array
