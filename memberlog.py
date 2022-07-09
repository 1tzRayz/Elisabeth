import nextcord
from nextcord.ext import commands

class chanlog(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_member_update(self, before, after):
        x = self.client.get_guild(917894685412974652).get_channel(921466118374314004)
        if before.display_name != after.display_name:
            memname = nextcord.Embed(title="Mise à jour du membre", description=f"Changement de pseudonyme sur le serveur : {after.mention} ", color=0X880808)
            memname.add_field(name="Avant", value=before.display_name, inline=True)
            memname.add_field(name="Après", value=after.display_name, inline=True)
            memname.set_thumbnail(after.avatar.url)
            await x.send(embed=memname)
    

    @commands.Cog.listener()
    async def on_user_update(self, before, after):
        x = self.client.get_guild(917894685412974652).get_channel(921466118374314004)
        if before.avatar.url != after.avatar.url:
            memav = nextcord.Embed(title="Mise à jour du membre", description=f"Changement de photo de profil : {after.mention} ", color=0X880808)
            memav.add_field(name="Ancienne photo de profil :", value =f"{before.avatar.url}", inline=True)
            memav.set_thumbnail(after.avatar.url)
            await x.send(embed=memav)
        elif before.name != after.name:
            memn = nextcord.Embed(title="Mise à jour du membre", description=f"Changement de pseudonyme de compte : {after.mention} ", color=0X880808)
            memn.add_field(name="Avant", value =f"{before.name}", inline=True)
            memn.add_field(name="Après", value =f"{after.name}", inline=True)
            memn.set_thumbnail(after.avatar.url)
            await x.send(embed=memn)
        elif before.discriminator != after.discriminator:
            memd = nextcord.Embed(title="Mise à jour du membre", description=f"Changement de discriminant de compte : {after.mention} ", color=0X880808)
            memd.add_field(name="Avant", value =f"#{before.discriminator}", inline=True)
            memd.add_field(name="Après", value =f"#{after.discriminator}", inline=True)
            memd.set_thumbnail(after.avatar.url)
            await x.send(embed=memd)


def setup(client):
    client.add_cog(chanlog(client))