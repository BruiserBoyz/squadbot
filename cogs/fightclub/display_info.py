from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont


def display_info(fighters):
    bg = Image.open("./cogs/assets/img/Cypress-wall-panel-d-1030x593.png")  # Background image to be loaded
    avatarImage1 = fighters[2].avatar_url  # winners avatar
    avatarImage2 = fighters[3].avatar_url  # losers avatar
    drawbg = ImageDraw.Draw(bg)
    font = ImageFont.truetype("./cogs/assets/fonts/Gotu-Regular.ttf", 45)  # Selected fonts.
    largeFont = ImageFont.truetype("./cogs/assets/fonts/Gotu-Regular.ttf", 45)  # Selected fonts.
    #     (x,y)::↓ ↓ ↓(text)::↓ ↓ (r,g,b)::↓ ↓ ↓
    drawbg.text((150, 90), "BATTLE", (0, 0, 0), font=largeFont)  # draws Heading

    drawbg.text((150, 50), "{}".format(fighters[2].display_name), (0, 0, 0),
                font=font)  # Nickname of the Winner
    drawbg.paste(avatarImage1, (20, 50))  # paste the winner image to coordinate
    drawbg.paste(avatarImage2, (100, 200))  # paste the loser image to coordinate
    drawbg.text((150, 500), "{}".format(fighters[3].display_name), (0, 0, 0),
                font=font)  # Nickname of the Loser
    drawbg.text((150, 575), "{}".format(fighters[2].top_role), (0, 0, 0),
                font=font)  # draws the top role for Winner
    drawbg.text((150, 575), "{}".format(fighters[3].top_role), (0, 0, 0),
                font=font)  # draws the top role for Loser
    bg.save('./cogs/assets/img/fight!.png')  # Change fight.png if needed
