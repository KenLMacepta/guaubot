import discord
from discord.ext import commands
from datetime import datetime

now = datetime.now()
members = []

class Cumpleaños:
  def __init__(self, dia = 0, mes = 0, name="Fulano de Tal"):
    self.dia = dia
    self.mes = mes
    self.name = name
    members.append(self)

  def isBirthday(self):
    return self.dia == now.day and self.mes == now.month

ken = Cumpleaños(27, 5, "kEN")
niux = Cumpleaños(9, 4, "Niux_03")
benites = Cumpleaños(14, 5, "Benithos")
kikiwat = Cumpleaños(11, 12, "KIKIWAT")
wachimachine = Cumpleaños(17, 3, "Wachimachine")
takzak = Cumpleaños(27, 8, "takzak01")
lajarra = Cumpleaños(13, 3, "LaJarra")
guau = Cumpleaños(24, 1, "G.U.A.U")
fiary = Cumpleaños(21, 2, "Fiary 2.0")

class Birthday(commands.Cog):
  
  def __init__(self, bot):
    self.bot = bot
    

  @commands.command()
  async def cum(self, ctx):
    theresBirthday = False
    for i in members:
      if i.isBirthday():
        theresBirthday = True
        await ctx.channel.send(f'{ctx.message.guild.default_role} Es el cumpleaños de {i.name}! 🎉🎈')
        continue
    if not theresBirthday:
      await ctx.channel.send("No es el cumpleaños de nadie hoy")



  @commands.command()
  async def nextcum(self, ctx):
    nextcumlist = []
    for cum in members:
      if cum.mes >= now.month and cum.dia > now.day:
        nextcumlist.append(cum)
        try:
          await ctx.reply(f'El próximo cumpleaños es el de {nextcumlist[0].name}!! ({cum.dia}/{cum.mes}), y quien le sigue es {nextcumlist[1].name}')
        except:
          await ctx.reply(f'El próximo cumpleaños es el de {nextcumlist[0].name}!! ({cum.dia}/{cum.mes})')
        else:
          allcums = []
          for mes in range(1,13):
              for dia in range(1, 32):
                  for friend in members:
                      if friend.mes == mes and friend.dia == dia:
                          allcums.append(members.name)
          ctx.reply(f'El próximo cumpleaños es el de {nextcumlist[0].name}!! ({cum.dia}/{cum.mes}), y quien le sigue es {nextcumlist[1].name}')

            
def setup(bot):
  bot.add_cog(Birthday(bot))