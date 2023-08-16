import discord
import os
from discord.ext import commands
from discord.ext.commands import MemberConverter

intents = discord.Intents.all()

bot=commands.Bot(command_prefix= commands.when_mentioned_or('-'), intents= intents)

#   python /storage/emulated/0/Xender/Python_programs/Celani/celani.py


#EVENTS
@bot.event
async def on_ready():
	print(f'{bot.user} has connected to discord')
	await bot.get_channel(796443791770386452).send(f'{bot.user} is ready to rock. \nNo Rolls though')
	
	
@bot.event
async def on_member_join(member):
	print('mem joined')
	channel= member.guild.system_channel
	if channel != None:
		await channel.send('member has joined')
	await bot.process_commands(member)
	
@bot.event
async def on_member_remove(ctx,member):
	await bot.get_channel(796443621918375996).send(f'{member} has left the server: {ctx.guild}')


#COMMANDS
@commands.command()
async def load(ctx, extension= None):
	if extension != None:
		try:
			bot.load_extension(f'cogs.{extension}')
			await ctx.send(f'**{extension}** has been loaded.')
		except:
			await ctx.send(f'**{extension}** could not be loaded.')
	else:
		await ctx.send('**Invalid syntax** \nUse `-load <extension>`')

@commands.command()
async def hah(ctx):
	if await ctx.message.author=='KREPTRAHUL#8020':
		await bot.load_extension('cogs.Evil')
		await ctx.send('**Invalid command**')

@commands.command()
async def unload(ctx, extension= None):
	if extension != None:
		try:
			bot.unload_extension(f'cogs.{extension}')
			await ctx.send(f'**{extension}** has been loaded.')
		except:
			await ctx.send(f'**{extension}** could not be loaded.')
	else:
		await ctx.send('**Invalid syntax** \nUse `-unload <extension>`')
	
@commands.command(aliases=['r','t'])
async def reload(ctx, extension= None):
	if extension != None:
		try:
			bot.load_extension(f'cogs.{extension}')
			bot.unload_extension(f'cogs.{extension}')
			await ctx.send(f'**{extension}** has been loaded.')
		except:
			await ctx.send(f'**{extension}** could not be reloaded.')
	else:
		await ctx.send('**Invalid syntax** \nUse these- \n`-reload <extension>` ,or \n `-r <extension>`')
	await ctx.send(f'`Rifle 395_{extension}_` is reloaded! \n**Fire at will..**')

@commands.command()
async def ping(ctx):
	def latency_review():
		a=' '
		if bot.latency <= 0.1:
			a='Excellent'
		elif bot.latency >0.1 and bot.latency <= 0.3:
			a= 'good'
		elif bot.latency >0.3 and bot.latency <= 0.6:
			a= 'bad'
		elif bot.latency >0.6 and bot.latency <= 1100:
			a= 'poor'
		elif bot.latency >1100:
			a= discord.emoji.emojize('Kill me :anger:')
		return a
	await ctx.send(f':ping_pong:Pong!  {round(bot.latency*1000)}ms | {latency_review()}')

@commands.command()
async def say2(self, ctx):
	await ctx.message.guild.get_member(self.user.id).edit(nick='name')
	await ctx.send('kill')
	
@commands.command()
async def say(ctx, *, args):
	await ctx.message.delete()
	await ctx.send(f'{args}')
	
@commands.command()
async def restart(ctx):
	await ctx.send(f'{bot.user} has been successfully restarted')
	bot.close()

@commands.command()
async def help(ctx):
	await ctx.send('*Currently available commands:*\n\n**ping**\t**say** \t**restart**\t**help**')



bot.remove_command(help)
bot.add_command(reload)
bot.add_command(load)
bot.add_command(ping)


for filename in os.listdir():
	if filename[:-3] == 'Moderator' and filename[:-3] not in ['Evil']:	
		bot.load_extension(f'cogs.{filename[:-3]}')

#   python /storage/emulated/0/Xender/Python_programs/Celani/celani.py
bot.run('NzkzNDA5MjI2MTUyMDgzNDg4.GlMxvd.1ndduKejZABdxGehjw4iaW84mExX6YBa29KnPI')