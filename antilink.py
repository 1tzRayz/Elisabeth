import nextcord
from nextcord.ext import commands

class antilink(commands.Cog):
    def __init__(self, client):
        self.client = client
        
     
    command.Cog.listener()
    async def on_message(self, message):
    x = self.client.get_channel(995091597509279804)
    if "discord.gg" in message.content.lower():
        await message.delete()
        await message.channel.send("Tu n'as pas le droit d'envoyer d'invitation sur ce serveur.")
        await x.send(f"{message.author.mention} à envoyé une invitation dans le salon {message.channel.mention}.")
        

def setup(client):
    client.add_cog(antilink(client))
