import discord
from discord.ext import commands
import random

client = commands.Bot(command_prefix = ".")

@client.event
async def on_ready():
	await client.change_presence(status=discord.Status.online, activity=discord.Game('Made by Pizza#3035'))
	print('Bot is ready.')
	
@client.event
async def on_member_join(member):
	
    for channel in member.guild.channels:
        if str(channel) == "welcome":
            await channel.send(f'Welcome {member.mention} to the server!')
	
	
@client.event
async def on_member_remove(member):
	print(f'{member} has left a server.')
	
	
@client.command()
async def shift(ctx, link = "I/T"):
	await ctx.channel.purge(limit=1)
	role = discord.utils.get(ctx.guild.roles, name="[Starcade] Supervisor")
	if role in ctx.author.roles:
		await ctx.send(f'''Hello Arcaders!
I'm currently hosting a shift down at the arcade! 
If you would like to attend make sure to join me!

:link:  {link}
@here ''')
	else:
		await ctx.send('You lack the permissions.')





@client.command(aliases=['Ping'])
async def ping(ctx):
	await ctx.send(f'Pong! {round(client.latency * 1000)}ms')
	
	
@client.command(aliases=['Hello','Hi','hi'])
async def hello(ctx):
	await ctx.send('Hello!')




	
client.run('NTgxNDQxMjU3MjIyNzAxMDc2.XOfTlQ.GqNdn4fp4BXxIQkMdL9MbSaaOME')
