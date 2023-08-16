import discord
from discord.ext import commands

class Evil(commands.Cog):
	def __init__(self,bot):
		self.bot= bot

	
#monika
	@commands.command()
	async def monika(self, ctx, amt= None):
		if amt!= None:
			if amt.isdigit():
				amt= int(amt)
				for a in range(0,amt):
					await ctx.channel.purge(limit=1)
			else:
				await ctx.send('**Invalid syntax!**\nUse `-monika <amount>`')
		else:
			await ctx.send('**Invalid syntax!**\nUse `-monika <amount>`')	
		
#bunk
	@commands.command()
	async def bunk(self, ctx, member=None):
		if member != None:
			try:
				await ctx.message.delete()
			except:
				pass
			try:
				mem= await MemberConverter().convert(ctx,member)
				while member != 'stop':
					await ctx.send(mem.mention)
					await ctx.guild.purge(limit=1)
			except:
				while member != 'stop':
					await ctx.send(member)
					await ctx.channel.purge(limit=1)
		else:
			await ctx.send('**Invalid syntax** \nUse `-bunk <member> <times>`')			

#bunk_v2
	@commands.command()
	async def bunk_v2(self, ctx, *, member=None):
		if member != None:
			try:
				await ctx.message.delete()
			except:
				pass
			try:
				mem= await MemberConverter().convert(ctx,member)
				while member != 'stop':
					await ctx.send(mem.mention, delete_after= 0.01)
					
			except:
				while member != 'stop':
					await ctx.send(member, delete_after= 0.01)
					
		else:
			await ctx.send('**Invalid syntax** \nUse `-bunk <member> <times>`')		
			
			
			
			
	def setup(bot):
		bot.add_cog(Evil(bot))