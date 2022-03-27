# Discord Stream Spoofer - By Celvis#1772

# Import Moduals
import discord, os, keep_alive, asyncio, datetime, pytz

# Pull
from discord.ext import tasks, commands

client = commands.Bot(
  command_prefix=':',
  self_bot=True
)


# Display
@client.event
async def on_connect():
  # Put your title in "Stream spoofer - Celvis#1772" and link to redirect in "https://www.youtube.com/watch?v=sk25VISwSfk"
  await client.change_presence(activity = discord.Streaming(name = "Stream spoofer - Celvis#1772" , url = "https://www.youtube.com/watch?v=sk25VISwSfk"))

# Keep stream running ~Keep_alive.py~
keep_alive.keep_alive()
client.run(os.getenv("token"), bot=False)