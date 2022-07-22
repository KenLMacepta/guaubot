import discord
from discord.ext import commands


class Maths(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
    
  
  @commands.command()
  async def sum(self, ctx, *nums):
    operation = " + ".join(nums)
    await ctx.send(f'{operation} = {eval(operation)}')
  
  @commands.command()
  async def res(self, ctx, *nums): 
    operation = " - ".join(nums)
    await ctx.send(f'{operation} = {eval(operation)}')
  
  @commands.command()
  async def mul(self, ctx, *nums): 
    operation = " * ".join(nums)
    await ctx.send(f'{operation} = {eval(operation)}')
  
  @commands.command()
  async def div(self, ctx, *nums): 
    operation = " / ".join(nums)
    await ctx.send(f'{operation} = {eval(operation)}')

  @commands.command()
  async def hello(self, ctx):
    await ctx.reply("gelloo")

def setup(bot):
  bot.add_cog(Maths(bot))