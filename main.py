import nextcord
import os
import levels
import utils
import users
import LoL
from nextcord.ext import commands



token = os.environ['TOKEN']
cogs = [levels, utils, LoL, users] #vocal  
bot_admin = 931454068033986560
prefix = '+'


client = commands.AutoShardedBot(command_prefix=prefix, intents = nextcord.Intents.all(), activity = nextcord.Activity(name=f'{prefix}help pour de l\'aide', type=5))

client.remove_command("help")


@client.event
async def on_member_join(member):
  channel = client.get_channel(917896874671878155)
  embed=nextcord.Embed(color=0X800808, title="— Bienvenue !")
  embed.set_thumbnail(url=member.avatar.url)
  embed.add_field(name="<a:exc:933858691239788614> Voici quelques endroits à visiter <a:exc:933858691239788614> :", value="\n **<:vamp:964096437858230273> ╭・୨ <#923874457695703051>** \n **<:heartransfusion:961895222634221608> ┊・୨<#917897427648909422>**\n **<a:heartbounce:933858707907969114> ╰・୨ <#917897378445557770>**", inline=False)
  await channel.send(f"{member.mention} — <@&935167007412875335>", embed=embed)

client.sniped_messages = {}
@client.event
async def on_message_delete(message):
    if message.attachments:
        bob = message.attachments[0]
        client.sniped_messages[message.guild.id] = (bob.proxy_url, message.content, message.author, message.channel.name, message.created_at)
    else:
        client.sniped_messages[message.guild.id] = (message.content,message.author, message.channel.name, message.created_at)

@client.command()
async def snipe(ctx):
    try:
        bob_proxy_url, contents,author, channel_name, time = client.sniped_messages[ctx.guild.id]
    except:
        contents,author, channel_name, time = client.sniped_messages[ctx.guild.id]
    try:
        embed = nextcord.Embed(description=contents , color=0X800808, timestamp=time)
        embed.set_image(url=bob_proxy_url)
        embed.set_author(name=f"{author.name}#{author.discriminator}", icon_url=author.avatar.url)
        embed.set_footer(text=f"Supprimé dans : #{channel_name}")
        await ctx.channel.send(embed=embed)
    except:
        embed = nextcord.Embed(description=contents , color=0X800808, timestamp=time)
        embed.set_author(name=f"{author.name}#{author.discriminator}", icon_url=author.avatar.url)
        embed.set_footer(text=f"Supprimé dans : #{channel_name}")
        await ctx.channel.send(embed=embed)

@client.command(name = 'clear')
@commands.has_permissions(manage_messages = True)
async def clear(ctx , amount=5):
  await ctx.channel.purge(limit=amount + 1)

for i in range(len(cogs)):
    cogs[i].setup(client)
    print(f'Catégorie {cogs[i]} chargée.')
    

client.run(token)
