import random
import discord
from discord.ext import commands
from fightclub import fight_game

# class FightClub(commands.Cog):
class FightClub():
    def __init__(self, client):
        self.client = client
        self.fg = fight_game.FightGame()

    def _add_fighter(self, fighter):
        self.fg.set_fighter(fighter)

    def _print_fighters(self):
        fighters = self.fg.get_all_fighters()
        for fighter in fighters:
            print(f'{fighter}')

    # @commands.command(aliases=['challenge'])
    # async def _fc_add_player(self, ctx, *, user: discord.Member):
    #     # await ctx.send(f'{user.display_name} added.')
    #     await ctx.send(f'henlo.')

#     @commands.command(aliases=['fight'])
#     async def _fc_fight(self, ctx, *, user: discord.Member):
#         self.fg.set_fighter(ctx.message.author.id)
#         self.fg.set_fighter(user.mention)
#         for x in self.fg.get_all_fighters():
#             print(x)
#
#         await ctx.send(f'ok - we got a fight on our hands now!')
#
#
# def setup(client):
#     client.add_cog(FightClub(client))

game_on = True
game = FightClub("clientio")
while game_on:
    cmd = input("command: ")
    try:
        cmd_attr = cmd.split(" ")[1]
    except:
        cmd_attr = False

    if '.challenge' in cmd:
        game._add_fighter(cmd_attr)
    elif '.show' in cmd:
        game._print_fighters()
    elif '.setPrize' in cmd:
        game.fg.set_fight_prize(int(cmd_attr))
        print(f'prize set at {game.fg.get_fight_prize()}')
    elif 'exit' in cmd:
        print(f'later {game.client}')
        game_on = False;
        exit()