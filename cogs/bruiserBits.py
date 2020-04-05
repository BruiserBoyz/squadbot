# import discord
from discord.ext import commands

from .bruiser_bits.bb_accounts import MemberAccount
from .bruiser_bits.bb_bruiserbank import BruiserBank

this_bank = BruiserBank()

# create a new bank account for each existing member.
this_bank.add_account(MemberAccount())
this_bank.add_account(MemberAccount())
this_bank.add_account(MemberAccount())

# Create a new bank account for each new member.
this_bank.add_account(MemberAccount())


class BruiserBits(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['qbal'])
    async def _qbal(self, ctx):
        for x in this_bank.get_all_accounts():
            print(x.get_balance())
        await ctx.send(x.get_balance())

    @commands.command(aliases=['qdep'])
    async def _qdep(self, ctx):
        counter = 0
        for x in this_bank.get_all_accounts():
            # print(x.get_balance)
            this_bank.deposit(counter, 100)
            counter += 1

    @commands.command(aliases=['tfr'])
    async def _tfr(self, ctx, *, account_from, account_to, amount):
        this_bank.transfer(account_from, account_to, amount)


def setup(client):
    client.add_cog(BruiserBits(client))


# Add triggers for deposits, withdrawals, transfers.
# A deposit may be from posting content to news sections
# Withdrawal maybe to get some credit on swag or to access custom emoji accessible via a specific role
# or entry fee to fight club
# A Transfer may be from losing a fight club.
