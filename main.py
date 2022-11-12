import discord
import os

class BotClient(discord.Client):
  async def on_ready(self):
    print('We have logged in as {self.user}!')

  async def on_message(self, message):
    if message.author == client.user:
      return
    if message.content.startswith('$hello'):
      await message.channel.send('hello!')

intents = discord.Intents.default()
intents.message_content = True

client = BotClient(intents = intents)
client.run(os.getenv('AUTH_TOKEN'))