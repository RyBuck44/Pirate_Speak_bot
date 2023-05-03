import discord
from discord import app_commands
from discord.ext import commands
import os

secret_code = os.getenv('PS_TOKEN')
bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())


class ps(discord.Client):
    def __init__(self):
        super().__init__(intents=discord.Intents.default())
        self.synced = False

    async def on_ready(self):
        await tree.sync()
        self.synced = True
        print('Bot is online')


bot = ps()
tree = app_commands.CommandTree(bot)


@tree.command(name='ahoy', description='ARG! Shows ya how I work matey!')
async def self(interaction: discord.Interaction):
    await interaction.response.send_message('Time for a round of vinegar talk!\n'
                                            'Use /vinegar_talk whenever yarrrrr ready you scallywag!')


@tree.command(name='vinegar_talk', description='pick from my lists to craft the ultimate insult ya landlubber!')
async def self(interaction: discord.Interaction, start, middle, end):
    start = ['Idiotic', 'Parrot loving', 'Mumbling', 'Bleating',
             'Blathering', 'Sheep brained', 'Pin headed', 'Pig breathed',
             'Cricket sized', ]
    middle = ['Seaweed slurpin', 'Duck billed', 'Pus faced', 'Toothless',
              'Knuckle dragging', 'Cross eyed', 'Scurvey ridden', 'Clam tongued',
              'yellow bellied', ]
    end = ['Whale fart', 'Cow Pie', 'Sack o maggots', 'Swabber',
           'Cabin boy', 'waste of skin', 'Bag of vomit', 'Anchor headed',
           'Pieceof filth', ]


bot.run(secret_code)