from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from io import BytesIO
import requests
from PIL import ImageFile

ImageFile.LOAD_TRUNCATED_IMAGES = True
newsize = (300, 300)


def display_VS(fighters):
    """retrieves the avatars for both users in the fight and creates a VS image"""
    url1 = fighters[2].avatar_url  # winners avatar
    response1 = requests.get(url1)  # requests the image
    avatar1 = Image.open(BytesIO(response1.content))  # Opens the image
    avatar1 = avatar1.resize(newsize)  # resize the image
    avatar1.save('./cogs/assets/img/avatar1.png')  # saves the image

    url2 = fighters[3].avatar_url  # losers avatar
    response2 = requests.get(url2)  # requests the image
    avatar2 = Image.open(BytesIO(response2.content))  # Opens the image
    avatar2 = avatar2.resize(newsize)  # resize the image
    avatar2.save('./cogs/assets/img/avatar2.png')  # saves the image

    avatarC1 = Image.open('./cogs/assets/img/avatar1.png')  # Avatar image to be loaded
    avatarC2 = Image.open('./cogs/assets/img/avatar2.png')  # Avatar image to be loaded
    bg1 = Image.open('./cogs/assets/img/background.jpg')  # Background image to be loaded
    vs = Image.open('./cogs/assets/img/vs.png')  # VS image to be loaded

    back_im = bg1.copy()  # creates a copy of the background image to be edited
    back_im.paste(avatarC1, (125, 125))  # Pastes the Avatar1 image onto top left side of BG
    back_im.paste(avatarC2, (775, 125))  # Pastes the Avatar2 image onto top right side of BG
    back_im.paste(vs, (475, 150))  # Pastes the VS logo into center.
    back_im.save('./cogs/assets/img/avatarBG.jpg')  # Saves new background image with avatar & VS.

    avatar_BG = Image.open('./cogs/assets/img/avatarBG.jpg')  # Opens saved new Background with assets
    drawbg = ImageDraw.Draw(avatar_BG)  # Allows pillow to overlay text onto image
    font = ImageFont.truetype('./cogs/assets/fonts/fightkidci.ttf', 30)  # selected font (location required)
    largeFont = ImageFont.truetype('./cogs/assets/fonts/fightkidci.ttf', 50)  # selected font (location required)

    #     (x,y)::↓ ↓ ↓(text)::↓ ↓ (r,g,b)::↓ ↓ ↓
    drawbg.text((450, 50), "{}".format("FIGHT CLUB!"), (255, 255, 255), font=largeFont)  # Central Header
    drawbg.text((165, 450), "{}".format(fighters[2].display_name), (255, 255, 255),
                font=font)  # Nickname of the Winner
    drawbg.text((815, 450), "{}".format(fighters[3].display_name), (255, 255, 255),
                font=font)  # Nickname of the Loser
    drawbg.text((165, 500), "{}".format(fighters[2].top_role), (255, 255, 255),
                font=font)  # draws the top role for Winner
    drawbg.text((815, 500), "{}".format(fighters[3].top_role), (255, 255, 255,),
                font=font)  # draws the top role for Loser

    avatar_BG.save('./cogs/assets/img/fight!.jpg')
