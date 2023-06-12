import discord
import asyncio

# Replace 'YOUR_TOKEN' with your actual bot token
TOKEN = 'YOUR_TOKEN'
# Replace 'YOUR_CHANNEL_ID' with the ID of the channel where you want to send the message
CHANNEL_ID = YOUR_CHANNEL_ID

# Create a bot instance
intents = discord.Intents.default()
intents.typing = False
intents.presences = False
bot = discord.Client(intents=intents)

# Event triggered when the bot is ready
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} ({bot.user.id})')
    channel = bot.get_channel(CHANNEL_ID)
    await channel.send('Hello World!')

# Run the bot
bot.run(TOKEN)
