import discord
from discord.ext import commands


math_commands = "- sum \n - res \n - div \n - mul"
utility_commands = "- spam \n - get_avatar \n - react \n - ask"
voice_commands = "- play \n - leave"
birthday_commands = "- cum \n - nextcum"

class Help(commands.Cog):

  def __init__(self, bot):
    self.bot = bot
    bot.remove_command('help')


  @commands.command()
  async def help(self, ctx):
    embed = discord.Embed(title="Commands",color=ctx.author.color)
    embed.add_field(name="Calculator 🤓", value=math_commands)
    embed.add_field(name="Voice 🎤", value=voice_commands)
    embed.add_field(name="Birthdays 🎂", value=birthday_commands)
    embed.add_field(name="Other 👀", value=utility_commands)
    
    

    
    await ctx.channel.send(embed = embed)
  

    
    
def setup(bot):
  bot.add_cog(Help(bot))

