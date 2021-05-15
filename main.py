# Importing [ 임포트 ] | 모듈을 불러옵니다!
import discord # Discord 모듈
import asyncio # Async 모듈
import random # Random 모듈
import datetime # Datetime 모듈
import time # Time 모듈
import json # Json 모듈
import bs4 # Bs4 모듈
from bs4 import BeautifulSoup # Bs4 에서 불러오는 BeautifulSoup 모듈
from urllib.request import Request # Urllib 모듈 1
from urllib.request import URLError # 2
from urllib.request import HTTPError # 3
from urllib.request import urlopen # 4
from urllib.request import Request, urlopen # 5
from urllib.request import quote # 6
from urllib.request import urlopen, Request # 7
import urllib # Urllib 모듈
import requests # Requests 모듈

# ---------------------------------------------------------------------------------------------------- #

# Seting [ 설정 ] | 기본 정보를 세팅합니다!
p = "." # Prefix ( 접두사 ) 설정
prefix = "."
b_token = "ODQwOTMyOTcyNjc2MTIwNTk2.YJfZ3A.2V8ZVAZpzn8y1sXnopf5Nn-Dips" # Bot Token ( 봇 토큰 ) 설정
login_msg = "On" # 로그인 메시지 설정
staff = [653075791814590487]
cense = discord.Client()
client = discord.Client()
client_secret = "BFM_f72uFU"

# ---------------------------------------------------------------------------------------------------- #

# Bot Login Message [ 봇 로그인 메시지 ] | 봇이 로그인 됐을때 콘솔에 출력될 내용을 설정합니다.
@cense.event
async def on_ready():
    print(login_msg) # login_msg를 수정하세요.
    print("Work BOT")

# ---------------------------------------------------------------------------------------------------- #

@cense.event
async def on_message(message):
    if message.content.startswith(f'{p}수수료'):
        won = split[1]
        ssla = split[2]
        sslghm = "%.2f" % (float(ssla) * float(won) / 100.0)
        gap = float(won)+float(sslghm)
        sslembed = discord.Embed(title="수수료 구하기", description=f"원가 - {won}.00\n\n수수료 - {sslghm} ( {ssla} % )\n\n총합 - {gap}0", color=discord.Color.gold())
        await message.channel.send(embed=sslembed)
async def on_message(message):
    if message.content == f'{p}가입' or message.content == f'{p}가입':
        await open_account(message.author)
        users = await get_bank_data()
        user = message.author
        if users[str(user.id)]["verify"] == "N":
                embed = discord.Embed(title="Wait Please!", description="가입을 위해 준비하는 중이에요!", color=discord.Color.gold())
                embed.set_footer(text=f"{message.author} | 가입 준비중!")
                embed1 = await message.channel.send(embed=embed)
                time.sleep(2)
                await embed1.delete()
                embeds = discord.Embed(title="가입 주의사항", description="가입이 완료되면 서비스에서 일부 개인정보를 수집하는것에 대해 동의하는 것으로 간주합니다. \n 동의하려면 ✅로 반응하세요.", color=discord.Color.gold())
                m = await message.channel.send(f"{message.author.mention}", embed=embeds)
                await m.add_reaction('✅')
                await m.add_reaction('❎')
                try:
                    reaction, user = await cense.wait_for('reaction_add', timeout = 5, check = lambda reaction, user: user == message.author and str(reaction.emoji) in ['✅', '❎'])
                except asyncio.TimeoutError:
                    await m.delete()
                    embeds = discord.Embed(title="Time Out!", description="다시 시도해주세요!", color=discord.Color.red())
                    await message.channel.send(f"{message.author.mention}", embed=embeds)
                else:
                    if str(reaction.emoji) == "❎":
                        await m.delete()
                        noembed = discord.Embed(title="Failed!", description="가입을 취소했어요.", color = discord.Color.red())
                        await message.channel.send(f"{message.author.mention}", embed=noembed)
                    elif str(reaction.emoji) == "✅":
                        await m.delete()
                        yesembed = discord.Embed(title="Sucsess!", description=f"가입을 완료했어요!\n이제 모든 기능을 이용하실 수 있어요.", color = discord.Color.green())
                        await message.channel.send(f"{message.author.mention}", embed=yesembed)
                        users[str(user.id)]["verify"] = "Y"
                    with open("main.json", "w") as f:
                        json.dump(users,f)
        else:
            errorembed = discord.Embed(title="Failed!", description="이미 가입되어 있어요.", color = discord.Color.red())
            await message.channel.send(embed=errorembed)

    if message.content == f'{p}레벨':
        await open_account(message.author)
        users = await get_bank_data()
        user = message.author
        if users[str(user.id)]["verify"] == "Y":
            levelxp_am = users[str(user.id)]["levelxp"]
            if levelxp_am <= 1000:
                bronzeembed = discord.Embed(title="[ Tier - Bronze ]", description=f"현재 [ {message.author.name} ] 님의 포인트는 {levelxp_am}입니다!", color=0x966147) # 브론즈
                bronzeembed.set_thumbnail(url="https://media.discordapp.net/attachments/777143534440284161/777165159238991872/1-removebg-preview.png?width=367&height=349")
                await message.channel.send(embed=bronzeembed)
            if 1001 <= levelxp_am <= 5000:
                silverembed = discord.Embed(title="[ Tier - Silver ]", description=f"현재 [ {message.author.name} ] 님의 포인트는 {levelxp_am}입니다!", color=0xC0C0C0) # 실버
                silverembed.set_thumbnail(url='https://media.discordapp.net/attachments/777143534440284161/777165222459867186/2-removebg-preview.png?width=367&height=349')
                await message.channel.send(embed=silverembed)
            if 5001 <= levelxp_am <= 15000:
                goldembed = discord.Embed(title="[ Tier - Gold ]", description=f"현재 [ {message.author.name} ] 님의 포인트는 {levelxp_am}입니다!", color=0xFFD700) # 골드
                goldembed.set_thumbnail(url='https://media.discordapp.net/attachments/777143534440284161/777165309043802122/3-removebg-preview.png?width=367&height=349')
                await message.channel.send(embed=goldembed)
            if 15001 <= levelxp_am <= 30000:
                platinumembed = discord.Embed(title="[ Tier - Platinum ]", description=f"현재 [ {message.author.name} ] 님의 포인트는 {levelxp_am}입니다!", color=0x84A7D3) # 플레티넘
                platinumembed.set_thumbnail(url='https://media.discordapp.net/attachments/777143534440284161/777165410088517662/4-removebg-preview.png?width=367&height=349')
                await message.channel.send(embed=platinumembed)
            if 30001 <= levelxp_am <= 50000:
                diamondembed = discord.Embed(title="[ Tier - Diamond ]", description=f"현재 [ {message.author.name} ] 님의 포인트는 {levelxp_am}입니다!", color=0x00BFFF) # 다이아몬드
                await message.channel.send(embed=diamondembed)
            if 50001 <= levelxp_am:
                masterembed = discord.Embed(title="[ Tier - Master ]", description=f"현재 [ {message.author.name} ] 님의 포인트는 {levelxp_am}입니다!", color=0xFEE134) # 마스터
                masterembed.set_thumbnail(url='https://media.discordapp.net/attachments/777143534440284161/777165571288203264/5-removebg-preview.png?width=367&height=349')
                await message.channel.send(embed=masterembed)
        else:
            await message.channel.send('가입이 필요한 기능입니다.')

    if message.content.startswith(""):
        await open_account(message.author)
        users = await get_bank_data()
        user = message.author
        if users[str(user.id)]["verify"] == "Y":
            users[str(user.id)]["levelxp"] += 1
            with open('main.json','w') as f:
                json.dump(users,f)
    
    if message.content.startswith(""):
        await open_account(message.author)
        users = await get_bank_data()
        user = message.author
        if users[str(user.id)]["verify"] == "Y":
            levelxp_am = users[str(user.id)]["levelxp"]
            if levelxp_am == 1001:
                silverrankupembed = discord.Embed(title="[ Rank UP! ]", description=f"{message.author.mention}, Silver로 랭크업 했어요! \n Level XP - {levelxp_am}", color=0xC0C0C0)
                silverrankupembed.set_image(url='https://media.discordapp.net/attachments/776741529854148610/777178029297762304/2.PNG?width=622&height=350')
                await message.channel.send(embed=silverrankupembed)
            if levelxp_am == 5001:
                goldrankupembed = discord.Embed(title="[ Rank UP! ]", description=f"{message.author.mention}, Gold로 랭크업 했어요! \n Level XP - {levelxp_am}", color=0xFFD700)
                goldrankupembed.set_image(url='https://media.discordapp.net/attachments/776741529854148610/777178039636721695/3.PNG?width=622&height=350')
                await message.channel.send(embed=goldrankupembed)
            if levelxp_am == 15001:
                platinumrankupembed = discord.Embed(title="[ Rank UP! ]", description=f"{message.author.mention}, Platinum으로 랭크업 했어요! \n Level XP - {levelxp_am}", color=0x84A7D3)
                platinumrankupembed.set_image(url='https://media.discordapp.net/attachments/776741529854148610/777178049560051752/4.PNG?width=622&height=350')
                await message.channel.send(embed=platinumrankupembed)
            if levelxp_am == 30001:
                diamondrankupembed = discord.Embed(title="[ Rank UP! ]", description=f"{message.author.mention}, Diamond로 랭크업 했어요! \n Level XP - {levelxp_am}", color=0x00BFFF)
                diamondrankupembed.set_image(url='https://media.discordapp.net/attachments/776741529854148610/777178060599459860/5.PNG?width=622&height=350')
                await message.channel.send(embed=diamondrankupembed)
            if levelxp_am == 50001:
                masterrankupembed = discord.Embed(title="[ Rank UP! ]", description=f"{message.author.mention}, Master로 랭크업 했어요! \n Level XP - {levelxp_am}", color=0xFEE134)
                masterrankupembed.set_image(url='https://media.discordapp.net/attachments/776741529854148610/777180752936042526/S.png?width=622&height=350')
                await message.channel.send(embed=masterrankupembed)      

    if message.content == f'{p}내정보':
        await open_account(message.author)
        users = await get_bank_data()
        user = message.author
        if users[str(user.id)]["verify"] == "Y":
            buyox = users[str(user.id)]["buy"]
            money = users[str(user.id)]["money"]
            premium = users[str(user.id)]["premium"]
            infoembed = discord.Embed(title=f"{message.author.name} Info!",color=discord.Color.gold())
            infoembed.add_field(name="이름 | 고유 ID", value=f"{message.author.name} | {message.author.id}",inline=False)
            infoembed.add_field(name="구매여부", value=f"{buyox}\nY = Yes | N = No",inline=False)
            infoembed.add_field(name="보유잔고", value=f"{money}원",inline=False)
            infoembed.add_field(name="프리미엄", value=f"{premium}\nY = Yes | N = No")
            await message.channel.send(embed=infoembed)
        else:
            await message.channel.send('가입이 필요한 기능이에요!')
            


    if (message.content.split(" ")[0] == "!ban"):
        if (message.author.guild_permissions.ban_members):
            try:
                user = message.guild.get_member(int(message.content.split(' ')[1][2:20]))
                reason = message.content[22:]
                if (len(message.content.split(" ")) == 2):
                    reason = "None"
                await user.send("YOUR BANNED {message.guild.name} FROM THIS SERVER!  ",
                                " 당신은 **{message.guild.name}** 서버에서 차단되었습니다. 사유는 다음과 같습니다. ```{reason}```https://media.giphy.com/media/fe4dDMD2cAU5RfEaCU/giphy.gif ")
                await user.ban(reason=reason)
                await message.channel.send('<:check:776737893120999446>  밴을 완료했어요. https://media.giphy.com/media/Vh2c84FAPVyvvjZJNM/giphy.gif')
            except Exception as e:
                await message.channel.send(embed=discord.Embed(title="❌ 에러 발생", description=str(e), color=0xff0000))
                return
        else:
            await message.channel.send(embed=discord.Embed(title="⚠ 권한 부족",
                                                           description=message.author.mention + "님은 유저를 차단할 수 있는 권한이 없습니다.",
                                                           color=0xff0000))
            return

    if message.content.startswith(f"{prefix}영한번역"):            
        channel = message.channel
        url="https://openapi.naver.com/v1/papago/n2mt?source=en&target=ko&text="
        text = message.content[6:]
        if text == "":
            em = discord.Embed(title="⚠ㅣError!",description=f"번역할 내용을 입력하지 않았어요!\n양식 ) {prefix}한영번역 <내용>")
            await message.channel.send(embed=em)
        request_url = "https://openapi.naver.com/v1/papago/n2mt"
        headers= {"X-Naver-Client-Id": "R8G3abanLWy30ddsPLWt", "X-Naver-Client-Secret": "BFM_f72uFU"}
        params = {"source": "en", "target": "ko", "text": text}
        response = requests.post(request_url, headers=headers, data=params)
        result = response.json()
        result = result['message']['result']['translatedText']
        em = discord.Embed(title=":flag_us: > :flag_kr: 번역 성공!", description=f":flag_us: - {text} \n:flag_kr: - {result}",color = discord.Color.gold())
        await message.channel.send(embed=em)
    
    
    if message.content.startswith(f"{prefix}영일번역"):
        channel = message.channel
        url="https://openapi.naver.com/v1/papago/n2mt?source=en&target=ja&text="
        text = message.content[6:]
        if text == "":
            em = discord.Embed(title="⚠ㅣError!",description=f"번역할 내용을 입력하지 않았어요!\n양식 ) {prefix}한영번역 <내용>")
            await message.channel.send(embed=em)
        request_url = "https://openapi.naver.com/v1/papago/n2mt"
        headers= {"X-Naver-Client-Id": "R8G3abanLWy30ddsPLWt", "X-Naver-Client-Secret": "BFM_f72uFU"}
        params = {"source": "en", "target": "ja", "text": text}
        response = requests.post(request_url, headers=headers, data=params)
        result = response.json()
        result = result['message']['result']['translatedText']
        em = discord.Embed(title=":flag_us: > :flag_jp: 번역 성공!", description=f":flag_us: - {text} \n:flag_jp: - {result}",color = discord.Color.gold())
        await message.channel.send(embed=em)
    
    
    if message.content.startswith(f"{prefix}영중번역"):
        channel = message.channel
        url="https://openapi.naver.com/v1/papago/n2mt?source=en&target=zh-CN&text="
        text = message.content[6:]
        if text == "":
            em = discord.Embed(title="⚠ㅣError!",description=f"번역할 내용을 입력하지 않았어요!\n양식 ) {prefix}한영번역 <내용>")
            await message.channel.send(embed=em)
        request_url = "https://openapi.naver.com/v1/papago/n2mt"
        headers= {"X-Naver-Client-Id": "R8G3abanLWy30ddsPLWt", "X-Naver-Client-Secret": "BFM_f72uFU"}
        params = {"source": "en", "target": "zh-CN", "text": text}
        response = requests.post(request_url, headers=headers, data=params)
        result = response.json()
        result = result['message']['result']['translatedText']
        em = discord.Embed(title=":flag_us: > :flag_cn: 번역 성공!", description=f":flag_us: - {text} \n:flag_cn: - {result}",color = discord.Color.gold())
        await message.channel.send(embed=em)
    
    
    if message.content.startswith(f"{prefix}한영번역"):
        channel = message.channel
        url="https://openapi.naver.com/v1/papago/n2mt?source=ko&target=en&text="
        text = message.content[6:]
        if text == "":
            em = discord.Embed(title="⚠ㅣError!",description=f"번역할 내용을 입력하지 않았어요!\n양식 ) {prefix}한영번역 <내용>")
            await message.channel.send(embed=em)
        request_url = "https://openapi.naver.com/v1/papago/n2mt"
        headers= {"X-Naver-Client-Id": "R8G3abanLWy30ddsPLWt", "X-Naver-Client-Secret": "BFM_f72uFU"}
        params = {"source": "ko", "target": "en", "text": text}
        response = requests.post(request_url, headers=headers, data=params)
        result = response.json()
        result = result['message']['result']['translatedText']
        em = discord.Embed(title=":flag_kr: > :flag_us: 번역 성공!", description=f":flag_kr: - {text} \n:flag_us: - {result}",color = discord.Color.gold())
        await message.channel.send(embed=em)
    
    
    if message.content.startswith(f"{prefix}한일번역"):
        channel = message.channel
        url="https://openapi.naver.com/v1/papago/n2mt?source=ko&target=ja&text="
        text = message.content[6:]
        if text == "":
            em = discord.Embed(title="⚠ㅣError!",description=f"번역할 내용을 입력하지 않았어요!\n양식 ) {prefix}한영번역 <내용>")
            await message.channel.send(embed=em)
        request_url = "https://openapi.naver.com/v1/papago/n2mt"
        headers= {"X-Naver-Client-Id": "R8G3abanLWy30ddsPLWt", "X-Naver-Client-Secret": "BFM_f72uFU"}
        params = {"source": "ko", "target": "ja", "text": text}
        response = requests.post(request_url, headers=headers, data=params)
        result = response.json()
        result = result['message']['result']['translatedText']
        em = discord.Embed(title=":flag_kr: > :flag_jp: 번역 성공!", description=f":flag_kr: - {text} \n:flag_jp: - {result}",color = discord.Color.gold())
        await message.channel.send(embed=em)

    
    
    if message.content.startswith(f"{prefix}한중번역"):
        channel = message.channel
        url="https://openapi.naver.com/v1/papago/n2mt?source=ko&target=zh-CN&text="
        text = message.content[6:]
        if text == "":
            em = discord.Embed(title="⚠ㅣError!",description=f"번역할 내용을 입력하지 않았어요!\n양식 ) {prefix}한영번역 <내용>")
            await message.channel.send(embed=em)
        request_url = "https://openapi.naver.com/v1/papago/n2mt"
        headers= {"X-Naver-Client-Id": "R8G3abanLWy30ddsPLWt", "X-Naver-Client-Secret": "BFM_f72uFU"}
        params = {"source": "ko", "target": "zh-CN", "text": text}
        response = requests.post(request_url, headers=headers, data=params)
        result = response.json()
        result = result['message']['result']['translatedText']
        em = discord.Embed(title=":flag_kr: > :flag_cn: 번역 성공!", description=f":flag_kr: - {text} \n:flag_cn: - {result}",color = discord.Color.gold())
        await message.channel.send(embed=em)

    if message.content.startswith(f"{prefix}일한번역"):
        channel = message.channel
        url="https://openapi.naver.com/v1/papago/n2mt?source=ja&target=ko&text="
        text = message.content[6:]
        if text == "":
            em = discord.Embed(title="⚠ㅣError!",description=f"번역할 내용을 입력하지 않았어요!\n양식 ) {prefix}일한번역 <내용>")
            await message.channel.send(embed=em)
        request_url = "https://openapi.naver.com/v1/papago/n2mt"
        headers= {"X-Naver-Client-Id": "R8G3abanLWy30ddsPLWt", "X-Naver-Client-Secret": "BFM_f72uFU"}
        params = {"source": "ja", "target": "ko", "text": text}
        response = requests.post(request_url, headers=headers, data=params)
        result = response.json()
        result = result['message']['result']['translatedText']
        em = discord.Embed(title=":flag_jp: > :flag_kr: 번역 성공!", description=f":flag_jp: - {text} \n:flag_kr: - {result}",color = discord.Color.gold())
        await message.channel.send(embed=em)
            
    if message.content.startswith(f"{prefix}일영번역"):
        channel = message.channel
        url="https://openapi.naver.com/v1/papago/n2mt?source=ja&target=en&text="
        text = message.content[6:]
        if text == "":
            em = discord.Embed(title="⚠ㅣError!",description=f"번역할 내용을 입력하지 않았어요!\n양식 ) {prefix}일영번역 <내용>")
            await message.channel.send(embed=em)
        request_url = "https://openapi.naver.com/v1/papago/n2mt"
        headers= {"X-Naver-Client-Id": "R8G3abanLWy30ddsPLWt", "X-Naver-Client-Secret": "BFM_f72uFU"}
        params = {"source": "ja", "target": "en", "text": text}
        response = requests.post(request_url, headers=headers, data=params)
        result = response.json()
        result = result['message']['result']['translatedText']
        em = discord.Embed(title=":flag_jp: > :flag_us: 번역 성공!", description=f":flag_jp: - {text} \n:flag_us: - {result}",color = discord.Color.gold())
        await message.channel.send(embed=em)
        
    if message.content.startswith(f"{prefix}일중번역"):
        channel = message.channel
        url="https://openapi.naver.com/v1/papago/n2mt?source=ja&target=zh-CN&text="
        text = message.content[6:]
        if text == "":
            em = discord.Embed(title="⚠ㅣError!",description=f"번역할 내용을 입력하지 않았어요!\n양식 ) {prefix}일중번역 <내용>")
            await message.channel.send(embed=em)
        request_url = "https://openapi.naver.com/v1/papago/n2mt"
        headers= {"X-Naver-Client-Id": "R8G3abanLWy30ddsPLWt", "X-Naver-Client-Secret": "BFM_f72uFU"}
        params = {"source": "ja", "target": "zh-CN", "text": text}
        response = requests.post(request_url, headers=headers, data=params)
        result = response.json()
        result = result['message']['result']['translatedText']
        em = discord.Embed(title=":flag_jp: > :flag_cn: 번역 성공!", description=f":flag_jp: - {text} \n:flag_cn: - {result}",color = discord.Color.gold())
        await message.channel.send(embed=em)
            
    if message.content.startswith(f"{prefix}중일번역"):
        channel = message.channel
        url="https://openapi.naver.com/v1/papago/n2mt?source=zh-CN&target=ja&text="
        text = message.content[6:]
        if text == "":
            em = discord.Embed(title="⚠ㅣError!",description=f"번역할 내용을 입력하지 않았어요!\n양식 ) {prefix}중일번역 <내용>")
            await message.channel.send(embed=em)
        request_url = "https://openapi.naver.com/v1/papago/n2mt"
        headers= {"X-Naver-Client-Id": "R8G3abanLWy30ddsPLWt", "X-Naver-Client-Secret": "BFM_f72uFU"}
        params = {"source": "zh-CN", "target": "ja", "text": text}
        response = requests.post(request_url, headers=headers, data=params)
        result = response.json()
        result = result['message']['result']['translatedText']
        em = discord.Embed(title=":flag_cn: > :flag_jp: 번역 성공!", description=f":flag_cn: - {text} \n:flag_jp: - {result}",color = discord.Color.gold())
        await message.channel.send(embed=em)

    if message.content.startswith(f"{prefix}중영번역"):
        channel = message.channel
        url="https://openapi.naver.com/v1/papago/n2mt?source=zh-CN&target=en-CN&text="
        text = message.content[6:]
        if text == "":
            em = discord.Embed(title="⚠ㅣError!",description=f"번역할 내용을 입력하지 않았어요!\n양식 ) {prefix}중영번역 <내용>")
            await message.channel.send(embed=em)
        request_url = "https://openapi.naver.com/v1/papago/n2mt"
        headers= {"X-Naver-Client-Id": "R8G3abanLWy30ddsPLWt", "X-Naver-Client-Secret": "BFM_f72uFU"}
        params = {"source": "zh-CN", "target": "en", "text": text}
        response = requests.post(request_url, headers=headers, data=params)
        result = response.json()
        result = result['message']['result']['translatedText']
        em = discord.Embed(title=":flag_cn: > :flag_us: 번역 성공!", description=f":flag_cn: - {text} \n:flag_us: - {result}",color = discord.Color.gold())
        await message.channel.send(embed=em)

    if message.content.startswith(f"{prefix}중한번역"):
        channel = message.channel
        url="https://openapi.naver.com/v1/papago/n2mt?source=zh-CN&target=ko-CN&text="
        text = message.content[6:]
        if text == "":
            em = discord.Embed(title="⚠ㅣError!",description=f"번역할 내용을 입력하지 않았어요!\n양식 ) {prefix}중한번역 <내용>")
            await message.channel.send(embed=em)
        request_url = "https://openapi.naver.com/v1/papago/n2mt"
        headers= {"X-Naver-Client-Id": "R8G3abanLWy30ddsPLWt", "X-Naver-Client-Secret": "BFM_f72uFU"}
        params = {"source": "zh-CN", "target": "ko", "text": text}
        response = requests.post(request_url, headers=headers, data=params)
        result = response.json()
        result = result['message']['result']['translatedText']
        em = discord.Embed(title=":flag_cn: > :flag_kr: 번역 성공!", description=f":flag_cn: - {text} \n:flag_kr: - {result}",color = discord.Color.gold())
        await message.channel.send(embed=em)
    if message.content.startswith(f"{prefix}한태번역"):
        channel = message.channel
        url="https://openapi.naver.com/v1/papago/n2mt?source=ko&target=th&text="
        text = message.content[6:]
        if text == "":
            em = discord.Embed(title="⚠ㅣError!",description=f"번역할 내용을 입력하지 않았어요!\n양식 ) {prefix}한태번역 <내용>")
            await message.channel.send(embed=em)
        request_url = "https://openapi.naver.com/v1/papago/n2mt"
        headers= {"X-Naver-Client-Id": "R8G3abanLWy30ddsPLWt", "X-Naver-Client-Secret": "BFM_f72uFU"}
        params = {"source": "ko", "target": "th", "text": text}
        response = requests.post(request_url, headers=headers, data=params)
        result = response.json()
        result = result['message']['result']['translatedText']
        em = discord.Embed(title=":flag_kr: > :flag_th: 번역 성공!", description=f":flag_kr: - {text} \n:flag_th: - {result}",color = discord.Color.gold())
        await message.channel.send(embed=em)
    if message.content.startswith(f"{prefix}태한번역"):
        channel = message.channel
        url="https://openapi.naver.com/v1/papago/n2mt?source=th&target=ko&text="
        text = message.content[6:]
        if text == "":
            em = discord.Embed(title="⚠ㅣError!",description=f"번역할 내용을 입력하지 않았어요!\n양식 ) {prefix}태한번역 <내용>")
            await message.channel.send(embed=em)
        request_url = "https://openapi.naver.com/v1/papago/n2mt"
        headers= {"X-Naver-Client-Id": "R8G3abanLWy30ddsPLWt", "X-Naver-Client-Secret": "BFM_f72uFU"}
        params = {"source": "th", "target": "ko", "text": text}
        response = requests.post(request_url, headers=headers, data=params)
        result = response.json()
        result = result['message']['result']['translatedText']
        em = discord.Embed(title=":flag_th: > :flag_kr: 번역 성공!", description=f":flag_th: - {text} \n:flag_kr: - {result}",color = discord.Color.gold())
        await message.channel.send(embed=em)
    if message.content.startswith("!DM"):
        me = get(message.guild.members, id=763312320884506675)
        channel = await me.create_dm()
        await channel.send("DM발신 성공!")
        await message.channel.send(f"{message.author.mention}님,DM이 발송되었습니다!")
# Json Seting
async def open_account(user):

    users = await get_bank_data()

    if str(user.id) in users:
        return False
    else:
        users[str(user.id)] = {}
        users[str(user.id)]["levelxp"] = 0
        users[str(user.id)]["buy"] = "N"
        users[str(user.id)]["money"] =  0
        users[str(user.id)]["verify"] = "N"
        users[str(user.id)]["premium"] = "N"
        users[str(user.id)]["id"] = user.id
    with open("main.json","w") as f:
        users = json.dump(users,f)
    return True


async def get_bank_data():
    with open("main.json","r") as f:
        users = json.load(f)

    return users

cense.run(b_token)
