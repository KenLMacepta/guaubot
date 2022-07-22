import discord
from discord.ext import commands
import random
import guau_images as gi


actividad = "g!help"

class Listener(commands.Cog):
  
  
  def __init__(self, bot):
    self.bot = bot
    
  

  @commands.Cog.listener()
  async def on_ready(self):
    print(f"{self.bot.user} está corriendo :D")
    await self.bot.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name=actividad))
    #await channel.send(f"")
  
  
  @commands.Cog.listener()
  async def on_message(self, message): #trece
    print(message.content, " -" + str(message.author.name))
    if message.author == self.bot.user:
      return
  
    if message.content.startswith("g!spam") or message.content.startswith("g!multspam"):
      await message.delete()
  
    if message.content.startswith("g!react"):
      await message.delete()
  
    if self.bot.user.mentioned_in(message):
      user_dm = await message.author.create_dm()
      randomnum = random.randint(1, 2)
      if randomnum == 1:
        await user_dm.send("ola ia que me mencionaste, me yapeas de paso unas 5 lucas porfa que me muero de hambre :'vvvvv")
        await user_dm.send(gi.guauyape)

        
      
    


def setup(bot):
  bot.add_cog(Listener(bot))