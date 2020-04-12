from io import BytesIO

import requests
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFile
from PIL import ImageFont

ImageFile.LOAD_TRUNCATED_IMAGES = True
font = ImageFont.truetype('./cogs/assets/fonts/mk2.ttf', 30)  # selected font (location required)
largeFont = ImageFont.truetype('./cogs/assets/fonts/mk2.ttf', 50)  # selected font (location required)
newsize = (250, 250)


class displayFight:
    def __init__(self, fight_info):
        self.av_images = []
        self.info = fight_info

    def display_VS(self):
        """retrieves the avatars for both users in the fight and creates a VS image"""
        url1 = self.info[2].avatar_url  # winners avatar
        response1 = requests.get(url1)  # requests the image
        self.av_images[0] = Image.open(BytesIO(response1.content))  # Opens the image
        self.av_images[0] = self.av_images[0].resize(newsize)  # resize the image

        url2 = self.info[3].avatar_url  # losers avatar
        response2 = requests.get(url2)  # requests the image
        self.av_images[1] = Image.open(BytesIO(response2.content))  # Opens the image
        self.av_images[1] = self.av_images[1].resize(newsize)  # resize the image

        bg1 = Image.open('./cogs/assets/img/background.jpg')  # Background image to be loaded
        vs = Image.open('./cogs/assets/img/vs.png')  # VS image to be loaded

        avatar_BG = bg1.copy()  # creates a copy of the background image to be edited
        avatar_BG.paste(self.av_images[0], (125, 125))  # Pastes the Avatar1 image onto top left side of BG
        avatar_BG.paste(self.av_images[1], (825, 125))  # Pastes the Avatar2 image onto top right side of BG
        avatar_BG.paste(vs, (475, 175))  # Pastes the VS logo into center.

        drawbg = ImageDraw.Draw(avatar_BG)  # Allows pillow to overlay text onto image

        #     (x,y)::↓ ↓ ↓(text)::↓ ↓ (r,g,b)::↓ ↓ ↓
        drawbg.text((475, 50), "{}".format("_ FIGHT! _"), (255, 255, 255), font=largeFont)  # Central Header
        drawbg.text((125, 400), "{}".format(self.info[2].display_name), (255, 255, 255),
                    font=font)  # Nickname of the Winner
        drawbg.text((825, 400), "{}".format(self.info[3].display_name), (255, 255, 255),
                    font=font)  # Nickname of the Loser
        drawbg.text((125, 450), "{}".format(self.info[2].top_role), (255, 255, 255),
                    font=font)  # draws the top role for Winner
        drawbg.text((825, 450), "{}".format(self.info[3].top_role), (255, 255, 255,),
                    font=font)  # draws the top role for Loser
        drawbg.text((125, 500), "{}".format(self.info[1]), (255, 255, 255, 255),
                    font=font)  # displays the weapons used
        drawbg.text((825, 500), "{}".format(self.info[0]), (255, 255, 255, 255),
                    font=font)  # displays the weapons used

        return avatar_BG

    def fight_winner(self):
        """Displays the winner of the fight !!"""
        winner = self.av_images[0]  # currently the winner is at position Zero
        background = Image.open('./cogs/assets/img/background.jpg')  # generic background

        winner_BG = background.copy()  # create a copy og the stock background.
        winner_BG.paste(winner, (125, 125))  # Pastes the Avatar1 image onto top left side of BG

        draw_winner = ImageDraw.Draw(winner_BG)  # Allows pillow to overlay text onto image.

        #     (x,y)::↓ ↓ ↓(text)::↓ ↓ (r,g,b)::↓ ↓ ↓
        draw_winner.text((475, 100), "{}{}".format(self.info[2].display_name, " is the Winner!"),
                         (255, 255, 255),
                         font=font)  # Announce Winner
        draw_winner.text((475, 200), "{}{}".format("He destroyed ", self.info[3].display_name),
                         (255, 255, 255),
                         font=font)  # Whom the winner destroyed

        draw_winner.text((475, 300), "{}{}".format("Using their trusty ", self.info[1]), (255, 255, 255),
                         font=font)  # Weapon Used by winner
        draw_winner.text((475, 400),
                         "{}{}{}{}".format(self.info[2].display_name, " made ", self.info[2].top_role,
                                           ' proud!'),
                         (255, 255, 255),
                         font=font)  # Shows the guild/role
        draw_winner.text((475, 500), "{}".format('Earning $ BruizerBits'), (255, 255, 255,),
                         font=font)  # draws the top role for Loser

        return winner_BG
