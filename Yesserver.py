import discord
from discord import app_commands
from discord.ext import commands
import os
import re
count_file = "yes.txt"
def find_best_count():
    if os.path.exists(count_file):
        with open(count_file, "r") as f:
            try:
                return int(f.read().strip())
            except ValueError:
                return 0
    return 0
def save_best_count(count):
    with open(count_file, "w") as f:
        f.write(str(count))
def is_yes_best(message):
    pattern = r"(?i)(y\s?e\s?s)[^a-zA-Z]*(b\s?e\s?s\s?t)"
    match = re.search(pattern, message)
    if match:
        print(f"Regex Match Found: {message}")  # Log matching messages
    return match is not None
yes_best_counter = find_best_count()
intents = discord.Intents.default()
intents.message_content = True  # Ensure message content intent is enabled
bot = commands.Bot(command_prefix="", intents=intents)  # Empty prefix for slash commands
#conputer stuff
@bot.tree.command(name="yes-best", description="Show the count of 'yes best'")
async def yes_best(interaction: discord.Interaction):
    global yes_best_counter
    await interaction.response.send_message(
        f"'Yes Best' has been said {yes_best_counter} times!"
    )
@bot.event
async def on_message(message: discord.Message):
    global yes_best_counter
    if message.author.bot:
        return
    print(f"Received message in channel: {message.channel.name}")
    print(f"Message content: {message.content}")
    if is_yes_best(message.content):
        print(f"Counter before update: {yes_best_counter}")  # Log counter before update
        yes_best_counter += 1
        save_best_count(yes_best_counter)
        print(f"Counter after update: {yes_best_counter}")  # Log counter after update
    await bot.process_commands(message)
@bot.event
async def on_ready():
    await bot.tree.sync()
    print(f'Logged in as {bot.user}. Slash commands are synced and ready!')

bot.run("(secret_key)")
