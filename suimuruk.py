import discord
from discord.ext import commands
import os

client = commands.Bot(command_prefix = '$')

@client.event
async def on_ready():
  await client.change_presence(status=discord.Status.online)
  await client.change_presence(activity=discord.Game(name="싀무룩 보호"))
  print("봇 이름:",client.user.name,"봇 아이디:",client.user.id,"봇 버전:",discord.__version__)

@client.command()
async def help(ctx):
    embed=discord.Embed(title="명령어", description="현재 사용 가능한 명령어 목록입니다.", color=0x36fa00)
    embed.add_field(name="$경매 '현재 골드 시세'", value="레이드 경매 물품을 '판매' 할 때 손익분기점이 몇 골드인지 확인할 수 있습니다.\n해당 골드보다 상회 입찰 할 경우 손해입니다(사용은 또 달라요).\n다음과 같이 사용합니다.\n$경매 1700", inline=False)
    embed.add_field(name="$페온 '현재 골드 시세'", value="페온 1개당 몇 골드인지 현재 골드 시세를 바탕으로 계산해줍니다.\n다음과 같이 사용합니다.\n$페온 1700", inline=True)
    embed.set_footer(text="아직 개발중인 봇으로 기능이 추가될 수 있습니다.\nmade by WebView")
    await ctx.send(embed=embed)

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
    	await ctx.send("명령어를 찾지 못했습니다")        

client.run(os.environ['token'])