import os
import discord
from website import keep_alive
import json

from utils import default
from utils.data import Bot, HelpFormat

config = default.config()
print("Logging in...")

def get_prefix(client, message):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)

    return prefixes[str(message.guild.id)]

bot = Bot(
    command_prefix=get_prefix, prefix=config["prefix"],
    owner_ids=config["owners"], command_attrs=dict(hidden=True), help_command=HelpFormat(),
    intents=discord.Intents(  # kwargs found at https://discordpy.readthedocs.io/en/latest/api.html?highlight=intents#discord.Intents
        guilds=True, members=True, messages=True, reactions=True, presences=True
    )
)

for file in os.listdir("cogs"):
    if file.endswith(".py"):
        name = file[:-3]
        bot.load_extension(f"cogs.{name}")

keep_alive()

try:
    bot.run(os.getenv('TOKEN'))
except Exception as e:
    print(f'Error when logging in: {e}')
