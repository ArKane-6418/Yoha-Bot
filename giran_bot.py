import discord
import time
import asyncio
import random
import os
from discord.ext import commands

# id = 600408072837660717
messages = joined = 0

# client = discord.Client()
print(os.listdir())

bot = commands.Bot(command_prefix = "%")


@bot.event
async def on_ready():
    print(f"{bot.user.name} has descended.")
    channelObject = discord.utils.get(bot.get_all_channels(), guild__name='Bot Test Server', name='bot-commands')
    bot.loop.create_task(loop(channelObject))


async def loop(channelObject):
    while True:
        await asyncio.sleep(86400)
        await channelObject.send("Come Riri, descend with me.")


@bot.command(name='hello')
async def hello(ctx):
    await ctx.send(f"Hello little demon, {ctx.author.mention}.")


@bot.command(name='yohahelp')
async def yohahelp(ctx):
    embedded = discord.Embed(title="Help:", description="Useful commands")
    embedded.set_image(url = "https://cdn.discordapp.com/attachments/483106614724001796/604040877458980980/Yoha.png")
    embedded.add_field(name="yoshiko", value = "Best dork", inline = True)
    embedded.add_field(name="%lili", value = "Best little demon", inline = True)
    embedded.add_field(name="yohane", value = "Fallen Angel Yohane", inline = True)
    embedded.add_field(name="guilty kiss", value = "Best subunit", inline = True)
    embedded.add_field(name="jimo", value = "Ai", inline = True)
    embedded.add_field(name = "%yohasay <message>", value = "Messages for bot to say", inline = True)
    await ctx.send(content=None, embed=embedded)


@bot.command(name='lili')
async def lili(ctx):
    await ctx.send("Descend with me, little demons <:datenshi:600462901819736064> <:YohaneV:600463372802326539>")


@bot.event
async def on_member_join(member):
    global joined
    joined += 1
    '''Bot Test Server: welcome channel ID, message
       Casual Server: testing channel, message
    '''
    guild_dict = {583864496964108288: [583873540772593675, f"""Welcome to Hell Zone, {member.mention}!"""],
                  532048598888742924: [603809782742384652, f"""Welcome to Hell Zone, {member.mention}!"""]}
    for guild_id in guild_dict:
        if guild_id == member.guild.id:
            await bot.get_channel(guild_dict[guild_id][0]).send(guild_dict[guild_id][1])
            print(str(bot.get_guild(guild_id)))


@bot.command(name="yohasay")
async def say(ctx, msg):
    content = ctx.message.content.replace("%yohasay ", "")
    await ctx.message.delete()
    await ctx.send(content)


@bot.event
async def on_message(message):

    channels = ["bot-commands", "testing"]

    if str(message.channel) in channels and not message.author.bot:
        if message.content.lower().find("yoshiko") != -1:
            await message.channel.send("Dakara Yohane yo!")
        elif message.content.lower() == "yohane":
            await message.channel.send("Shoukan!")
        elif message.content.lower() == "guilty kiss":
            await message.channel.send("<:YohaYay:600464932382834707><:RikoYay:610687363663790080>"
                                       "<:MariYay:610687363647275008>")
        elif message.content.lower() == "jimo":
            await message.channel.send("<:Ai:600462114183839761>")
        elif message.content.lower().find("riko") != -1:
            await message.channel.send("My favourite little demon~")
        elif message.content.lower() == "roll":
            await message.channel.send("<a:yoharoll:600470605610876941>")
        elif message.content.lower() == "bongo":
            await message.channel.send("<a:bongoruby:600470496211107840>")
        elif message.content.lower().find("zura") != -1:
        elif message.content.lower().find("zura") != -1:
            await message.channel.send("<a:yaypotatozura:600473598679056395>")
        elif message.content.lower() == "aquarium ruby":
            await message.channel.send(file = discord.File("./Images/Aquarium Ruby.gif"))
        elif message.content.lower() == "aquarium maru":
            await message.channel.send(file = discord.File("./Images/Aquarium Maru.gif"))
        elif message.content.lower() == "aquarium yoha":
            await message.channel.send(file = discord.File("./Images/Aquarium Yoha.gif"))

    await bot.process_commands(message)

file_object = open("key.txt", "r")
bot.run(file_object.read().strip())
