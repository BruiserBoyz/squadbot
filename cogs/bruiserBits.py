# import discord
from discord.ext import commands
import asyncio
import asyncpg
import datetime
import discord

# from .bruiser_bits.bb_accounts import MemberAccount
# from .bruiser_bits.bb_bruiserbank import BruiserBank

# this_bank = BruiserBank()
#
# # Create a new bank account for each new member.
# this_bank.add_account(MemberAccount())
SB_WALLET = "sb_wallet_1"
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

        # query = "INSERT INTO %s (col_1, col_2) VALUES (%%s, %%s)" % SB_WALLET
        await conn.execute('''
                CREATE TABLE sb_wallet_2(
                    id serial PRIMARY KEY,
                    d_user_id int UNIQUE,
                    d_init_auth_id int,
                    date_est date,
                    balance double PRECISION
                )
            ''')

        # self.loop.run_until_complete(self.fc_est_dc())
        await conn.close()

    # @commands.command(aliases=['qbal'])
    # async def _qbal(self, ctx):
    #     """Displays quick balance - qbal"""
    #     for x in this_bank.get_all_accounts():
    #         print(x.get_balance())
    #     await ctx.send(x.get_balance())

    @commands.command(aliases=['qbal'])
    async def get_db(self, ctx):
        auth_id = ctx.message.author.id
        conn = await asyncpg.create_pool(**CREDS)
        self.row = await conn.fetchrow(
            'SELECT balance FROM sb_wallet_2 WHERE d_user_id = $1', auth_id
        )
        my_balance = self.row['balance']
        await conn.close()
        await ctx.send(f'{BB}{my_balance}')


    @commands.command(aliases=['add_wallet'])
    async def do_db(self, ctx, *, user: discord.User):
        # Setup the variables.
        now_date = datetime.datetime.now()
        user_id = user.id
        auth_id = ctx.message.author.id
        conn = await asyncpg.create_pool(**CREDS)
        # Execute.
        await conn.execute('''
                        INSERT INTO sb_wallet_2(d_user_id, d_init_auth_id, date_est, balance) VALUES($1, $2, $3, $4)
                    ''', user_id, auth_id, datetime.date(now_date.year, now_date.month, now_date.day), 0.0)
        await conn.close()
        print("wallet added")

    # Add player to array
    @commands.command(aliases=['check_user'])
    async def _check_user(self, ctx, *, user: discord.User):

        """for testing only"""
        user_id = user.id
        auth_id = ctx.message.author.id
        print(user_id, auth_id)

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


def setup(client):
    client.add_cog(BruiserBits(client))


# Add triggers for deposits, withdrawals, transfers.
# A deposit may be from posting content to news sections
# Withdrawal maybe to get some credit on swag or to access custom emoji accessible via a specific role
# or entry fee to fight club
# A Transfer may be from losing a fight club.
