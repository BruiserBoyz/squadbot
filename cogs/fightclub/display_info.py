from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from io import BytesIO
import requests


def display_info(fighters):
    url1 = fighters[2].avatar_url  # winners avatar
    response1 = requests.get(url1)
    avatar1 = Image.open(BytesIO(response1.content))
    avatar1.save('./cogs/assets/img/avatar1.png')
    url2 = fighters[3].avatar_url  # losers avatar
    response2 = requests.get(url2)
    avatar2 = Image.open(BytesIO(response2.content))
    avatar2.save('./cogs/assets/img/avatar2.png')

    bg1 = Image.open('./cogs/assets/img/initialBG.png')  # Background image to be loaded

    bg1.paste('./cogs/assets/img/avatar1.png'(300, 300), './cogs/assets/img/avatar1.png')
    bg1.paste('./cogs/assets/img/avatar2.png'(450, 450), './cogs/assets/img/avatar2.png')
    bg1.save('./cogs/assets/img/avatarBG.png')

    # avatar_BG = Image.open('./cogs/assets/img/avatarBG.png')
    #
    # drawbg = ImageDraw.Draw(avatar_BG)
    # font = ImageFont.truetype('./cogs/assets/fonts/Gotu-Regular.ttf', 45)  # Selected fonts.
    # largeFont = ImageFont.truetype('./cogs/assets/fonts/Gotu-Regular.ttf', 45)  # Selected fonts.
    # #     (x,y)::↓ ↓ ↓(text)::↓ ↓ (r,g,b)::↓ ↓ ↓
    # drawbg.text((500, 50), "VICTORY!", (0, 0, 0), font=largeFont)  # draws Heading
    # drawbg.text((150, 100), "{}".format(fighters[2].display_name), (0, 0, 0),
    #             font=font)  # Nickname of the Winner
    # drawbg.text((150, 500), "{}".format(fighters[3].display_name), (0, 0, 0),
    #             font=font)  # Nickname of the Loser
    # drawbg.text((150, 575), "{}".format(fighters[2].top_role), (0, 0, 0),
    #             font=font)  # draws the top role for Winner
    # drawbg.text((150, 575), "{}".format(fighters[3].top_role), (0, 0, 0),
    #             font=font)  # draws the top role for Loser
    # bg.save('./cogs/assets/img/fight!.png')  # Change fight.png if needed
