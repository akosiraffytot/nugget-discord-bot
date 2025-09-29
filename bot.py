import discord
from discord import app_commands
import os
import requests

intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

@client.event
async def on_ready():
    await tree.sync()  # syncs commands with Discord
    print(f"Logged in as {client.user}")

# Slash command: /fact
@tree.command(name="fact", description="Get a random fun fact")
async def fact(interaction: discord.Interaction):
    response = requests.get("https://uselessfacts.jsph.pl/random.json?language=en")
    if response.status_code == 200:
        fact = response.json().get("text")
        await interaction.response.send_message(f"{fact}")
    else:
        await interaction.response.send_message("⚠️ Couldn't fetch a fact right now!")

client.run(os.getenv("DISCORD_TOKEN"))
