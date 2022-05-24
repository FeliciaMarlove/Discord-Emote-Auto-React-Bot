from discord.ext import commands
from discord.utils import get

my_bot = commands.Bot(command_prefix='Voldemort')


@my_bot.event
async def on_ready():
    print("Voldemort bot is up and running")


@my_bot.event
async def on_message(message):
    await react_to_message(message, "voldemort", "voldemort_emoji")
    # await send_message(message, "I see what you're doing")


async def react_to_message(message, search_term, emote_name):
    if search_term in message.content.lower():
        emoji = get(my_bot.emojis, name=emote_name)
        await message.add_reaction(emoji=emoji)


async def send_message(message, new_message):
    # avoid an infinite loop if the bot posts messages
    if message.author == my_bot.user:
        return
    # send a message in the same channel
    await message.channel.send(new_message)


my_bot.run("APPLICATION_BOT_TOKEN")
