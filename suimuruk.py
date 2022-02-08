import discord
import math
from discord.ext import commands
import os

client = commands.Bot(command_prefix = '$', help_command = None)

@client.event
async def on_ready():
  await client.change_presence(status=discord.Status.online)
  await client.change_presence(activity=discord.Game(name="개발 당"))
  print("봇 이름:",client.user.name,"봇 아이디:",client.user.id,"봇 버전:",discord.__version__)
  
@client.command()
async def 페온(ctx, para):
    try:
        cost = int(para)
    except:
        embed=discord.Embed(title="페온 계산기", color=0x0091ff)
        embed.add_field(name="오류", value="잘못된 입력입니다. 다음과 같이 입력해주세요.\n예) $페온 (현재 골드시세)", inline=False)
        await ctx.send(embed=embed)
        return
    embed=discord.Embed(title="페온 계산기", description="페온 1개당 골드 가격", color=0x0091ff)
    embed.add_field(name="페온 1개", value=f"{math.ceil(cost*17/190)} 골드", inline=False)
    await ctx.send(embed=embed)

@client.command()
async def 경매(ctx,*para):
    try:
        cost = int(para[0])
    except:
        embed=discord.Embed(title="경매 입찰 손익분기점(판매)", color=0x94ffb4)
        embed.add_field(name="오류", value="잘못된 입력입니다. 다음과 같이 입력해주세요.\n예) $경매 1000", inline=False)
        await ctx.send(embed=embed)
        return
    embed=discord.Embed(title="경매 입찰(판매 기준)", description="경매 아이템 판매 기준 __**입찰적정가 / 손익분기점**__", color=0x36fa00)
    embed.add_field(name="경매소 가격", value=f"{cost} 골드", inline=False)
    cost = math.ceil(cost * 0.95)
    embed.add_field(name="4인", value=f"{math.ceil(math.ceil(cost*3/4)/1.1)} 골드 / {math.ceil(cost*3/4)} 골드", inline=False)
    embed.add_field(name="8인", value=f"{math.ceil(math.ceil(cost*7/8)/1.1)} 골드 / {math.ceil(cost*7/8)} 골드", inline=False)
    embed.add_field(name="30인", value=f"{math.ceil(math.ceil(cost*29/30)/1.1)} 골드 / {math.ceil(cost*29/30)} 골드", inline=False)
    await ctx.send(embed=embed)

@client.command()
async def 군단장(ctx):
    embed=discord.Embed(title="군단장 공략", description="모모코가 참고하면 좋은 군단장 레이드 공략!", color=0xff0000)
    embed.add_field(name="아브렐슈드 노말", value="https://www.inven.co.kr/board/lostark/4811/4163396", inline=False)
    await ctx.send(embed=embed)

@client.command()
async def help(ctx):
    embed=discord.Embed(title="명령어", description="현재 사용 가능한 명령어 목록입니다.", color=0x36fa00)
    embed.add_field(name="$경매 '경매 물품 경매소 가격'", value="레이드 경매 물품을 '판매' 할 때 손익분기점이 몇 골드인지 확인할 수 있습니다.\n해당 골드보다 상회 입찰 할 경우 손해입니다(사용은 또 달라요).\n다음과 같이 사용합니다.\n$경매 1700", inline=False)
    embed.add_field(name="$페온 '현재 골드 시세'", value="페온 1개당 몇 골드인지 현재 골드 시세를 바탕으로 계산해줍니다.\n다음과 같이 사용합니다.\n$페온 1700", inline=True)
    embed.set_footer(text="아직 개발중인 봇으로 기능이 추가될 수 있습니다.\nmade by WebView")
    await ctx.send(embed=embed)

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
    	await ctx.send("명령어를 찾지 못했습니다")

client.run(os.environ['token'])