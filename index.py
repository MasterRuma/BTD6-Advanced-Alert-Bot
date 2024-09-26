import discord
import os # default module
from dotenv import load_dotenv
import requests
from datetime import datetime
from discord.ext import tasks

load_dotenv() # load all the variables from the env file
bot = discord.Bot()

last_advanced_id = None

chan_id = 1288833343252856832

def Advanced():
    url = "https://data.ninjakiwi.com/btd6/challenges/filter/daily"
    response = requests.get(url)
    data = response.json().get('body', [])  # body 안의 데이터 추출

    for item in data:
        if isinstance(item, dict):
            if 'advanced' in item.get('name', '').lower():
                return item.get('name'), item.get('createdAt'), item.get('id'), item.get('metadata')
    return None

@tasks.loop(minutes=1)  # 1분마다 확인
async def check_for_advanced():
    global last_advanced_id
    channel = bot.get_channel(chan_id)
    result = Advanced()

    print(f"{datetime.today().strftime('%Y/%m/%d %H:%M:%S')}")

    if result:
        name, createdAt, id_, metadata = result
        # 새로운 고급 도전인지 확인
        if last_advanced_id != id_:
            last_advanced_id = id_  # 현재 고급 도전 ID 저장
            embed = discord.Embed(title="고급도전 갱신!", url="https://data.ninjakiwi.com/btd6/challenges/filter/daily", description="오늘의 고급도전은?", color=0x00d5ff)
            embed.set_thumbnail(url="https://m.media-amazon.com/images/I/71BaHwbnrpL.png")
            embed.add_field(name="Name", value=f"{name}", inline=False)
            embed.add_field(name="CreateAt", value=f"{createdAt}", inline=False)
            embed.add_field(name="ID", value=f"{id_}", inline=False)
            embed.add_field(name="Metadata", value=f"{metadata}", inline=False)
            embed.set_footer(text=f"알림 시간 : {datetime.today().strftime('%Y/%m/%d %H:%M:%S')}")
            
            await channel.send(embed=embed)

@bot.event
async def on_ready():
    print(f"{bot.user} is ready and online!")
    check_for_advanced.start()  # 봇이 준비되면 주기적 확인 시작

@bot.slash_command(name="ping", description="서버의 핑을 측정합니다.")
async def ping(ctx: discord.ApplicationContext):
    await ctx.respond("교주님!")

bot.run(os.getenv('TOKEN')) # run the bot with the token