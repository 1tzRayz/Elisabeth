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
        em = discord.Embed(title="Commandes d'Elisabeth",color=0x880808)
        em.add_field(name="```-pic [membre]```", value="Permet de récupérer la photo de profil de quelqu'un.", inline=False)
        em.add_field(name="```-banner [membre]```", value="Permet de récupérer la bannière de quelqu'un.", inline=False)
        em.add_field(name="```-level [membre]```", value="Permet d'afficher des informations sur l'XP de quelqu'un.", inline=False)
        em.add_field(name="```-profile [membre] (soon)```", value="Donne le profil de quelqu'un.", inline=False)
        em.add_field(name="```-leaderboard / -lb```", value="Permet d'afficher le classement d'XP du serveur.", inline=False)
        em.add_field(name="```-whos```", value="Demande qui est le meilleur joueur sur <champion de LoL>.", inline=False)
        await ctx.send(embed=em)
      
   
def setup(client):
    client.add_cog(utils(client))
