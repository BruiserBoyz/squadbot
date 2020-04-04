import random


# This should bea class but is just a function for ease of example.
def fc_fight(fight_club_players):
    # Set some initial variables
    fcf_return_array =[]
    p1 = fight_club_players[0]
    p1_score = random.randint(0, 100)
    p2 = fight_club_players[1]
    p2_score = random.randint(0, 100)

    # Return some combat messages
    fcf_return_array[0] = f'{p1.member_obj.display_name} has a {p1.weapon}.'
    fcf_return_array[1] = f'{p2.member_obj.display_name} has a {p2.weapon}.'

    # add winners / losers to array
    if p1_score > p2_score:
        fcf_return_array[2] = p1.member_obj.mention
        fcf_return_array[3] = p2.member_obj.mention
    else:
        fcf_return_array[3] = p2.member_obj.mention
        fcf_return_array[2] = p1.member_obj.mention

    # Return the array
    return fcf_return_array
