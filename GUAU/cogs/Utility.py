import discord
from discord.ext import commands
import asyncio
import random


class Utility(commands.Cog):

  
  def __init__(self, bot):
    self.bot = bot
    

    
  @commands.command()
  async def spam(self, ctx, num = 1, *user):
    
    limit = 9
    banned_user_ID = 725058766445346857
    users = " ".join(user)
  
    banned_user = await self.bot.fetch_user(banned_user_ID)
    if num > limit:
      num = limit
    if ctx.message.author != banned_user:
      for i in range(int(num)):
        await ctx.channel.send(users, delete_after=0.3)
    else:
      banned_user_DM = await banned_user.create_dm()
      await banned_user_DM.send("tas baneado de usar g!spam :v")
      await asyncio.sleep(3)
      await banned_user_DM.send("btw me yapeas 5 lucas porfa? me muero de hambre :'v pipipipippi")
      await banned_user_DM.send(file = discord.File('./Imagenes/yapeguau.jpg'))
      for i in range(int(num)):
        await ctx.channel.send(banned_user.mention, delete_after=0.3)


        
  @commands.command()#ask
  async def ask(self, ctx, message = None):
    answers = ["si", "no", "quizás", "quizás no", "probablemente si", "probablemente no", "nose :'v'"]
    if not message == None:
      await ctx.reply(random.choice(answers))
    else:
      await ctx.reply("Haz una pregunta de Si o No p :v")
  
  @commands.command()#react on
  async def react(self, ctx, emote, messageID: int):
    msg = await ctx.fetch_message(messageID)
    await msg.add_reaction(emote)
  
  @commands.command()
  async def say(self, ctx, channelID: int, *sentences):
    channel = self.bot.get_channel(channelID)
    msg = " ".join(sentences)
    await channel.send(msg)
  
  @commands.command()
  async def dm(self, ctx, userID: int, *words):
    msg = " ".join(words)
    user = await self.bot.fetch_user(userID)
    userDM = await user.create_dm()
    await userDM.send(msg)
    
  @commands.command()
  async def get_avatar(self, ctx, userID: int):
    user = await self.bot.fetch_user(userID)
    await ctx.channel.send(user.avatar_url)

def setup(bot):
  bot.add_cog(Utility(bot))