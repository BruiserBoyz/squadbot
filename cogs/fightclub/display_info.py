from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from io import BytesIO
import requests
from PIL import ImageFile

ImageFile.LOAD_TRUNCATED_IMAGES = True
newsize = (300, 300)


def display_info(fighters):
    url1 = fighters[2].avatar_url  # winners avatar
    response1 = requests.get(url1)
    avatar1 = Image.open(BytesIO(response1.content))
    avatar1 = avatar1.resize(newsize)
    avatar1.save('./cogs/assets/img/avatar1.png')
    avatarC1 = Image.open('./cogs/assets/img/avatar1.png')
    url2 = fighters[3].avatar_url  # losers avatar
    response2 = requests.get(url2)
    avatar2 = Image.open(BytesIO(response2.content))
    avatar2 = avatar2.resize(newsize)
    avatar2.save('./cogs/assets/img/avatar2.png')
    avatarC2 = Image.open('./cogs/assets/img/avatar2.png')
    bg1 = Image.open('./cogs/assets/img/background.jpg')  # Background image to be loaded
    vs = Image.open('./cogs/assets/img/vs.png')

    back_im = bg1.copy()
    back_im.paste(avatarC1, (100, 75))
    back_im.paste(avatarC2, (750, 75))
    back_im.paste(vs, (450, 150))
    back_im.save('./cogs/assets/img/avatarBG.jpg')

    avatar_BG = Image.open('./cogs/assets/img/avatarBG.jpg')
    drawbg = ImageDraw.Draw(avatar_BG)
    font = ImageFont.truetype('./cogs/assets/fonts/arial.ttf', 30)
    largeFont = ImageFont.truetype('./cogs/assets/fonts/arial.ttf', 50)
    #     (x,y)::↓ ↓ ↓(text)::↓ ↓ (r,g,b)::↓ ↓ ↓
    drawbg.text((140, 400), "{}".format(fighters[2].display_name), (255, 255, 255),
                font=font)  # Nickname of the Winner
    drawbg.text((800, 400), "{}".format(fighters[3].display_name), (255, 255, 255),
                font=font)  # Nickname of the Loser
    drawbg.text((140, 450), "{}".format(fighters[2].top_role), (255, 255, 255),
                font=font)  # draws the top role for Winner
    drawbg.text((800, 450), "{}".format(fighters[3].top_role), (255, 255, 255,),
                font=font)  # draws the top role for Loser

    avatar_BG.save('./cogs/assets/img/fight!.jpg')
