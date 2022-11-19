import discord
import os
from discord.ext import commands
import func
import keepalive

##########

bot = discord.Bot()

##########

@bot.event
async def on_ready():
  print(f'{bot.user} is running')

##########

@bot.command(description = 'Get help for Notchapple1703#3631')
async def help(ctx):
  await func.helper(ctx)

##########

pointgroup = bot.create_group('point')

##########

@pointgroup.command(description = 'Add points')
@commands.has_role('Commander')
async def add(ctx, name: discord.Member, point: int):
  await func.pointadd(ctx, name, point)
  await func.roleadd(ctx, name)

##########

@pointgroup.command(description = 'Remove points')
@commands.has_role('Commander')
async def remove(ctx, name: discord.Member, point: int):
  await func.pointremove(ctx, name, point)

##########

@pointgroup.command(description = 'Set points')
@commands.has_role('Commander')
async def set(ctx, name: discord.Member, point: int):
  await func.pointset(ctx, name, point)
  await func.roleadd(ctx, name)

##########

@pointgroup.command(description = 'Delete all points')
@commands.has_role('Commander')
async def delete(ctx, name: discord.Member):
  await func.pointdelete(ctx, name)

##########

permissiongroup = bot.create_group('permission')

##########

@permissiongroup.command(description = 'Add permission')
@commands.has_role('Commander')
async def add(ctx, name: discord.Member):
  await func.permissionadd(ctx, name)

##########

@permissiongroup.command(description = 'Remove permission')
@commands.has_role('Commander')
async def remove(ctx, name: discord.Member):
  await func.permissionremove(ctx, name)

##########

@bot.command(description = 'Leaderboard 🥳')
async def leaderboard(ctx):
  await func.leaderboard(ctx)

##########

while __name__ == '__main__':
  try:
    keepalive.keepalive()
    bot.run(os.environ['Token'])
  except discord.errors.HTTPException as e:
    print(e)
    os.system('kill 1')
keepalive()