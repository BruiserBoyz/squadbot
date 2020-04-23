# import discord
from discord.ext import commands
import asyncio
import asyncpg
import datetime

# from .bruiser_bits.bb_accounts import MemberAccount
# from .bruiser_bits.bb_bruiserbank import BruiserBank

# this_bank = BruiserBank()
#
# # Create a new bank account for each new member.
# this_bank.add_account(MemberAccount())
CREDS = {
            "user": "postgres",
            "password": "cBUaCHS3ptvFyi",
            "database": "squadbot_demo",
            "host": "squadbot.ckkl1eknyjde.ap-southeast-2.rds.amazonaws.com"
        }
BB = '<:bb:702872380149727232> '


class BruiserBits(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.loop = asyncio.get_event_loop()

    # Establish DB table(s).
    @commands.command(aliases=['est_db_toastcheeserabbit'])
    async def _fc_est_db(self, ctx):
        """Setup tables if they don't exist"""
        conn = await asyncpg.connect(**CREDS)
        # Execute a statement to create a new table.
        await conn.execute('''
                CREATE TABLE sb_wallet(
                    id serial PRIMARY KEY,
                    name text,
                    est date,
                    bal double PRECISION
                )
            ''')

        self.loop.run_until_complete(self.fc_est_dc())
        await conn.close()

    # @commands.command(aliases=['qbal'])
    # async def _qbal(self, ctx):
    #     """Displays quick balance - qbal"""
    #     for x in this_bank.get_all_accounts():
    #         print(x.get_balance())
    #     await ctx.send(x.get_balance())

    @commands.command(aliases=['qbal'])
    async def get_db(self, ctx, *, user_nm):
        conn = await asyncpg.create_pool(**CREDS)
        self.row = await conn.fetchrow(
            'SELECT bal FROM sb_wallet WHERE name = $1', user_nm
        )
        my_balance = self.row['bal']
        await conn.close()
        await ctx.send(f'{BB}{my_balance}')

    @commands.command(aliases=['add_wallet'])
    async def do_db(self, ctx, *, user_nm):
        conn = await asyncpg.create_pool(**CREDS)
        await conn.execute('''
                        INSERT INTO sb_wallet(name, est, bal) VALUES($1, $2, $3)
                    ''', user_nm, datetime.date(2020, 4, 23), 0.0)
        await conn.close()

    @commands.command(aliases=['add_money'])
    async def do_add_money(self, ctx, funds_to_add, user_nm):
        conn = await asyncpg.create_pool(**CREDS)
        row = await conn.fetchrow(
            'SELECT bal FROM sb_wallet WHERE name = $1', user_nm
        )
        my_balance = row['bal'] + float(funds_to_add)
        await conn.execute('''
                            UPDATE sb_wallet set bal = $1
                            WHERE name = $2
                        ''', float(my_balance), user_nm)
        await ctx.send(f'{BB}{funds_to_add} added to account')
        await conn.close()
    #
    # @commands.command(aliases=['qdep'])
    # async def _qdep(self, ctx):
    #     """Very quick deposit to single account - qdep"""
    #     counter = 0
    #     for x in this_bank.get_all_accounts():
    #         # print(x.get_balance)
    #         this_bank.deposit(counter, 100)
    #         counter += 1
    #
    # @commands.command(aliases=['tfr'])
    # async def _tfr(self, ctx, *, account_from, account_to, amount):
    #     """Transfer from a single account to another single account - tfr"""
    #     this_bank.transfer(account_from, account_to, amount)


def setup(client):
    client.add_cog(BruiserBits(client))


# Add triggers for deposits, withdrawals, transfers.
# A deposit may be from posting content to news sections
# Withdrawal maybe to get some credit on swag or to access custom emoji accessible via a specific role
# or entry fee to fight club
# A Transfer may be from losing a fight club.
