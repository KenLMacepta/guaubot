import discord
from discord.ext import commands
from discord import FFmpegPCMAudio
import asyncio
import random

audioList = []

class Audio:
  def __init__(self, src, duration):
    self.src = src
    self.duration = duration
    audioList.append(self) #auto-Add to audioList


wenomechainsama = Audio('./audios/wenomechainsama.mp3', 27)
estanocheoscura = Audio('./audios/estanocheoscura.mp3', 80)
gokuvssuperman = Audio('./audios/gokuvssuperman.mp3', 130)
logitech = Audio('./audios/logitech.mp3', 19)
musicaepicagrefg = Audio('./audios/musicaepicagrefg.mp3', 36)
elpequeñodelfin = Audio('./audios/elpequeñodelfin.mp3', 12)
puapuapua = Audio('./audios/puapuapua.mp3', 40)
tunometecabrasarambiche = Audio('./audios/tunometecabrasarambiche.mp3', 38)
nosesiviviromorir = Audio('./audios/nosesiviviromorir.mp3', 40)
wideputin = Audio('./audios/wideputin.mp3', 19)
earthbound = Audio('./audios/earthboundsong.mp3', 11)
pvzvictorytheme = Audio('./audios/pvzvictorytheme.mp3', 7)
ttminutes = Audio('./audios/31minutos.mp3', 51)
gvvenysanamidolor = Audio('./audios/gvvenysanamidolor.mp3', 62)
sonidosgraciosos = Audio('./audios/sonidosgraciosos.mp3', 29)
XD = Audio('./audios/XD.mp3', 33)
wa = Audio('./audios/wa.mp3', 2)
xiehuapiao = Audio('./audios/xiehuapiao.mp3', 15)
asianmeme = Audio('./audios/asianmeme.mp3', 15)
innersatisfaction = Audio('./audios/innersatisfaction.mp3', 27)
hunterxhuntersong = Audio('./audios/hunterxhuntersong.mp3', 49)
subcacha = Audio('./audios/subcacha.mp3', 106)
stayinsideme = Audio('./audios/stayinsideme.mp3', 106)
cuacuavaca = Audio('./audios/cuacuavaca.mp3', 26)
ironmansnap = Audio('./audios/ironmansnap.mp3', 33)
vegetacaritaempapada = Audio('./audios/vegetacaritaempapada.mp3', 31)
escuchameunacosa = Audio('./audios/escuchameunacosa.mp3', 62)
gokufiufiu = Audio('./audios/gokufiufiu.mp3', 28)

class Voice(commands.Cog):

  def __init__(self, bot):
    self.bot = bot
  

  @commands.command(pass_context = True , aliases=['l'])
  async def leave(self, ctx):
    await ctx.voice_client.disconnect()
    

  @commands.command(pass_context = True , aliases=['p'])
  async def play(self, ctx):
    
    audio = random.choice(audioList) #Get random audio from "audioList"
    source = FFmpegPCMAudio(audio.src, executable="ffmpeg") #Converting mp3 to.. something executable xd

    try:
      channel = ctx.author.voice.channel #Try Get channel
    except:
      await ctx.reply("No estás en un vc")
      return

      
    await channel.connect() #Connect
    ctx.voice_client.play(source)#Play audio

    
    del(source)# "Reset" the var

    
    await asyncio.sleep(audio.duration) #Wait for audio to end

    
    await ctx.voice_client.disconnect()#Disconnect


  @commands.command(pass_context = True , aliases=['jp'])
  async def jplay(self, ctx, channelID):
    
    audio = random.choice(audioList) 
    source = FFmpegPCMAudio(audio.src, executable="ffmpeg") 

    try:
      channel = await self.bot.fetch_channel(channelID) 
    except:
      print("No se encontró el canal de voz")
      return

      
    await channel.connect() 
    ctx.voice_client.play(source)

    
    del(source)

    
    await asyncio.sleep(audio.duration) 
    
    await ctx.voice_client.disconnect()

    

def setup(bot):
  bot.add_cog(Voice(bot))