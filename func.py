import discord
from discord.ext import commands
from discord.ext.pages import Paginator, PaginatorButton
from replit import db

##########

async def helper(ctx):
  embed = discord.Embed(
    title = 'Commands 💻',
    color = discord.Colour.blurple()
  )

  embed.add_field(name = '**Add point:**', value = '*/point add [name] [point]*')
  embed.add_field(name = '**Remove point:**', value = '*/point remove [name] [point]*')
  embed.add_field(name = '**Set point:**', value = '*/point set [name] [point]*')
  embed.add_field(name = '**Delete point:**', value = '*/point delete [name]*')
  embed.add_field(name = '**Add permission:**', value = '*/permission add [name]*')
  embed.add_field(name = '**Remove permission:**', value = '*/permission remove [name]*')
  embed.add_field(name = '**Leaderboard:**', value = '*/leaderboard*')

  embed.set_thumbnail(url = 'https://th.bing.com/th/id/R.68bc19b49c678904e7b1d6e574e25753?rik=eyN%2bhKxJEuWgzg&pid=ImgRaw&r=0')
    
  await ctx.respond(embed = embed)

##########

async def roleadd(ctx, name):
  i = str(name)
  
  if db[i] >= 1000:
    role = discord.utils.get(ctx.guild.roles, name = 'Territorial Player')
    if role not in name.roles:
      await name.add_roles(role)

  if db[i] >= 2000:
    role = discord.utils.get(ctx.guild.roles, name = 'Territorial Enjoyer')
    if role not in name.roles:
      await name.add_roles(role)

  if db[i] >= 3000:
    role = discord.utils.get(ctx.guild.roles, name = 'Territorial Grinder')
    if role not in name.roles:
      await name.add_roles(role)

  if db[i] >= 5000:
    role = discord.utils.get(ctx.guild.roles, name = 'Territorial Master')
    if role not in name.roles:
      await name.add_roles(role)

  if db[i] >= 10000:
    role = discord.utils.get(ctx.guild.roles, name = 'Territorial God')
    if role not in name.roles:
      await name.add_roles(role)

  if db[i] >= 20000:
    role = discord.utils.get(ctx.guild.roles, name = 'Ultimate Corgi')
    if role not in name.roles:
      await name.add_roles(role)

##########

async def pointadd(ctx, name, point):
  i = str(name)
  
  if i not in db.keys():
    db[i] = 0
  db[i] += point

  embed = discord.Embed(
    description = f'✅ Added 🏅 {point} to {name.mention}, now you have 🏅 {db[i]}',
    color = discord.Colour.brand_green()
  )

  embed.set_author(name = ctx.author, icon_url = ctx.author.avatar)

  await ctx.respond(embed = embed)

##########

async def pointremove(ctx, name, point):
  i = str(name)
  
  if i not in db.keys():
    db[i] = point
    
  db[i] -= point
  
  if db[i] < 0:
    db[i] = 0

  embed = discord.Embed(
    description = f'✅ Removed 🏅 {point} from {name.mention}, now you have 🏅 {db[i]}',
    color = discord.Colour.brand_red()
  )

  embed.set_author(name = ctx.author, icon_url = ctx.author.avatar)

  await ctx.respond(embed = embed)

##########

async def pointset(ctx, name, point):
  i = str(name)
  db[i] = point

  embed = discord.Embed(
    description = f'✅ Set 🏅 {point} for {name.mention}, now you have 🏅 {db[i]}',
    color = discord.Colour.blue()
    )

  embed.set_author(name = ctx.author, icon_url = ctx.author.avatar)

  await ctx.respond(embed = embed)

##########

async def pointdelete(ctx, name):
  i = str(name)
  del db[i]

  embed = discord.Embed(
    description = f'✅ Deleted all {name.mention}\'s points, now you have 🏅 0',
    color = discord.Colour.yellow()
  )

  embed.set_author(name = ctx.author, icon_url = ctx.author.avatar)

  await ctx.respond(embed = embed)

##########

async def permissionadd(ctx, name):
  role = discord.utils.get(ctx.guild.roles, name = 'Commander')
  await name.add_roles(role)

  embed = discord.Embed(
    description = f'✅ {name.mention}\'s wish is my command',
    color = discord.Colour.brand_green()
  )

  embed.set_author(name = ctx.author, icon_url = ctx.author.avatar)

  await ctx.respond(embed = embed)

##########

async def permissionremove(ctx, name):
  role = discord.utils.get(ctx.guild.roles, name = 'Commander')
  await name.remove_roles(role)

  embed = discord.Embed(
    description = f'✅ Goodbye {name.mention}',
    color = discord.Colour.brand_red()
  )

  embed.set_author(name = ctx.author, icon_url = ctx.author.avatar)

  await ctx.respond(embed = embed)

##########

async def leaderboard(ctx):
  name = list(db.keys())
  point = [db[i] for i in name]
  
  leaderdict = dict(zip(name, point))
  leaderdict = {i[0]: i[1] for i in sorted(leaderdict.items(), key = lambda x: (-x[1], x[0]))}
  
  leaderlist = list(leaderdict.items())
  
  leaderchunk = []

  for i in range(0, len(leaderlist), 2):
    leaderchunk.append(leaderlist[i:i + 2])

  embedlist = []

  for innerlist in leaderchunk:
    leaderstring = ''''''
    
    for item in innerlist:
      leaderstring += f'**{list(leaderdict.keys()).index(item[0]) + 1}.** {item[0]} • 🏅 {item[1]}\n'
    try:
      rank = list(leaderdict.keys()).index(str(ctx.author)) + 1
    except:
      rank = 'Not Available'

    embed = discord.Embed(
      color = discord.Colour.blue(),
      description = f'{leaderstring}\n{ctx.author}\'s rank: **{rank}**'
    )

    embed.set_author(name = 'Corgi Circus Leaderboard', icon_url = 'https://th.bing.com/th/id/R.ba8bfdbe80cc37713774c525ad0c47c0?rik=sC4Sc3mszjVu%2fw&pid=ImgRaw&r=0')

    embedlist.append(embed)

  

  paginator = Paginator(pages = embedlist)

  await paginator.respond(ctx.interaction)