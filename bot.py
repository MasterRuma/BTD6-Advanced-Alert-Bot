import discord
import os 
import requests
from datetime import datetime
from discord.ext import tasks

bot = discord.Bot()

last_advanced_id = None

chan_id = int(os.environ.get("CHAN_ID")) 

avaliable_heros = []

tower_names = {
    "DartMonkey": "다트",
    "BoomerangMonkey": "부메랑",
    "BombShooter": "폭탄",
    "TackShooter": "압정",
    "IceMonkey": "얼음",
    "GlueGunner": "글루",
    "SniperMonkey": "저격",
    "MonkeySub": "잠수",
    "MonkeyBuccaneer": "해적",
    "MonkeyAce": "에이스",
    "HeliPilot": "헬리콥터",
    "MortarMonkey": "박격포",
    "DartlingGunner": "다틀링",
    "WizardMonkey": "마법",
    "SuperMonkey": "슈퍼",
    "NinjaMonkey": "닌자",
    "Alchemist": "연금술사",
    "Druid": "드루이드",
    "Mermonkey": "바다",
    "BananaFarm": "바나나 농장",
    "SpikeFactory": "스파이크",
    "MonkeyVillage": "마을",
    "EngineerMonkey": "엔지니어",
    "BeastHandler": "맹수 조련사"
}

info = {
    "name": None,
    "id": None,
    "mapurl": None,
    "diff": None,
    "diff_mode": None,
    "disableDoubleCash": None,
    "disableInstas": None,
    "disableMK": None,
    "disablePowers": None,
    "disableSelling": None,
    "startingCash": None,
    "abilityCooldownReductionMultiplier": None,
    "leastCashUsed": None,
    "leastTiersUsed": None,
    "removeableCostMultiplier": None,
    "lives": None,
    "startRound": None,
    "endRound": None,
    "maxTowers": None,
    "bloon_speed": None,
    "moab_speed": None,
    "regrow_rate": None,
    "all_camo": None,
    "all_regrow": None,
    "ceramic_health": None,
    "moab_health": None,
}

heros = {
    "ChosenPrimaryHero": None,
    "Quincy": None,
    "Gwendolin": None,
    "StrikerJones": None,
    "ObynGreenfoot": None,
    "CaptainChurchill": None,
    "Benjamin": None,
    "Ezili": None,
    "PatFusty": None,
    "Adora": None,
    "AdmiralBrickell": None,
    "Etienne": None,
    "Sauda": None,
    "Psi": None,
    "Geraldo": None,
    "Corvus": None,
    "Rosalia": None
}

towers = {
    "DartMonkey": {
        "max": None,
        "path1NumBlockedTiers": None,
        "path2NumBlockedTiers": None,
        "path3NumBlockedTiers": None
    },
    "BoomerangMonkey": {
        "max": None,
        "path1NumBlockedTiers": None,
        "path2NumBlockedTiers": None,
        "path3NumBlockedTiers": None
    },
    "BombShooter": {
        "max": None,
        "path1NumBlockedTiers": None,
        "path2NumBlockedTiers": None,
        "path3NumBlockedTiers": None
    },
    "TackShooter": {
        "max": None,
        "path1NumBlockedTiers": None,
        "path2NumBlockedTiers": None,
        "path3NumBlockedTiers": None
    },
    "IceMonkey": {
        "max": None,
        "path1NumBlockedTiers": None,
        "path2NumBlockedTiers": None,
        "path3NumBlockedTiers": None
    },
    "GlueGunner": {
        "max": None,
        "path1NumBlockedTiers": None,
        "path2NumBlockedTiers": None,
        "path3NumBlockedTiers": None
    },
    "SniperMonkey": {
        "max": None,
        "path1NumBlockedTiers": None,
        "path2NumBlockedTiers": None,
        "path3NumBlockedTiers": None
    },
    "MonkeySub": {
        "max": None,
        "path1NumBlockedTiers": None,
        "path2NumBlockedTiers": None,
        "path3NumBlockedTiers": None
    },
    "MonkeyBuccaneer": {
        "max": None,
        "path1NumBlockedTiers": None,
        "path2NumBlockedTiers": None,
        "path3NumBlockedTiers": None
    },
    "MonkeyAce": {
        "max": None,
        "path1NumBlockedTiers": None,
        "path2NumBlockedTiers": None,
        "path3NumBlockedTiers": None
    },
    "HeliPilot": {
        "max": None,
        "path1NumBlockedTiers": None,
        "path2NumBlockedTiers": None,
        "path3NumBlockedTiers": None
    },
    "MortarMonkey": {
        "max": None,
        "path1NumBlockedTiers": None,
        "path2NumBlockedTiers": None,
        "path3NumBlockedTiers": None
    },
    "DartlingGunner": {
        "max": None,
        "path1NumBlockedTiers": None,
        "path2NumBlockedTiers": None,
        "path3NumBlockedTiers": None
    },
    "WizardMonkey": {
        "max": None,
        "path1NumBlockedTiers": None,
        "path2NumBlockedTiers": None,
        "path3NumBlockedTiers": None
    },
    "SuperMonkey": {
        "max": None,
        "path1NumBlockedTiers": None,
        "path2NumBlockedTiers": None,
        "path3NumBlockedTiers": None
    },
    "NinjaMonkey": {
        "max": None,
        "path1NumBlockedTiers": None,
        "path2NumBlockedTiers": None,
        "path3NumBlockedTiers": None
    },
    "Alchemist": {
        "max": None,
        "path1NumBlockedTiers": None,
        "path2NumBlockedTiers": None,
        "path3NumBlockedTiers": None
    },
    "Druid": {
        "max": None,
        "path1NumBlockedTiers": None,
        "path2NumBlockedTiers": None,
        "path3NumBlockedTiers": None
    },
    "Mermonkey": {
        "max": None,
        "path1NumBlockedTiers": None,
        "path2NumBlockedTiers": None,
        "path3NumBlockedTiers": None
    },
    "BananaFarm": {
        "max": None,
        "path1NumBlockedTiers": None,
        "path2NumBlockedTiers": None,
        "path3NumBlockedTiers": None
    },
    "SpikeFactory": {
        "max": None,
        "path1NumBlockedTiers": None,
        "path2NumBlockedTiers": None,
        "path3NumBlockedTiers": None
    },
    "MonkeyVillage": {
        "max": None,
        "path1NumBlockedTiers": None,
        "path2NumBlockedTiers": None,
        "path3NumBlockedTiers": None
    },
    "EngineerMonkey": {
        "max": None,
        "path1NumBlockedTiers": None,
        "path2NumBlockedTiers": None,
        "path3NumBlockedTiers": None
    },
    "BeastHandler": {
        "max": None,
        "path1NumBlockedTiers": None,
        "path2NumBlockedTiers": None,
        "path3NumBlockedTiers": None
    },
}

def available_hero():
    avaliable_heros.clear()
    for hero in heros:
        if heros[hero] != 0:
            avaliable_heros.append(hero)
        

def Advanced():
    url = "https://data.ninjakiwi.com/btd6/challenges/filter/daily"
    response = requests.get(url)
    data = response.json().get('body', [])

    for item in data:
        if isinstance(item, dict):
            if 'advanced' in item.get('name', '').lower():
                info['name'] = item.get('name')
                info['id'] = item.get('id')
                Advanced_metadata(item.get('metadata'))
                return item.get('id')
    return None

def Advanced_metadata(URL):
    response = requests.get(URL)
    data = response.json().get('body', [])
    # INFO
    info['name'] = data.get('name', "")
    info['id'] = data.get('id', "")
    info['mapurl'] = data.get('mapURL', "")
    info['diff'] = data.get('difficulty', "")
    info['diff_mode'] = data.get('mode', "")
    info['disableDoubleCash'] = data.get('disableDoubleCash', "")
    info['disableInstas'] = data.get('disableInstas', "")
    info['disableMK'] = not data.get('disableMK', False) if isinstance(data.get('disableMK'), bool) else data.get('disableMK', "")
    info['disablePowers'] = not data.get('disablePowers', False) if isinstance(data.get('disablePowers'), bool) else data.get('disablePowers', "")
    info['disableSelling'] = not data.get('disableSelling', False) if isinstance(data.get('disableSelling'), bool) else data.get('disableSelling', "")
    info['startingCash'] = data.get('startingCash', "")
    info['abilityCooldownReductionMultiplier'] = data.get('abilityCooldownReductionMultiplier', "")
    info['leastCashUsed'] = data.get('leastCashUsed', "")
    info['leastTiersUsed'] = data.get('leastTiersUsed', "")
    info['removeableCostMultiplier'] = data.get('removeableCostMultiplier', "")
    info['lives'] = data.get('lives', "")
    info['startRound'] = data.get('startRound', "")
    info['endRound'] = data.get('endRound', "")
    info['maxTowers'] = data.get('maxTowers', "")
    info['bloon_speed'] = data.get('_bloonModifiers', {}).get('speedMultiplier', "")
    info['moab_speed'] = data.get('_bloonModifiers', {}).get('moabSpeedMultiplier', "")
    info['regrow_rate'] = data.get('_bloonModifiers', {}).get('regrowRateMultiplier', "")
    info['all_camo'] = data.get('_bloonModifiers', {}).get('allCamo', "")
    info['all_regrow'] = data.get('_bloonModifiers', {}).get('allRegen', ""),
    info['ceramic_health'] = data.get('_bloonModifiers', {}).get("healthMultipliers", "").get("bloons", "")
    info['moab_health'] = data.get('_bloonModifiers', {}).get("healthMultipliers", "").get("moabs", "")

    # HERO
    tmp = data.get('_towers', [])
    for hero in tmp:
        hero_name = hero['tower'] 
        if hero_name in heros:    
            heros[hero_name] = hero['max'] 
    available_hero()

    # TOWER
    tmp = data.get('_towers', [])
    for tower in tmp:
        tower_name = tower['tower']
        if tower_name in towers:
            towers[tower_name]['max'] = tower['max']  
            towers[tower_name]['path1NumBlockedTiers'] = tower['path1NumBlockedTiers']
            towers[tower_name]['path2NumBlockedTiers'] = tower['path2NumBlockedTiers']
            towers[tower_name]['path3NumBlockedTiers'] = tower['path3NumBlockedTiers']
            total_tiers = 5 
            towers[tower_name]['path1NumBlockedTiers'] = total_tiers - (towers[tower_name]['path1NumBlockedTiers'] if towers[tower_name]['path1NumBlockedTiers'] != -1 else 5)
            towers[tower_name]['path2NumBlockedTiers'] = total_tiers - (towers[tower_name]['path2NumBlockedTiers'] if towers[tower_name]['path2NumBlockedTiers'] != -1 else 5)
            towers[tower_name]['path3NumBlockedTiers'] = total_tiers - (towers[tower_name]['path3NumBlockedTiers'] if towers[tower_name]['path3NumBlockedTiers'] != -1 else 5)
        
@tasks.loop(minutes=1)
async def check_for_advanced():
    global last_advanced_id
    channel = bot.get_channel(chan_id)
    result = Advanced()

    print(f"{datetime.today().strftime('%Y/%m/%d %H:%M:%S')}")

    try:

        if result:
            id_ = result
            if last_advanced_id != id_:
                last_advanced_id = id_
                embed=discord.Embed(title="고급도전 갱신!", url="https://data.ninjakiwi.com/btd6/challenges/filter/daily", description="오늘의 고급도전은?", color=0x00d4ff)
                embed.set_thumbnail(url=info["mapurl"])
                embed.add_field(name="이름", value=info["name"], inline=True)
                embed.add_field(name="고유 번호", value=info["id"], inline=True)
                embed.add_field(name="난이도", value=f"{info['diff']} {info['diff_mode']}", inline=True)
                embed.add_field(name="활성화", value="", inline=False)
                embed.add_field(name="더블 캐시", value=info["disableDoubleCash"], inline=True)
                embed.add_field(name="인스타 몽키", value=info["disableInstas"], inline=True)
                embed.add_field(name="지식", value=info["disableMK"], inline=True)
                embed.add_field(name="파워", value=info["disablePowers"], inline=True)
                embed.add_field(name="팔기", value=info["disableSelling"], inline=True)
                embed.add_field(name="규칙", value="", inline=False)
                embed.add_field(name="시작 캐시", value=info["startingCash"], inline=False)
                embed.add_field(name="시작 라운드", value=info["startRound"], inline=True)
                embed.add_field(name="끝 라운드", value=info["endRound"], inline=True)
                embed.add_field(name="생명", value=info["lives"], inline=True)
                embed.add_field(name="모두 캐모", value=info["all_camo"], inline=True)
                embed.add_field(name="모두 재생", value=info["all_regrow"], inline=True)
                embed.add_field(name="최대 캐시", value=info["leastCashUsed"], inline=True)
                embed.add_field(name="최대 티어", value=info["leastTiersUsed"], inline=True)
                embed.add_field(name="최대 타워", value=info["maxTowers"], inline=True)
                embed.set_footer(text=f"알림 시간 : {datetime.today().strftime('%Y/%m/%d %H:%M:%S')}")
                await channel.send(embed=embed)

                embed=discord.Embed(title="수치와 사용 영웅", description="오늘의 고급도전은?", color=0x00d4ff)
                embed.add_field(name="풍선 속도", value=info["bloon_speed"], inline=True)
                embed.add_field(name="MOAB 속도", value=info["moab_speed"], inline=True)
                embed.add_field(name="세라믹 체력", value=info["ceramic_health"], inline=True)
                embed.add_field(name="MOAB 체력", value=info["moab_health"], inline=True)
                embed.add_field(name="재생 속도", value=info["regrow_rate"], inline=True)
                embed.add_field(name="쿨타임", value=info["abilityCooldownReductionMultiplier"], inline=True)
                embed.add_field(name="장애물 비용", value=info["removeableCostMultiplier"], inline=True)
                if avaliable_heros:
                    embed.add_field(name="사용 영웅", value=avaliable_heros, inline=False)
                embed.set_footer(text=f"알림 시간 : {datetime.today().strftime('%Y/%m/%d %H:%M:%S')}")
                await channel.send(embed=embed)

                embed=discord.Embed(title="사용 타워", description="오늘의 고급도전은?", color=0x00d4ff)
                for tower_key, tower_name in tower_names.items():
                    if towers[tower_key]['max'] == -1:
                        embed.add_field(
                            name=tower_name, 
                            value=f"{towers[tower_key]['path1NumBlockedTiers']}-{towers[tower_key]['path2NumBlockedTiers']}-{towers[tower_key]['path3NumBlockedTiers']}", 
                            inline=True
                        )
                    elif towers[tower_key]['max'] != 0:
                        embed.add_field(
                            name=f"{tower_name} ({towers[tower_key]['max']})", 
                            value=f"{towers[tower_key]['path1NumBlockedTiers']}-{towers[tower_key]['path2NumBlockedTiers']}-{towers[tower_key]['path3NumBlockedTiers']}", 
                            inline=True
                        )
                embed.set_footer(text=f"알림 시간 : {datetime.today().strftime('%Y/%m/%d %H:%M:%S')}")
                await channel.send(embed=embed)
    except Exception as e:
        await channel.send(e)

@bot.event
async def on_ready():
    print(f"{bot.user} is ready and online!")
    check_for_advanced.start()

@bot.slash_command(name="ping", description="서버의 핑을 측정합니다.")
async def ping(ctx: discord.ApplicationContext):
    await ctx.respond("pong!")

bot.run(os.environ.get("TOKEN"))