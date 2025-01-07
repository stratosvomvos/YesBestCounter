import discord
from discord.ext import commands
import os
import re
# discord stuff idk
intents = discord.Intents.default()
intents.messages = True
bot = commands.Bot(command_prefix=None, intents=intents)

count_file = "yes.txt"

def findBest():
    if os.path.exists(count_file):
        with open(count_file, "r") as f:
            try:
                return int(f.read().strip())
            except:
                return 0
    return 0

def saveBest(c):
    with open(count_file, "w") as f:
        f.write(str(c))

yes_best_counter = findBest()
# regex to find yes best variations
def idklol(message):
    p = r"(?i)(y\s?e\s?s)[^a-zA-Z]*(b\s?e\s?s\s?t)"
    return re.search(p, message) != None

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")
# counts how many time yes best is said
@bot.event
async def on_message(message):
    global yes_best_counter
    if message.channel.name == "yes-best" and idklol(message.content):
        yes_best_counter += 1
        saveBest(yes_best_counter)
    await bot.process_commands(message)
# slash command for yes best
@bot.slash_command(name="yes-best", description="Count")
async def yes_best(ctx):
    await ctx.respond(f"{yes_best_counter}")
# runs bot with secret token
bot.run("(secret_key)")
