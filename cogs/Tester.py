import random

from discord.ext import commands


class ShortCircuit():
    def __init__(self):
        self.message = "is alive"
        self.players = []

    def return_message(self):
        return self.message

    def add_player(self, playerName):
        self.players.append(playerName)

    def get_players(self):
        return self.players


class Tester(commands.Cog):

    def __init__(self, client):
        self.client = client
        self.robot = ShortCircuit()

    # Tester
    @commands.command(aliases=['jr'])
    async def _jr(self, ctx, *, question):
        responses = ['henlo, number five...' + self.robot.return_message() ,]
        await ctx.send(f'you say: {question}\nI say: {random.choice(responses)}')

    # Add player to array
    @commands.command(aliases=['ap'])
    async def _add_player(self, ctx, *, playerName):
        self.robot.add_player(playerName)
        await ctx.send(f'Player {playerName} added.')

    # List players.
    @commands.command(aliases=['lp'])
    async def _list_players(self, ctx):
        players = self.robot.get_players()
        await ctx.send(f'Player {players}.')


def setup(client):
    client.add_cog(Tester(client))
