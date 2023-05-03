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
                                            'Use /insult whenever yarrrrr ready you scallywag!')


bot.run(secret_code)