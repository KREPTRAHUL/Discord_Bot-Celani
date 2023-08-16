import discord
import emoji
import os
from discord.ext import commands
from discord.ext.commands import MemberConverter

bot=commands.Bot(command_prefix= commands.when_mentioned_or('-'))


@bot.event
async def on_ready():
	print(f'{bot.user} has connected to discord.')
	

@bot.command()
async def test2(ctx, mem_amt= None, amount= None, *, args= None):
	if mem_amt!= None:
		try:
			mem= await MemberConverter().convert(ctx, mem_amt)
			await ctx.send(mem)
			if amount.isdigit():
				amount= int(amount)
				await ctx.message.delete()
				if amount > 1 and amount <=1000:
					await ctx.channel.purge(limit=amount,check= lambda message: message.author == mem)
					await ctx.send('after_first_if')
					await ctx.send(f'Deleted {amount} messages from {mem_amt.mention}.', delete_after= 0.4)
				elif amount == 1:
					await ctx.channel.purge(limit=1,check= lambda message: message.author == mem)
					await ctx.send('Deleted 1 message from {mem_amt.mention}.', delete_after=0.4)
				elif amount > 1000:
					await ctx.send(emoji.emojize('Tryna break the bot, huh :sweat_smile:\n**Purging limit is 1000 btw**'), delete_after=1.2)
				elif amount <= 0:
					await ctx.send('Purging less than 1 message is stupid', delete_after= 2)
			else:
				await ctx.message.delete()
				await ctx.channel.purge(limit=1,check= lambda message: message.author == mem)
				await ctx.send('Deleted 1 message.', delete_after= 0.4)
		except:
			if mem_amt.isdigit():
				await ctx.send('yes')
				mem_amt= int(mem_amt)
				await ctx.message.delete()
				if mem_amt > 1 and mem_amt <=1000:
					await ctx.channel.purge(limit=mem_amt)
					await ctx.send(f'Deleted {mem_amt} messages.', delete_after= 0.4)
				elif mem_amt == 1:
					await ctx.channel.purge(limit=1)
					await ctx.send('Deleted 1 message.', delete_after=0.4)
				elif mem_amt > 1000:
					await ctx.send(emoji.emojize('Tryna break the bot, huh :sweat_smile:\n**Purging limit is 1000 btw**'), delete_after=1.2)
				elif mem_amt <= 0:
					await ctx.send('Purging less than 1 message is stupid', delete_after= 2)
			else:
				await ctx.send('second_last_else')
				await ctx.message.delete()
				await ctx.channel.purge(limit=1)
				await ctx.send('Deleted 1 message.', delete_after= 0.4)
	else:
		await ctx.send('last_else')
		await ctx.message.delete()
		await ctx.channel.purge(limit=1)
		await ctx.send('Deleted 1 message.', delete_after= 0.4)
			
@bot.command()
async def test3(ctx, member,amount):
	mem= await MemberConverter().convert(ctx,member)
	await ctx.message.delete()
	channel = ctx.channel.history(limit=None)
	msg=[]
	print(channel)
'''
	for message in channel:
		if message.author == mem:
			msg.append(message)
	await ctx.message.channel.delete_messages(msg)
'''

#   python /storage/emulated/0/Xender/Python_programs/Celani/Tests.py

bot.run('NzkzNDA5MjI2MTUyMDgzNDg4.X-r17A.un-qE7e-sxqrcSCtB7ToPRLZ51M')