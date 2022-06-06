import discord
from discord import member
from discord.ext import commands
from discord.message import Message
from discord.utils import get    
from discord import Member
from discord.ext.commands import has_permissions, MissingPermissions
from keep_alive import keep_alive

client = commands.Bot("%")
client.remove_command('help')

@client.event
async def on_ready():
  print('Logged on as {0}!'.format(client.user))
  await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="seus comandos"))


@client.event
async def on_message(message):
  content = message.content.lower()
  channel = message.channel
  user = message.author.id
  await client.process_commands(message)


@client.command(name="couple")
async def married_couple(ctx, member1 : discord.Member, member2 : discord.Member):

  url_image = "https://img1.picmix.com/output/stamp/normal/6/1/7/5/555716_61b8e.gif"
  couple = discord.Embed(title=f"{ctx.author.name} declarou:", description=f"Hoje {member1.mention} e {member2.mention}estão oficialmente  casados")
  couple.set_image(url=url_image)
  couple.set_footer(text="(っ ͡❛ 👅 ͡❛)っ🎔  Aproveitem o dia pombinhos!! (っ ͡❛ 👅 ͡❛)っ🎔")
  await ctx.message.delete()
  await ctx.channel.send(embed=couple)

@client.command(name="menu")
async def menu(ctx):
  menu = discord.Embed(title=f"{ctx.guild.name}", description=f"Oiee {ctx.author.mention}, sou a sextinha <3", color=0x22408a)
  menu.add_field(name="**COMANDOS**", value="⬇️⬇️⬇️", inline=False)
  menu.add_field(name="**`%clear` [quantidade]**", value="Uma varridinha no chat sempre é bom!")
  menu.add_field(name="**`%couple`** [user1] [user2]", value="Marcando a declaração de casamento!")
  menu.add_field(name="**`%heart`** [user]", value="Apenas marque a pessoa que vocẽ esta apaixonado!")
  menu.add_field(name="**`%kick`** [user]", value="Da uma kickada em um usuario")
  menu.add_field(name="**`%ban`** [user]", value="Da uma linda banida em um usuario")
  menu.add_field(name="**`%agenda`**", value="Agenda publica do servidor")
  menu.set_image(url="https://i.ytimg.com/vi/tN6mBBQQZFQ/hqdefault.jpg?sqp=-oaymwEjCPYBEIoBSFryq4qpAxUIARUAAAAAGAElAADIQj0AgKJDeAE=&rs=AOn4CLAaXJ90iwOEK6mcfQS6Cqs8Q1WpLw")
  menu.set_author(name=client.user.name, icon_url=client.user.avatar_url)
  await ctx.channel.send(embed=menu)

@client.command(name="heart")
async def love_message(ctx, member : discord.Member):

  url_image = "https://media3.giphy.com/media/26FLdmIp6wJr91JAI/200.gif"
  love = discord.Embed(title=f":heart: {ctx.author.name} :heart: {member.name} :heart:", description=f"Hoje {ctx.author.mention} está se sentindo apaixonado(a) por {member.mention}")
  love.set_image(url=url_image)
  love.set_footer(text="(っ ͡❛ 👅 ͡❛)っ🎔 (っ ͡❛ 👅 ͡❛)っ🎔 (っ ͡❛ 👅 ͡❛)っ🎔")
  await ctx.message.delete()
  await ctx.channel.send(embed=love)


@client.command(name="agenda")
async def personal_list(ctx):

  with open('cogs/list.txt') as f:
    lines = []
    lines = f.readlines()

  list = discord.Embed(title="AGENDA PUBLÍCA", description=f"⬇️⬇️⬇️", color=0x22408a)
  count = 0
  for line in lines:
      count += 1
      list.add_field(name=f"**{count}**", value=f"{line}", inline=False)
  list.set_footer(text="Adicione uma anotação digitando `%adicionar [anotação]` e para remover `%remover [id]`")
  await ctx.channel.send(embed=list)

@client.command(name="adicionar")
async def add_argument_to_list(ctx, content):
  with open('cogs/list.txt', 'a') as f:
    f.write(f"{content} | {ctx.author.mention}")
    f.write("\n")
    await ctx.channel.send(f"**{content}** foi adicionado a sua agenda!")


@client.command(name="remover")
async def remove_argument_from_list(ctx, numInt):
    delete_line = open("cogs/list.txt", "r")
    lines = delete_line.readlines()
    delete_line.close()
    id = (int(numInt) - 1)
    del lines[id]
    line_d = open("cogs/list.txt", "w+")
    for line in lines:
        line_d.write(line)
    line_d.close()
    await ctx.channel.send(f"O indice `{numInt}` foi excluido da agenda")


@client.command()
async def clear(ctx, max=5):
  if(max >= 150):
    await ctx.send(f"{ctx.author.mention} **Você não pode apagar tantas mensagens**")
  else:
    await ctx.channel.purge(limit=max)
    await ctx.send(f"( ͡❛ 𝆒 ͡❛)👌  {ctx.author.mention} Mensagens apagadas com sucesso ( ͡❛ 𝆒 ͡❛)👌 ")

@client.command(pass_context = True)
@commands.has_permissions(kick_members=True)
async def kick(ctx, user: discord.Member, *, reason="( ͡👁️ _⦣ ͡👁️)👎"):
  url_image = "https://c.tenor.com/EaPsxzzXyQwAAAAM/kick-gone.gif"
  try:
    await user.kick(reason=reason)
    kick = discord.Embed(title=f":boot: Kicked {user.name}!", description=f"Motivo: {reason}\nPor: {ctx.author.mention}")
    kick.set_image(url=url_image)
    await ctx.message.delete()
    await ctx.channel.send(embed=kick)
    await user.send(embed=kick)
  except discord.errors.Forbidden:
    await ctx.message.delete()
    erro = discord.Embed(title=f"Não foi possivel kickar {user.name}!", description=f"**Motivo**: Sem permissão")
    erro.set_image(url=url_image)
    await ctx.channel.send(embed=erro)

@client.command(pass_context = True)
@commands.has_permissions(kick_members=True)
async def ban(ctx, user: discord.Member, *, reason="( ͡👁️ _⦣ ͡👁️)👎"):
  url_image = "https://c.tenor.com/5DXl8txCcBUAAAAM/ban-banned.gif"
  try:
    await user.ban(reason=reason)
    ban = discord.Embed(title=f":boot: {ctx.author.name} baniu {user.name}!", description=f"Motivo: {reason}")
    ban.set_image(url=url_image)
    await ctx.message.delete()
    await ctx.channel.send(embed=ban)
    await user.send(embed=ban)
  except discord.errors.Forbidden:
    await ctx.message.delete()
    erro = discord.Embed(title=f"Não foi possivel banir {user.name}!", description=f"**Motivo**: Sem permissã")
    erro.set_image(url=url_image)
    await ctx.channel.send(embed=erro)


keep_alive()

## YOUR DISCORD TOKEN
client.run('') 

