import discord
import random
from config import TOKEN
from discord.ext.commands import Bot
from discord.ext import commands

client = Bot(command_prefix="!", pm_help = False)

compliments = ["You're doing amazing sweetie",
               "Don't give up, you'll do great !"
               "You are powerful",
               "You are the strongest motherfucker ever",
               "You do amazing at anything you do",
               "You're the best !",
               "You're an amazing friend.",
               "All your friends love you",
               "You fight until the end !",
               "You are one tough cookie !",
               "Keep doing your best !",
               "Your friends love and support you.",
               "You're kind and amazing.",
               "You can do this !",
               "You go you !"]
@client.event
async def on_ready():
    print("All ready boss !")

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)

    if message.content.startswith('!mousse'):
        msg = 'https://www.youtube.com/watch?v=lxyy_njLmxw'.format(message)
        await client.send_message(message.channel, msg)

    if message.content.startswith('!ping'):
        msg = ':ping_pong: Pong !'.format(message)
        await client.send_message(message.channel, msg)

    if message.content.startswith('!AH'):
        await client.send_file(message.channel,'AH.gif')

    if message.content.startswith('!gay'):
        await client.send_file(message.channel,'gay.gif')

    if message.content.startswith("D'abord la Mortal ?"):
        await client.send_message(message.channel,'ENSUITE LE MONDE !')

    if message.content.startswith("Il est comment le beurre ?"):
        await client.send_message(message.channel,'SALÉ !')

    if message.content.startswith("!compliments"):
        await client.send_message(message.channel,message.author.mention+' '+random.choice(compliments))

    if 'sun' in message.content:
        await client.send_message(message.channel,"Rikaaaaaaaah")

    if 'bah bien' in message.content:
        await client.send_message(message.channel, "AH BAH C'EST BIEN NILS, SUPER POUR L'APPAREIL PHOTO ! IL EST FOUTU C'EST PAS GRAVE HEIN")

    if 'mousse' in message.content:
        await client.send_message(message.channel,"ATTENTION A LA MOUSSE !")



client.run(TOKEN)
