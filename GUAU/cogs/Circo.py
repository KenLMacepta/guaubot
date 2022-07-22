import discord
from discord.ext import commands
import random

IdList = []
class Circo(commands.Cog):
  
  
  def __init__(self, bot):
    self.bot = bot


  
  @commands.Cog.listener()
  async def on_raw_reaction_add(self, payload):
    
    print(f'{payload.member.display_name} added {payload.emoji.name} on {payload.message_id}')
    
  
    message = await self.bot.get_channel(payload.channel_id).fetch_message(payload.message_id)

    
    
    try:
      reaction = discord.utils.get(message.reactions)
    except:
      pass

    
  
  
    circo = self.bot.get_channel(997239769379647599)
    counter = 3
  
    
  
  
    embed = discord.Embed(title=message.content,color=message.author.color)
    embed.set_author(name=message.author.display_name, url=message.jump_url, icon_url= message.author.avatar_url)
    embed.add_field(name="\u200b", value=f"[Click Here to view context]({message.jump_url})")
    try:
      img = message.attachments[0].url
    except:
      pass
  
    try:
      embed.set_image(url=img)
    except:
      pass
  
    
    
    if reaction.count == counter and reaction.emoji == '🤡':
      
      currentMessageID = reaction.message.id
      
      if not currentMessageID in IdList:
        messageID = reaction.message.id
        IdList.insert(1, messageID)
        nivel_de_chiste = random.randint(0, 100)
        await circo.send(f'nivel de 🤡: {str(nivel_de_chiste)}/100', embed=embed)
      else:
        channel = reaction.message.channel
        await channel.send("This message is already in Circo", delete_after = 5.0)
  
  
  
  
  @commands.Cog.listener() #Eliminar mensaje
  async def on_reaction_add(self, reaction, user=None):
    hall_of_fame = self.bot.get_channel(997239769379647599)
    counter = 3
    if reaction.count >= counter and reaction.emoji == "❌":
      if reaction.message.author == self.bot.user:
        reaction.message.add_reaction("😈")
        return
      else:
        if not reaction.message.channel == hall_of_fame:
          await reaction.message.delete()
          await reaction.message.channel.send("<:no_bitches:990794333773004880> no message <:no_bitches:990794333773004880>")
        else:
          await reaction.message.delete()


def setup(bot):
  bot.add_cog(Circo(bot))