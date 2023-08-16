'''
@commands.command()
async def test(ctx, member= None):
	from discord.ext.commands import MemberConverter
	try:
		_mem= await MemberConverter().convert(ctx,member)
		await ctx.send(f'{_mem}')
	except:
		await ctx.send('except is executing')


for filename in os.listdir('/storage/emulated/0/Xender/Python_programs/Celani/cogs'):
	if filename.startswith('Moderator'):
		bot.load_extension(f'cogs.{filename[:-3]}')


for filename in os.listdir('/storage/emulated/0/Xender/Python_programs/Celani/cogs'):
	if filename.endswith('.py'):
		bot.load_extension(f'cogs.{filename[:-3]}')
'''
'''
embed = discord.Embed(title="Title", description="Desc", color=0x00ff00) #creates embed
file = discord.File("path/to/image/file.png", filename="image.png")
embed.set_image(url="attachment://image.png")
await ctx.send(file=file, embed=embed)
'''