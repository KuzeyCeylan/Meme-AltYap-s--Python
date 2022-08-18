#Coded Kuzey Ceylan
#Tr Licanse: Bu Komutların Kuzey Ceylan Git Hub Hesabının  Dışında Bir Yerde Paylaşılırsa Dava İle Uzlaşma Aranacaktır.

import os
import random
import discord
from discord.ext import commands

perms = discord.Intents().all()
client = commands.Bot(command_prefix="!", intents=perms) # Change The Prefix And Add İntents Permissions.

#Adding on_ready event
@client.event
async def on_ready():
    print("Im Ready!") # ready command.

#Adding Meme Commands.
@client.command()
async def meme(ctx):
    #Enter The Memes Url.
    meme1 = "1" # Use: meme1 = "url".
    meme2 = "2"
    meme3 = "3"
    meme4 = "4"
    meme5 = "5"
    meme6 = "6"
    meme7 = "7"
    meme8 = "8"
    meme9 = "9"
    meme10 = "10"
    meme11 = "11"
    meme12 = "12"
    meme13 = "13"
    meme14 = "14"
    meme15 = "15"
    meme16 = "16"
    meme17 = "17"
    meme18 = "18"
    meme19 = "19"
    meme20 = "20"
    meme21 = "21"
    meme22 = "22"
    meme23 = "23"
    meme24 = "24"
    meme25 = "25"
    
    random_meme = random.choice([meme1,
    meme2,
    meme3,
    meme4,
    meme5,
    meme6,
    meme7,
    meme8,
    meme9,
    meme10,
    meme11,
    meme12,
    meme13,
    meme14,
    meme15,
    meme16,
    meme17,
    meme18,
    meme19,
    meme20,
    meme21,
    meme22,
    meme23,
    meme24,
    meme25,
    ])
    print(random_meme)


client.run("token")