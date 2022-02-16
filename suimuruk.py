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
async def 페온(ctx, *, para):
    try:
        para = para.split()
        cost = int(para[0])
        if len(para) == 2:
            cnt = int(para[1])
    except:
        embed=discord.Embed(title="페온 계산기", color=0x0091ff)
        embed.add_field(name="오류", value="잘못된 입력입니다. 다음과 같이 입력해주세요.\n예) $페온 (현재 골드시세)\n예) $페온 (현재 골드시세) (페온개수)", inline=False)
        await ctx.send(embed=embed)
        return
    if len(para) == 1:
        embed=discord.Embed(title="페온 계산기", description="페온 1개 골드 가격", color=0x0091ff)
        embed.add_field(name="페온 1개", value=f"{math.ceil(cost*17/190)}G", inline=False)
        await ctx.send(embed=embed)
    else:
        embed=discord.Embed(title="페온 계산기", description=f"페온 {cnt}개 골드 가격", color=0x0091ff)
        embed.add_field(name=f"페온 {cnt}개", value=f"{math.ceil(cost*17/190)*cnt}G", inline=False)
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
async def 발탄(ctx):
    embed=discord.Embed(title="발탄 레이드 보상 및 더보기", description="발탄 난이도별 보상 및 더보기 정보입니다.", color=0x00ffbf)
    embed.add_field(name="노말\n1관문", value="500G, 힘줄 3개, 뼈 1개\n**더보기**\n500G, 힘줄 3개, 뼈 1개", inline=True)
    embed.add_field(name="\u200b", value="\u200b", inline=True)
    embed.add_field(name="\u200b\n2관문", value="2000G, 힘줄 3개, 뼈 2개\n**더보기**\n800G, 힘줄 3개, 뼈 2개", inline=True)
    embed.add_field(name="하드\n1관문", value="1000G, 뼈 3개\n**더보기**\n900G, 뼈 3개", inline=True)
    embed.add_field(name="\u200b", value="\u200b", inline=True)
    embed.add_field(name="\u200b\n2관문", value="3500G, 뼈 3개\n**더보기**\n1200G, 뼈 3개", inline=True)
    embed.add_field(name="최종보상 without 더보기", value="노말\n2500G, 힘줄 6개, 뼈 3개\n하드\n4500G, 뼈 6개", inline=True)
    embed.add_field(name="최종보상 with 더보기", value="노말\n1200G, 힘줄 12개, 뼈 6개\n하드\n2400G, 뼈 12개", inline=True)
    await ctx.send(embed=embed)
    
@client.command()
async def 비아(ctx):
    embed=discord.Embed(title="비아키스 레이드 보상 및 더보기", description="비아키스 난이도별 보상 및 더보기 정보입니다.", color=0xff5cbb)
    embed.add_field(name="노말\n1관문", value="500G, 송곳니 2개, 날개 1개\n**더보기**\n400G, 송곳니 2개, 날개 1개", inline=True)
    embed.add_field(name="\u200b\n2관문", value="600G, 송곳니 2개, 날개 1개\n**더보기**\n600G, 송곳니 2개, 날개 1개", inline=True)
    embed.add_field(name="\u200b\n3관문", value="1400G, 송곳니 2개, 날개 1개\n**더보기**\n800G, 송곳니 2개, 날개 1개", inline=True)
    embed.add_field(name="하드\n1관문", value="1000G, 날개 2개\n**더보기**\n700G, 날개 2개", inline=True)
    embed.add_field(name="\u200b\n2관문", value="1000G, 날개 2개\n**더보기**\n900G, 날개 2개", inline=True)
    embed.add_field(name="\u200b\n3관문", value="2500G, 날개 2개\n**더보기**\n1200G, 날개 2개", inline=True)
    embed.add_field(name="최종보상 without 더보기", value="노말\n2500G, 송곳니 6개, 날개 3개\n하드\n4500G, 날개 6개", inline=True)
    embed.add_field(name="최종보상 with 더보기", value="노말\n700G, 송곳니 12개, 날개 6개\n하드\n1700G, 날개 12개", inline=True)
    await ctx.send(embed=embed)
    
@client.command()
async def 쿠크(ctx):
    embed=discord.Embed(title="쿠크세이튼 레이드 보상 및 더보기", description="쿠크세이튼 난이도별 보상 및 더보기 정보입니다.", color=0xff0059)
    embed.add_field(name="노말\n1관문", value="1000G, 나팔 1개\n**더보기**\n800G, 나팔 1개", inline=True)
    embed.add_field(name="\u200b\n2관문", value="1000G, 나팔 2개\n**더보기**\n1000G, 나팔 2개", inline=True)
    embed.add_field(name="\u200b\n3관문", value="2500G, 나팔 2개\n**더보기**\n1300G, 나팔 2개", inline=True)
    # embed.add_field(name="하드\n1관문", value="1000G, 날개 2개\n**더보기**\n700G, 날개 2개", inline=True)
    # embed.add_field(name="\u200b\n2관문", value="1000G, 날개 2개\n**더보기**\n900G, 날개 2개", inline=True)
    # embed.add_field(name="\u200b\n3관문", value="2500G, 날개 2개\n**더보기**\n1200G, 날개 2개", inline=True)
    embed.add_field(name="최종보상 without 더보기", value="노말\n4500G, 나팔 5개", inline=True)
    embed.add_field(name="최종보상 with 더보기", value="노말\n1400G, 나팔 10개", inline=True)
    await ctx.send(embed=embed)
    
@client.command()
async def 아브(ctx):
    embed=discord.Embed(title="아브렐슈드 레이드 보상 및 더보기", description="아브렐슈드 난이도별 보상 및 더보기 정보입니다.", color=0xbd2eff)
    embed.add_field(name="노말\n12관문", value="4500G, 뿔 7개\n**더보기**\n1000G, 뿔 7개", inline=True)
    embed.add_field(name="\u200b\n34관문", value="1500G, 뿔 7개\n**더보기**\n1500G, 뿔 7개", inline=True)
    embed.add_field(name="\u200b\n56관문", value="2500G, 뿔 8개\n**더보기**\n2000G, 뿔 8개", inline=True)
    embed.add_field(name="하드\n12관문", value="5500G, 사념 7개\n**더보기**\n1500G, 사념 7개", inline=True)
    embed.add_field(name="\u200b\n34관문", value="2000G, 사념 7개\n**더보기**\n2000G, 사념 7개", inline=True)
    embed.add_field(name="\u200b\n56관문", value="3000G, 사념 8개\n**더보기**\n2500G, 사념 8개", inline=True)
    embed.add_field(name="최종보상 without 더보기", value="노말\n8500G, 뿔 22개\n하드\n10500G, 사념 22개", inline=True)
    embed.add_field(name="최종보상 with 더보기", value="노말\n4500G, 뿔 44개\n하드\n5500G, 사념 44개", inline=True)
    await ctx.send(embed=embed)

@client.command()
async def help(ctx):
    embed=discord.Embed(title="명령어", description="현재 사용 가능한 명령어 목록입니다.", color=0x36fa00)
    embed.add_field(name="$경매 '경매 물품 경매소 가격'", value="레이드 경매 물품을 '판매' 할 때 손익분기점이 몇 골드인지 확인할 수 있습니다.\n해당 골드보다 상회 입찰 할 경우 손해입니다(사용은 또 달라요).\n다음과 같이 사용합니다.\n$경매 1700", inline=False)
    embed.add_field(name="$페온 '현재 골드 시세'", value="페온 1개당 몇 골드인지 현재 골드 시세를 바탕으로 계산해줍니다.\n다음과 같이 사용합니다.\n$페온 1700", inline=True)
    embed.add_field(name="$페온 '현재 골드 시세' '페온 개수'", value="입력한 페온 개수당 몇 골드인지 현재 골드 시세를 바탕으로 계산해줍니다.\n다음과 같이 사용합니다.\n$페온 1700 30", inline=True)
    embed.add_field(name="$발탄", value="발탄 레이드 보상 및 더보기 정보입니다.", inline=True)
    embed.add_field(name="$비아키스", value="비아키스 레이드 보상 및 더보기 정보입니다.", inline=True)
    embed.add_field(name="$쿠크세이튼", value="쿠크세이튼 레이드 보상 및 더보기 정보입니다.", inline=True)
    embed.add_field(name="$아브렐슈드", value="아브렐슈드 레이드 보상 및 더보기 정보입니다.", inline=True)
    embed.set_footer(text="아직 개발중인 봇으로 기능이 추가될 수 있습니다.\nmade by WebView")
    await ctx.send(embed=embed)

@client.command()
async def 도움(ctx):
    embed=discord.Embed(title="명령어", description="현재 사용 가능한 명령어 목록입니다.", color=0x36fa00)
    embed.add_field(name="$경매 '경매 물품 경매소 가격'", value="레이드 경매 물품을 '판매' 할 때 손익분기점이 몇 골드인지 확인할 수 있습니다.\n해당 골드보다 상회 입찰 할 경우 손해입니다(사용은 또 달라요).\n다음과 같이 사용합니다.\n$경매 1700", inline=False)
    embed.add_field(name="$페온 '현재 골드 시세'", value="페온 1개당 몇 골드인지 현재 골드 시세를 바탕으로 계산해줍니다.\n다음과 같이 사용합니다.\n$페온 1700", inline=True)
    embed.add_field(name="$페온 '현재 골드 시세' '페온 개수'", value="입력한 페온 개수당 몇 골드인지 현재 골드 시세를 바탕으로 계산해줍니다.\n다음과 같이 사용합니다.\n$페온 1700 30", inline=True)
    embed.add_field(name="$발탄", value="발탄 레이드 보상 및 더보기 정보입니다.", inline=True)
    embed.add_field(name="$비아키스", value="비아키스 레이드 보상 및 더보기 정보입니다.", inline=True)
    embed.add_field(name="$쿠크세이튼", value="쿠크세이튼 레이드 보상 및 더보기 정보입니다.", inline=True)
    embed.add_field(name="$아브렐슈드", value="아브렐슈드 레이드 보상 및 더보기 정보입니다.", inline=True)
    embed.set_footer(text="아직 개발중인 봇으로 기능이 추가될 수 있습니다.\nmade by WebView")
    await ctx.send(embed=embed)

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
    	await ctx.send("명령어를 찾지 못했습니다")
     
client.run(os.environ['token'])