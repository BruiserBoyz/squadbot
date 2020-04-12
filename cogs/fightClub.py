import random
import discord
from discord.ext import commands

from .fightclub.displayFight import displayFight
from .fightclub.fc_fight import fc_fight

fight_club_players = []
weapon_selection = [
    "rusty broken knife",
    "ruddy gun",
    "broken bottle",
]


class FCPlayer:
    def __init__(self):
        self.member_obj = None
        self.player_name = None
        self.weapon = None
        self.strength = 1
        self.speed = 1
        self.agility = 1
        self.health = 1

    def get_weapon(self):
        return self.weapon

    def set_weapon(self, new_weapon):
        self.weapon = new_weapon

    def get_health(self):
        return self.health


class FightClub(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.fight_club_players = []
        self.do_fight = []

    def set_fc_players(self, winner):
        self.fight_club_players = []
        self.fight_club_players.append(winner)

    # Add player to array
    @commands.command(aliases=['fcap'])
    async def _fc_add_player(self, ctx, *, user: discord.Member):
        """adds a player into fight club - fcap"""
        obj = FCPlayer()
        obj.member_obj = user
        obj.set_weapon(weapon_selection[random.randint(0, 2)])
        self.fight_club_players.append(obj)
        # await ctx.send(f'{user.display_name} added.')
        await ctx.send(f'{user.mention} added.')

    # List players.
    @commands.command(aliases=['fclp'])
    async def _fc_list_players(self, ctx):
        """lists current players in fight club- fclp"""
        players = self.fight_club_players
        return_message = "Fighter(s): "
        for player in players:
            return_message += f'{player.member_obj.display_name}, '
        await ctx.send(f'{return_message}.')

    @commands.command(aliases=['f!'])
    async def _fc_fight(self, ctx):
        """turns two players against each other - f!"""
        # Set rando weapons
        for x in self.fight_club_players:
            x.set_weapon((weapon_selection[random.randint(0, 2)]))
        self.do_fight = fc_fight(self.fight_club_players)

        vs_screen = displayFight.display_VS(self.do_fight)
        await ctx.send(vs_screen)
        winner = displayFight.fight_winner(self.do_fight)
        await ctx.send(winner)
        self.set_fc_players(self.do_fight[4])


def setup(client):
    client.add_cog(FightClub(client))
