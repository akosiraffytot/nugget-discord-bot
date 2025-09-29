import discord
import os
import asyncio
import requests

TOKEN = os.getenv("DISCORD_TOKEN")
CHANNEL_ID = int(os.getenv("CHANNEL_ID"))

async def main():
    intents = discord.Intents.default()
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        try:
            # Fetch a random fact from API
            response = requests.get("https://uselessfacts.jsph.pl/random.json?language=en")
            fact = response.json().get("text", "Could not fetch a fact today 🤷")

            # Send it to the channel
            channel = client.get_channel(CHANNEL_ID)
            await channel.send(f"🤔 Daily Fun Fact: {fact}")


        except Exception as e:
            print(f"Error: {e}")




        finally:
            await client.close()  # Exit after sending

    await client.start(TOKEN)

asyncio.run(main())
