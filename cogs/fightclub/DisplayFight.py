from io import BytesIO

import requests
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFile
from PIL import ImageFont


class DisplayFight:
    ImageFile.LOAD_TRUNCATED_IMAGES = True
    font = ImageFont.truetype('./cogs/assets/fonts/fightkidci.ttf', 30)  # selected font (location required)
    largeFont = ImageFont.truetype('./cogs/assets/fonts/fightkidci.ttf', 50)  # selected font (location required)
    new_size = (250, 250)

    def __init__(self, fighters):
        self.fighters = fighters
        self.av_images = []

    def display_vs(self):
        """retrieves the avatars for both users in the fight and creates a VS image"""
        url1 = self.fighters[2].avatar_url  # winners avatar
        response1 = requests.get(url1)  # requests the image
        self.av_images.append(Image.open(BytesIO(response1.content)))  # adds the image to array
        self.av_images[0] = self.av_images[0].resize(self.new_size)  # resize the image

        url2 = self.fighters[3].avatar_url  # losers avatar
        response2 = requests.get(url2)  # requests the image
        self.av_images.append(Image.open(BytesIO(response2.content)))  # adds the image to array
        self.av_images[1] = self.av_images[1].resize(self.new_size)  # resize the image

        bg1 = Image.open('./cogs/assets/img/background.jpg')  # Background image to be loaded
        vs = Image.open('./cogs/assets/img/vs.png')  # VS image to be loaded

        avatar_bg = bg1.copy()  # creates a copy of the background image to be edited
        avatar_bg.paste(self.av_images[0], (125, 125))  # Pastes the Avatar1 image onto top left side of BG
        avatar_bg.paste(self.av_images[1], (825, 125))  # Pastes the Avatar2 image onto top right side of BG
        avatar_bg.paste(vs, (475, 175))  # Pastes the VS logo into center.

        draw_bg = ImageDraw.Draw(avatar_bg)  # Allows pillow to overlay text onto image

        #     (x,y)::↓ ↓ ↓(text)::↓ ↓ (r,g,b)::↓ ↓ ↓
        draw_bg.text((475, 50), "{}".format("_ FIGHT! _"), (255, 255, 255), font=self.largeFont)  # Central Header
        draw_bg.text((125, 400), "{}".format(self.fighters[2].display_name), (255, 255, 255),
                     font=self.font)  # Nickname of the Winner
        draw_bg.text((825, 400), "{}".format(self.fighters[3].display_name), (255, 255, 255),
                     font=self.font)  # Nickname of the Loser
        draw_bg.text((125, 450), "{}".format(self.fighters[2].top_role), (255, 255, 255),
                     font=self.font)  # draws the top role for Winner
        draw_bg.text((825, 450), "{}".format(self.fighters[3].top_role), (255, 255, 255,),
                     font=self.font)  # draws the top role for Loser
        draw_bg.text((125, 500), "{}".format(self.fighters[1]), (255, 255, 255, 255),
                     font=self.font)  # displays the weapons used
        draw_bg.text((825, 500), "{}".format(self.fighters[0]), (255, 255, 255, 255),
                     font=self.font)  # displays the weapons used

        return avatar_bg

    def fight_winner(self):
        """Displays the winner of the fight !!"""
        winner = self.av_images[0]  # currently the winner is at position Zero
        background = Image.open('./cogs/assets/img/background.jpg')  # generic background

        winner_bg = background.copy()  # create a copy og the stock background.
        winner_bg.paste(winner, (125, 125))  # Pastes the Avatar1 image onto top left side of BG

        draw_winner = ImageDraw.Draw(winner_bg)  # Allows pillow to overlay text onto image.

        #     (x,y)::↓ ↓ ↓(text)::↓ ↓ (r,g,b)::↓ ↓ ↓
        draw_winner.text((475, 100), "{}{}".format(self.fighters[2].display_name, " is the Winner!"),
                         (255, 255, 255),
                         font=self.font)  # Announce Winner
        draw_winner.text((475, 200), "{}{}".format("He destroyed ", self.fighters[3].display_name),
                         (255, 255, 255),
                         font=self.font)  # Whom the winner destroyed

        draw_winner.text((475, 300), "{}{}".format("Using their trusty ", self.fighters[1]), (255, 255, 255),
                         font=self.font)  # Weapon Used by winner
        draw_winner.text((475, 400),
                         "{}{}{}{}".format(self.fighters[2].display_name, " made ", self.fighters[2].top_role,
                                           ' proud!'),
                         (255, 255, 255),
                         font=self.font)  # Shows the guild/role
        draw_winner.text((475, 500), "{}".format('Earning $ BruizerBits'), (255, 255, 255,),
                         font=self.font)  # draws the top role for Loser

        return winner_bg
