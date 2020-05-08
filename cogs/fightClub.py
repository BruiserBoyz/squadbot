import random
import discord
from discord.ext import commands
from .fightclub.fight_game import FightGame
from .fightclub.fighter import Fighter

class FightClub(commands.Cog):
# class FightClub():
    def __init__(self, client):
        self.client = client
        self.fg = FightGame()

    @commands.command(aliases=['challenge'])
    async def _challenge(self, ctx, *, fighter):
        # Invoke new fighter and set the attributes.
        new_fighter = Fighter()
        # TODO replace this with the member object, or some way to link to member.
        new_fighter.set_player(fighter)
        self.fg.set_fighter(new_fighter)
        # Increase number of fighters - remember to decrease when we drop a fighter.
        self.fg.set_num_fighters(1)

        # get some fighter information (demo)
        new_fighter = self.fg.get_fighter(self.fg.get_num_fighters()-1)
        player_name = new_fighter.get_player()
        # await ctx.send(player_name)

    @commands.command(aliases=['printF'])
    async def _print_fighters(self, ctx):
        fighters = self.fg.get_all_fighters()
        prt_fighter = ""
        for fighter in fighters:
            prt_fighter += f'{fighter}\n'
        await ctx.send(prt_fighter)

    @commands.command(aliases=['weapon'])
    async def _set_weapon(self, ctx, weapon, *, fighter):
        """Sets a new weapon for a single fighter"""
        weapon_set = self.fg.set_fighter_weapon(weapon, fighter)
        if weapon_set:
            await ctx.send(f'{fighter} was found and {weapon} was set')
        else:
            await ctx.send('Problem setting the weapon.')

    @commands.command(aliases=['setWeaponAll'])
    async def _set_weapon_all(self, ctx, weapon):
        """Gives the same weapon to all fighters"""
        weapon_set = self.fg.set_all_weapons(weapon)
        if weapon_set:
            await ctx.send(f'All fighters now have a {weapon}.')
        else:
            await ctx.send('Problem setting the weapons for some or all fighters.')

    @commands.command(aliases=['f2'])
    async def _fight_two(self, ctx, num_rounds):
        """Takes the first two fighters, and brawls them."""
        game_over_man = False
        round = 0
        round_counter = 1
        if num_rounds == 'd':
            rounds = 99
        else:
            rounds = num_rounds

        while str(round) < str(rounds) and not game_over_man:
            msg = f'Round {round_counter}\n'
            do_fight = self.fg.fight_two()
            if "game over man" in do_fight:
                game_over_man = True
            msg += do_fight
            await ctx.send(msg)
            if num_rounds != 'd':
                round += 1
            round_counter += 1

    @commands.command(aliases=['td'])
    async def _test_data(self, ctx):
        f1 = Fighter()
        f1.set_player("Justin")
        f1.set_weapon("Pistole")
        f2 = Fighter()
        f2.set_player("Ploberto")
        f2.set_weapon("Kor")
        self.fg.set_fighter(f1)
        self.fg.set_fighter(f2)
        self.fg.set_num_fighters(2)


    @commands.command(aliases=['dd'])
    async def _drop_fighter_db(self, ctx):
        self.fg.drop_all_fighters()
        await ctx.send(f'# fighters {self.fg.get_num_fighters()}')

def setup(client):
    client.add_cog(FightClub(client))
