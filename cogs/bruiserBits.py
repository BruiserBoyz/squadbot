# import discord
from discord.ext import commands
import asyncio
import asyncpg
import datetime
import discord
import os
from dotenv import load_dotenv
load_dotenv('../../.env')

CREDS_P = os.getenv("CREDS_P")
CREDS_U = os.getenv("CREDS_U")
CREDS_H = os.getenv("CREDS_H")
CREDS_D = os.getenv("CREDS_D")
BANK_OWNER = os.getenv("BANK_OWNER")
BB = os.getenv("BB")

SB_WALLET = "sb_wallet_3"
CREDS = {
            "user": CREDS_U,
            "password": CREDS_P,
            "database": CREDS_D,
            "host": CREDS_H
        }


class BruiserBits(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.loop = asyncio.get_event_loop()

    # Establish DB table(s).
    @commands.command(aliases=['est_db_toastcheeserabbit'])
    async def _fc_est_db(self, ctx):
        auth_id = ctx.message.author.id
        if auth_id != int(BANK_OWNER):
            print("not authorised")
            return
        else:
            """Setup tables if they don't exist"""
            conn = await asyncpg.connect(**CREDS)
            # Execute a statement to create a new table.

            # query = "INSERT INTO %s (col_1, col_2) VALUES (%%s, %%s)" % SB_WALLET
            await conn.execute('''
                    CREATE TABLE sb_wallet_3(
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
        print("Authorised.")
        conn = await asyncpg.create_pool(**CREDS)
        self.row = await conn.fetchrow(
            'SELECT balance FROM sb_wallet_3 WHERE d_user_id = $1', auth_id
        )
        my_balance = self.row['balance']
        await conn.close()
        await ctx.send(f'{BB}{my_balance}')


    @commands.command(aliases=['add_wallet'])
    async def do_db(self, ctx, *, user: discord.User):
        auth_id = ctx.message.author.id
        if auth_id != int(BANK_OWNER):
            print("Not authorised.")
            return
        else:
            # Setup the variables.
            now_date = datetime.datetime.now()
            user_id = user.id
            auth_id = ctx.message.author.id
            conn = await asyncpg.create_pool(**CREDS)
            # Execute.
            await conn.execute('''
                            INSERT INTO sb_wallet_3(d_user_id, d_init_auth_id, date_est, balance) VALUES($1, $2, $3, $4)
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
    async def _add_money(self, ctx, funds_to_add, *, user: discord.User):
        auth_id = ctx.message.author.id
        if auth_id != int(BANK_OWNER):
            print(BANK_OWNER)
            print("Not Authorised.")
            return
        else:
            print("Authorised.")
            conn = await asyncpg.create_pool(**CREDS)
            user_id = user.id
            row = await conn.fetchrow(
                'SELECT balance FROM sb_wallet_3 WHERE d_user_id = $1', user_id
            )
            my_balance = row['balance'] + float(funds_to_add)
            await conn.execute('''
                                UPDATE sb_wallet_3 set balance = $1
                                WHERE d_user_id = $2
                            ''', float(my_balance), user_id)
            await ctx.send(f'{BB}{funds_to_add} added to account')
            await conn.close()

    @commands.command(aliases=['transfer'])
    async def _transfer_money(self, ctx, funds_to_tfr, *, user: discord.User):
        auth_id = ctx.message.author.id
        conn = await asyncpg.create_pool(**CREDS)
        user_id = user.id

        # Remove the funds
        row = await conn.fetchrow(
            'SELECT balance FROM sb_wallet_3 WHERE d_user_id = $1', auth_id
        )
        my_balance = row['balance'] - float(funds_to_tfr)
        if my_balance >= 0:
            await conn.execute('''
                                UPDATE sb_wallet_3 set balance = $1
                                WHERE d_user_id = $2
                            ''', float(my_balance), auth_id)

            # Add the funds
            row = await conn.fetchrow(
                'SELECT balance FROM sb_wallet_3 WHERE d_user_id = $1', user_id
            )
            my_balance = row['balance'] + float(funds_to_tfr)
            await conn.execute('''
                                        UPDATE sb_wallet_3 set balance = $1
                                        WHERE d_user_id = $2
                                    ''', float(my_balance), user_id)

            await ctx.send(f'{BB}{funds_to_tfr} transfered to account')
            await conn.close()
        else:
            await ctx.send("Not enough money to do that homie...")


def setup(client):
    client.add_cog(BruiserBits(client))
