import discord
from discord.ext import commands
from discord.ext.commands import MemberConverter
from discord.ext.commands import UserConverter

class Moderator(commands.Cog):
	def __init__(self,bot):
		self.bot= bot
		
	
	#COMMANDS:-
	
	#kick
	@commands.command()
	async def kick(self, ctx, member= None, *, reason= None):
		try:
			mem= await MemberConverter().convert(ctx, member)
			await mem.kick(reason=reason)
			await ctx.send(f'**{mem} has been kicked.**\nReason: {reason}')
		except:	
			flag= 1
			if member != None:
				if member[-5:-4]!='#':
					flag=0
				for digit in member[-4:]:
					if digit not in '1234567890':
						flag=0
						break
				if flag==0:
					await ctx.send('**Invalid syntax!**\nUse `-kick <member> <reason>`')		
				elif flag==1:
					await ctx.send(f'**{member}** is not a member of **{ctx.guild}.**')
			else:
				await ctx.send('**Invalid syntax!**\nUse `-kick <member> <reason>`')
	
	#ban
	@commands.command()
	async def ban(self, ctx, member= None, *, reason= None):
		try:
			mem= await MemberConverter().convert(ctx, member)
			await mem.ban(reason=reason)
			await ctx.send(f'**{mem} has been banned.**\nReason: {reason}')
		except:	
			flag= 1
			if member != None:
				if member[-5:-4]!='#':
					flag=0
				for digit in member[-4:]:
					if digit not in '1234567890':
						flag=0
						break
				if flag==0:
					await ctx.send('**Invalid syntax!**\nUse `-ban <member> <reason>`')		
				elif flag==1:
					await ctx.send(f'**{member}** is not a member of **{ctx.guild}.**')
			else:
				await ctx.send('**Invalid syntax!**\nUse `-ban <member> <reason>`')
	
	#unban
	@commands.command()
	async def unban(self, ctx, *, member= None):
		if member != None:
			m1,m2,mc1,mc2,flag='','',0,0,1
			for _member in member.split(' '):
				try:
					await ctx.send('hiiiiiiiiii')
					mem= self.bot.fetch_user(member)
					await ctx.send('hii')
					if len(await ctx.guild.bans()) > 0:
						for banned_entry in await ctx.guild.bans():
							
							await ctx.send('yo')
							await ctx.send(f'{mem}')
							if str(banned_entry.user).split('#') == str(mem.user).split('#'):
								await ctx.send('before_unban')
								await ctx.guild.unban(banned_entry.user)
								m1=m1+str(mem.user)+', '
								mc1+=1
							else:
								m2=m2+str(mem.user)+', '
								mc2+=1
					else:
						m2=m2+str(mem.user)+', '
						mc2+=1
				except:
					flag1,flag2=1,1
					#Brainy ifs here
					if _member.isdigit()==False:
						flag2=0
					if len(_member)<5:
						flag1=0
					elif _member[-5]!='#' or _member[-4:].isdigit()==False:
						flag1=0	
					if flag1==1 or flag2==1:
						await ctx.send('**Invalid syntax!**\nCheck the `username/id`')
					else:
						await ctx.send('**Invalid syntax!**\nUse `-unban <member1> <member2>....`')
					flag=0
					break
			#Big brain time
			m={mc1:'members',mc2:'members',1:'member',0:'members'}
			if (mc1>0 or mc2>0) and flag==1:
				await ctx.send(f'**Unbanned {mc1} {m[mc1]}:**\n'+m1[:-2]+f'\n**{mc2} {m[mc2]}** '+'**ain\'t banned:**\n'+m2[:-2])
		else:
			await ctx.send('Invalid syntax!\nUse `-unban <member1> <member2>....`')
	
	#purge
	@commands.command()
	async def purge(self, ctx, mem_amt= None, amount= None):
		try:
			if mem_amt != None:
				mem= await MemberConverter().convert(ctx, mem_amt)
				if amount.isdigit():
					amount=int(amount)
					msg=[]
					if amount > 1 and amount <=1000:
						async for m in ctx.channel.history(limit=1000):
							if len(msg) == amount:
								break
							if m.author == mem:
								msg.append(m)
						await ctx.channel.delete_messages(msg)
						await ctx.send(f'Deleted {amount} messages from {mem}.', delete_after= 1.3)
					elif amount == None or amount == 1:
						async for m in ctx.channel.history(limit=100):
							if len(msg) == amount:
								break
							if m.author == mem:
								msg.append(m)
						await ctx.channel.delete_messages(msg)
						await ctx.send(f'Deleted 1 message from {mem}.', delete_after=1.3)
					elif amount > 1000:
						await ctx.send('Tryna break the bot, huh :sweat_smile:\n**Purging limit is 1000 btw**', delete_after=1.3)
					elif amount <= 0:
						await ctx.message.delete()
						await ctx.send('Purging less than 1 message is stupid', delete_after= 1)
					try:
						await ctx.message.delete()
					except:
						pass
				else:
					await ctx.send('**Invalid syntax!**\nUse these:-\n`-purge <user> <amount>` ,or\n`-purge <amount>`')
			else:
				await ctx.channel.purge(limit=2)
				await ctx.send('Deleted 1 message.', delete_after=0.3)
				try:
					await ctx.message.delete()
				except:
					pass
		except:
			if mem_amt.isdigit():
				amount=int(mem_amt)
				if amount > 1 and amount <=1000:
					await ctx.channel.purge(limit=amount+1)
					await ctx.send(f'Deleted {amount} messages.', delete_after= 0.3)
				elif amount == 1:
					await ctx.channel.purge(limit=2)
					await ctx.send('Deleted 1 message.', delete_after=0.3)
				elif amount > 1000:
					await ctx.send('Tryna break the bot, huh :sweat_smile:\n**Purging limit is 1000 btw**', delete_after=1.3)
				elif amount <= 0:
					await ctx.send('Purging less than 1 message is stupid', delete_after= 1)
				try:
					await ctx.message.delete()
				except:
					pass
					
			else:
				await ctx.send('**Invalid syntax!**\nUse these:-\n`-purge <user> <amount>` ,or\n`-purge <amount>`')
		
	@commands.command()
	async def test(self,ctx, *, member=None):
		if member != None:
			m1,m2='',''
			for mem in member.split(' '):
				try:
					flag1,flag2=0,0
					try:
						for i in mem:
							if i in '1234567890':
								flag1=1
								await ctx.send('no._before')
								await ctx.guild.unban(int(mem))
								await ctx.send('no._after')
								m1=m1+mem+', '
					except:
						await ctx.send('wrong_syntax')
						m2=m2+mem+', '
						continue
					try:
						if member[-5]=='#' and member[-4:].isdigit():
							flag2=1
							await ctx.send('name_before')
							await ctx.guild.unban(member)
							await ctx.send('name_after')
							m1=m1+mem+', '
					except:
						await ctx.send('invalid syntax')
						m2=m2+mem+', '
						return
				except:
					await ctx.send('all_fail')
						
		else:
			await ctx.send('killed syntax')
			
										
	

							
							
def setup(bot):
	bot.add_cog(Moderator(bot))