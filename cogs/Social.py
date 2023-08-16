import discord
import random
from discord.ext import commands
from discord.ext.commands import MemberConverter

class Social(commands.Cog):
	def __init__(self, bot):
		self.bot=bot
	
	#EVENTS
	@commands.Cog.listener()
	async def on_ready(self):
		await self.bot.change_presence(status= discord.Status.idle, activity= discord.Game('Minecraft'))
	
	#COMMANDS
	@commands.command()
	async def hug(self, ctx, member= None):
		if member!= None:
			try:
				mem= await MemberConverter().convert(ctx, member)
				if [mem.name,mem.discriminator] == [ctx.author.name,ctx.author.discriminator]:
					embed= discord.Embed(title= f'Aww, lemme Hug you',color=discord.Color.red())
					embed.set_image(url='attachment://image.gif')
					await ctx.send(file=hug,embed=embed)
				elif mem != ctx.author:
					embed= discord.Embed(title=f'{ctx.author.name} Hugs {mem.name}!',color=discord.Color.red())
					embed.set_image(url='attachment://image.gif')
					await ctx.send(file=hug,embed=embed)		
			except:
				await ctx.send(f'**Invalid syntax!**\nUse `-hug <mention>`')
		else:
			await ctx.send(f'**Invalid syntax!**\nUse `-hug <mention>`')
			
			
	@commands.command()
	async def keth(self,ctx,subcommand,*args):
		j=subcommand
		if j=="<@622379845200117770>":
			j="KREPTRAHUL#8020"
		elif j=="<@779411840643760148>":
			j="HelperBot#8568"
		elif j=="<@473657428483899402>":
			j="AKplayz#5367"
		elif j=="<@788070321038688276>":
			j="KRAKENX121"
		elif j=="<@560123106149138452>":
			j="kartiku#2150"
		elif j=="<@694180427556061204>":
			j="Rex#1929"
		elif j=="<@701052068252876821>":
			j="SILPA#4353"
		elif j=="<@752233106836160652>":
			j="MightyAnik#0470"
		elif j=="<@344534401620901918>":
			j="ᘜᕼᓎSᖶᖇᙍᗅᑤᓎᘉ᙭#8256"
		elif j=="<@778320067150610443>":
			j="Minati#1978"
		elif j=="<@797019907937140758>":
			j="Inori-san#9408"
		elif j=="<@774891058223251476>":
			j="Thundermines#7543"
		elif j=="<@737333355359502348>":
			j="sangox07#0342"
		elif j=="<@757469767136444479>":
			j="Ark々Thunder#7991"
		embed=discord.Embed(title=str(ctx.author)+" hugs "+str(j),color=discord.Color.teal())
		vale = random.randint(1,5)
		value=1
		if value==1:
			embed.set_image(url="https://tenor.com/view/gif-19916097")
		if value==2:
			embed.set_image(url="https://i.imgur.com/f8C9M7n.gif")
		if value==3:
			embed.set_image(url="https://cdn.weeb.sh/images/SknauOQwb.gif")
		if value==4:
			embed.set_image(url="https://cdn.weeb.sh/images/rkx1dJ25z.gif")
		if value==5:
			embed.set_image(url="https://media.tenor.com/images/ca88f916b116711c60bb23b8eb608694/tenor.gif")
		await ctx.send(embed=embed)
		await ctx.send(f'{value}')

	@commands.command()
	async def guilds(self,ctx):
		await ctx.send(f'{self.bot.guilds}')

	@commands.command()
	async def hug2(self, ctx, member= None):
		'''
		pr= [
		 shhs
		  hsshu
		   hshs
		
		#list of url here
		
]
		rand_hug=random.choice(pr)
		'''
		rand_hug='https://tenor.com/view/gif-19916104'
		if member!= None:
			try:
				mem= await MemberConverter().convert(ctx, member)
				if ctx.author == mem:
					embed= discord.Embed(title= f'Aww, lemme Hug you',color=discord.Color.red())
				elif mem != ctx.author:
					embed= discord.Embed(title=f'{ctx.author.name} Hugs {mem.name}!',color=discord.Color.red())
				embed.set_image(url=rand_hug)
				await ctx.send(embed=embed)
			except:
				await ctx.send(f'**Invalid syntax!**\nUse `-hug <mention>`')
		else:
			await ctx.send(f'**Invalid syntax!**\nUse `-hug <mention>`')
	
			

		
						
#	python /storage/emulated/0/Xender/Python_programs/Celani/celani.py		
def setup(bot):
	bot.add_cog(Social(bot))
	
#hugs
'''
https://giphy.com/gifs/bts-v-bangtan-boys-idmXZuW33WlWw

https://giphy.com/gifs/thebachelorau-the-bachelor-3o7TKpaCWO5sTsNZ4Y

https://giphy.com/gifs/ZQN9jsRWp1M76

https://giphy.com/gifs/barkpost-mwJX5dRdsrefu

https://giphy.com/gifs/cats-gl8ymnpv4Sqha

https://giphy.com/gifs/hug-cat-cute-f6y4qvdxwEDx6

https://giphy.com/gifs/anime-boy-LIqFOpO9Qh0uA

https://giphy.com/gifs/dog-hug-f4HpCDvF84oh2
'''