import nextcord
from nextcord.ext import commands
prefix = '+'

class moderation(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['purge'])
    @commands.has_permissions(manage_messages = True)
    async def clear(self, ctx , amount=5):
      channel = ctx.channel
      await channel.purge(limit=amount + 1)

    @commands.command()
    @commands.has_permissions(ban_members = True)
    async def ban(self, ctx, member : nextcord.Member = None, *, raison = None):
      embed = nextcord.Embed(color=0XFFFFFF,description=f"{member.mention} a été banni pour ``{raison}``")
      await member.ban(reason = raison)
      await ctx.channel.send(embed=embed)
      return

    @commands.command()
    @commands.has_permissions(administrator = True)
    async def unban(self, ctx, *, member):
      banned_users = await ctx.guild.bans()
      member_name, member_discriminator = member.split("#")
      for ban_entry in banned_users:
        user = ban_entry.user
        if (user.name, user.discriminator) == (member_name, member_discriminator):
          await ctx.guild.unban(user)
          await ctx.send(f'Le membre {user.mention} a été débanni.')
          return

    @commands.command()
    @commands.has_permissions(manage_channels = True)
    async def lock(self, ctx):
      channel = ctx.channel
      overwrite = channel.overwrites_for(ctx.guild.default_role)
      overwrite.send_messages = False
      await channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
      await ctx.send('Le salon a été lock.')

    @commands.command()
    @commands.has_permissions(manage_channels = True)
    async def unlock(self, ctx):
      channel = ctx.channel
      overwrite = channel.overwrites_for(ctx.guild.default_role)
      overwrite.send_messages = True
      await channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
      await ctx.send('Le salon a été unlock.')

    @commands.command()
    @commands.has_permissions(kick_members = True)
    async def kick(self, ctx, *, member : nextcord.Member = None, raison = None):
      embed = nextcord.Embed(color=0XFFFFFF,description=f"{member.mention} a été kick pour ``{raison}``")
      await member.kick(reason = raison)
      await ctx.channel.send(embed=embed)
      return
      
   
def setup(client):
    client.add_cog(moderation(client))
