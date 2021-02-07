from bot_token import token
import discord as db
import discord.ext

Client = db.Client()

@Client.event
async def on_ready():
    print("bot is opgestart")
    activity = db.Activity(type=db.ActivityType.streaming, name='gekkebult')
    await Client.change_presence(activity=activity)

@Client.event
async def on_message(message):
    if message.content.startswith("!hoi"):
      await message.channel.send("Hallo")

Client.run(token)
