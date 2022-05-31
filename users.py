import discord
from discord.ext import commands
bot_channel = 922663411660251206
prefix = '-'

class users(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.command()
    async def pic(self, ctx, *, member : discord.Member = None):
        member = ctx.author if not member else member
        em = discord.Embed(title = member.name + '#' + member.discriminator, color=0X800808)
        embed.set_image(url=member.avatar.url)
        if ctx.channel.id == bot_channel:
            await ctx.send(embed=em)
    
    @commands.command()
    async def banner(self, ctx, *, member : discord.Member = None):
        member = ctx.author if not member else member
        req = await self.client.http.request(discord.http.Route("GET", "/users/{uid}", uid=member.id))
        banner_id = req["banner"]
        if banner_id:
          if banner_id.startswith("a_"):
            embed = discord.Embed(title= member.name + '#' + member.discriminator, color=0X800808)
            embed.set_image(url=f"https://cdn.discordapp.com/banners/{member.id}/{banner_id}.gif?size=1024")
          else:
            embed = discord.Embed(title= member.name + '#' + member.discriminator, color=0X800808)
            embed.set_image(url=f"https://cdn.discordapp.com/banners/{member.id}/{banner_id}?size=1024")
        if ctx.channel.id == bot_channel:
            await ctx.send(embed=embed)


   
def setup(client):
    client.add_cog(users(client))
