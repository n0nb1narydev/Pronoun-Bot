import os
import discord
from dotenv import load_dotenv
from discord.ext import tasks, commands
import asyncio

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.members = True
bot = discord.Client(intents=intents)


@bot.event
async def on_ready():
    print('bot up and running')
    check_for_pronouns.start()

@tasks.loop(hours=24)
async def check_for_pronouns():
    for guild in bot.guilds:
        for member in guild.members:
            for role in member.roles: 
                if role.name == "They/Them" and "/" not in member.name: 
                    await member.edit(nick=f"{member.name} (They/Them)")
                    print("Nickname for they/them Changed")
                elif role.name == "She/Her" and "/" not in member.name:
                    await member.edit(nick=f"{member.name} (She/Her)")
                    print("Nickname for she/her Changed")
                elif role.name == "He/Him" and "/" not in member.name:
                    await member.edit(nick=f"{member.name} (He/Him)")
                    print("Nickname for he/him Changed")
                elif role.name == "Any Pronouns" and "(" not in member.name:
                    await member.edit(nick=f"{member.name} (Any Pronouns)")
                    print("Nickname for any pronouns Changed")

bot.run(TOKEN)