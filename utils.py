import discord
from discord.ext import commands
bot_channel = 922663411660251206
bump_channel = 917897595190386710
bot_admin = 931454068033986560
prefix = '-'

class utils(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['aide'])
    async def help(self, ctx):
      embed=discord.Embed(color=0x880808, title="Commande d'aide")
      embed.set_author(name="Elisabeth est là pour t'aider 🧛",icon_url="https://images-ext-2.discordapp.net/external/-5YTsAFzQA6xUx6NWrAiqTaeVHXCLuGSDpKwNXNIBr4/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/931451884336742400/1f419b41073663feb8d695880ddf4987.png?width=559&height=559")
      embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/961893746113384471/964098205702832138/200w.gif")
      embed.add_field(name="``Systeme d'XP`` :star:", value=f"> {prefix}rank *Permet d'afficher des informations sur votre XP.* \n > {prefix}leaderboard *Permet d'afficher le classement d'XP du serveur.*", inline=False)
      embed.add_field(name="``Fun`` 😋", value=f"> {prefix}Whos *Demande 'Qui est le meilleur joueur de <Champion LoL>'*, à vos risques de brisage d'amitiés ou autre.", inline=False)
      if ctx.channel.id == bot_channel:
        await ctx.channel.send(embed=embed)
      elif ctx.channel.id == bot_admin:
        embed.add_field(name="``Administration XP`` :vampire:", value=f"> {prefix}givexp <nombre> (membre) : *Permet d'ajouter de l'XP à un membre du serveur.* \n > {prefix}removexp <nombre> (membre): *Permet de retirer de l'XP à un membre du serveur.*", inline=False)
        await ctx.channel.send(embed=embed)
      
   
def setup(client):
    client.add_cog(utils(client))
