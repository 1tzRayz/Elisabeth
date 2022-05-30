import discord
import random
from discord.ext import commands
chan_gaming = 917897748638990336

champs=["Aatrox","Akali","Aurelion Sol","Ahri","Alistar","Amumu","Anivia","Annie","Ashe","Azir","Bard","Blitzcrank","Brand","Braum","Camille","Caitlyn","Cassiopeia","Cho Gath","Corki","Darius","Dr. Mundo","Diana","Draven","Ekko","Elise","Evelynn","Ezreal","Fiddlesticks","Fiora","Fizz","Galio","Gangplank","Garen","Gnar","Gragas","Graves","Hecarim","Heimerdinger","Irelia","Ivern","Illaoi","Janna","Jarvan IV","Jax","Jayce","Jhin","Jinx","Karma","Kalista","Karthus","Kassadin","Kai Sa","Katarina","Kayn","Kayle","Kennen","Kha Zix","Kog Maw","Kled","Kindred","LeBlanc","Lee Sin","Leona","Lucian","Lissandra","Lulu","Lux","Malphite","Malzahar","Maokai","Master Yi","Miss Fortune","Mordekaiser","Morgana","Nami","Nasus","Nautilus","Neeko","Nidalee","Nocturne","Nunu","Olaf","Orrn","Orianna","Pantheon","Poppy","Pyke","Quinn","Rammus","Rakan","Rek Sai","Renekton","Rengar","Riven","Rumble","Ryze","Sejuani","Shaco","Shen", "Shyvana", "Singed", "Sion", "Sivir", "Skarner", "Sona", "Soraka", "Swain", "Syndra", "Sylas", "Talon", "Taliyah","Taric","Tahm Kench","Thresh","Teemo","Tristana","Trundle","Tryndamere","Twisted Fate","Twitch","Udyr","Urgot","Varus","Vayne","Veigar","Vel Koz","Vi","Viktor","Vladimir","Volibear","Warwick","Wukong","Xayah","Xerath","Xin Zhao","Yasuo","Yorick","Zac","Zed","Ziggs","Zilean","Zoe","Zyra","Yuumi","Senna","Qiana","Sett","Aphelios","Lillia","Yone","Samira","Seraphine","Rell","Viego","Gwen","Akshan","Vex", "Zeri", "Renata"]

class LoL(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['whos'])
    async def Whos(self, ctx):
      champion = random.choice(champs)
      if ctx.channel.id == chan_gaming:
            embed=discord.Embed(color=0X800808, title=f"Qui est le meilleur joueur de {champion} ?")
            await ctx.send(embed=embed)
    
def setup(client):
    client.add_cog(LoL(client))
