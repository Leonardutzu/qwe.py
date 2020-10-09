import discord #Imports the discord module.
from discord.ext import commands #Imports discord extensions.

#The below code verifies the "client".
client = commands.Bot(command_prefix='q!')
#The below code stores the token.
token = "NzYzNjkyNTAwNDYwMjQwODk2.X37aEA.gJECe2eHPOMD98_PI1N1tKTVTZk"

#Bot online
@client.event
async def on_ready():
	print('Botu e acum Online')


'''
The below code displays if you have any errors publicly. This is useful if you don't want to display them in your output shell.
'''
@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('**Mentioneaza pe cineva sefu**.')
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("**Nu ai acces idiotule :))**")

"#Cu comanda asta banezi pe cnv gen
@client.command()
@commands.has_permissions(ban_members = True)
async def ban(ctx, member : discord.Member, *, reason = None):
    await member.ban(reason = reason)

#Cu asta dai afara pe cineva
@client.command()
@commands.has_permissions(kick_members = True)
async def kick(ctx, member : discord.Member, *, reason = None):
	await member.kick(reason=reason)
	await ctx.send(f'Utilizatorul {member.mention} a fost dat afara')

#Mute cmd


#The below code runs the bot.
client.run("NzYzNjkyNTAwNDYwMjQwODk2.X37aEA.gJECe2eHPOMD98_PI1N1tKTVTZk")
