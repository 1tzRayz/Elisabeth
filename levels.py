import discord
import asyncio
from discord.ext import commands
from pymongo import MongoClient

 
bot_channel = [922663411660251206,931454068033986560]
talk_channels = [917896874671878155, 917897164812869702, 917897216419590204, 917897269272010792, 917897748638990336, 917897813986250833, 917898218367500398, 917898632303349830, 917898691904430080, 917899171044921434, 917899244503961611, 917899307934416926, 921457745893400626, 941319677433511946]
admin_chan = 931454068033986560
VocIDS = [917895479545712720, 917895581291135036, 917924829229875240, 917924900948283472, 917924677622562837, 918490456839565322, 917924580323102771, 917925739096068136, 917924476560224316]

level = ["𝐋𝐚𝐧𝐠𝐚", "𝐇𝐨𝐰𝐥", "𝐇𝐚𝐤𝐮", "𝐌𝐮𝐬𝐭𝐚𝐧𝐠", "𝐒𝐚𝐧", "𝐊𝐢𝐫𝐢𝐠𝐚𝐤𝐮𝐫𝐞", "𝐌𝐨𝐧𝐤𝐞"]
levelnum = [2, 5, 10, 15, 20, 30, 100]
 
cluster = os.environ['MONGO']
 
collection_name = cluster["data"]["levelings"] 
 
class levels(commands.Cog):
    def __init__(self, client):
        self.client = client
 
    @commands.Cog.listener()
    async def on_ready(self):
      print("Online!")

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.channel.id in talk_channels:
            stats = collection_name.find_one({"id":message.author.id})
            if not message.author.bot:
                if stats is None:
                    newuser = {"id" : message.author.id, "xp" : 0}
                    collection_name.insert_one(newuser)
                else:
                    xp = stats["xp"] + 1
                    collection_name.update_one({"id":message.author.id}, {"$set":{"xp":xp}}) 
                    lvl = 0
                    while True:
                        if xp < ((50*(lvl**2))+(50*lvl)):
                            break
                        lvl += 1
                    xp -= ((50*((lvl-1)**2))+(50*(lvl-1)))
                    if xp == 0:
                        await message.reply(f"Bravo, tu viens de passer au niveau  {lvl} !")
                        for i in range(len(level)):
                            if lvl == levelnum[i]:
                                await message.author.add_roles(discord.utils.get(message.author.guild.roles, name=level[i]))
                                embed = discord.Embed(color = 0X800808, description=f"{message.author.mention}. Félicitations ! Tu viens d'obtenir un nouveau rôle : **{level[i]}**.")
                                embed.set_author(name = message.author.name, icon_url=message.author.avatar_url)
                                await message.channel.send(embed=embed)
                              
    @commands.command(aliases=['xp', 'level', 'Rank'])
    async def rank(self, ctx, member : discord.User = None):
      if member == None:
        member = ctx.author
      if ctx.channel.id in bot_channel:
            stats = collection_name.find_one({"id" : member.id})
            if stats is None:
                embed = discord.Embed(color=0X800808,description="Tu n'as envoyé aucun message, tu ne possèdes donc pas d'XP !")
                await ctx.channel.send(embed=embed)
            else:
                xp = stats["xp"]
                lvl = 0
                rank = 0
                while True:
                        if xp < ((50*(lvl**2))+(50*lvl)):
                            break
                        lvl += 1
                xp -= ((50*((lvl-1)**2))+(50*(lvl-1)))
                boxes = int((xp/(200*((1/2) * lvl)))*20)
                rankings = collection_name.find().sort("xp",-1) 
                for x in rankings:
                    rank += 1
                    if stats["id"] == x["id"]:
                        break
                embed = discord.Embed(color=0X800808,title="Information sur l'XP de {}".format(member.name))
                embed.add_field(name="Pseudonyme", value=member.mention, inline=True)
                embed.add_field(name="XP", value=f"{xp}/{int(200*((1/2)*lvl))}", inline=True)
                embed.add_field(name="Niveau", value=f"{lvl}", inline=True)
                embed.add_field(name="Barre de progression :", value=boxes * ":blue_square:" + (20-boxes) * ":white_large_square:", inline=False)
                embed.set_thumbnail(url=member.avatar_url)
                await ctx.channel.send(embed=embed)

    @commands.command(aliases=['lb', 'classement', 'Lb', 'Leaderboard'])
    async def leaderboard(self, ctx):
        if (ctx.channel.id in bot_channel):
            rankings = collection_name.find().sort("xp",-1) 
            i = 1
            embed = discord.Embed(color=0X800808,title="Classement du serveur :")
            for x in rankings:
                try:
                    temp = ctx.guild.get_member(x["id"])
                    tempxp = x["xp"]
                    embed.add_field(name=f"``⭐ {i} :`` {temp.name}", value=f"*XP Total :* {tempxp}", inline=False)
                    i += 1
                except:
                    pass
                if i == 11:
                    break
            await ctx.channel.send(embed=embed)

    @commands.command()
    async def givexp(self,ctx, number : int, member : discord.Member = None):
      if member == None:
        member = ctx.author
      if (ctx.channel.id == admin_chan):
        stats = collection_name.find_one({"id":member.id})
        xp = stats["xp"] + number
        collection_name.update_one({"id":member.id}, {"$set":{"xp":xp}})
        given = discord.Embed(color=0X800808,title=f"Tu viens de donner {number} points d'XP à l'utilisateur {member.name} ! <:grochat:935628681064357888>")
        await ctx.send(embed=given)
    
    @commands.command()
    async def removexp(self,ctx, number : int, member : discord.Member = None):
      if member == None:
        member = ctx.author
      if (ctx.channel.id == admin_chan):
        stats = collection_name.find_one({"id":member.id})
        xp = stats["xp"] - number
        collection_name.update_one({"id":member.id}, {"$set":{"xp":xp}})
        removed = discord.Embed(color=0X800808,title=f"Tu viens de te retirer {number} points d'XP à {member.name} ! <:grochat:935628681064357888>")
        await ctx.send(embed=removed)


def setup(client):
    client.add_cog(levels(client))
