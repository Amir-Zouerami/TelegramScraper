from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty
from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty
from telethon import types
import csv

# ------ YOUR PERSONAL INFO
api_id = 0000000  # Replace this with your own api_id
api_hash = 'YOUR HASH HERE'  # Replace this with your own api_hash
phone = '+00000000000'  # Your phone number goes here with the area code and +
client = TelegramClient(phone, api_id, api_hash)

client.connect()
if not client.is_user_authorized():
    client.send_code_request(phone)
    client.sign_in(phone, input(
        'Enter the code sent to your Telegram account: '))


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

print('Choose a group to scrape members from:')
i = 0
for g in groups:
    print(str(i) + '- ' + g.title)
    i += 1

g_index = input("Enter a Number: ")
target_group = groups[int(g_index)]
filename = target_group.title


print('Fetching Members...')
all_participants = []
all_participants = client.get_participants(target_group, aggressive=True)

print('Saving In file...')
with open(("{}.csv".format(filename)), "w", encoding='UTF-8') as f:
    writer = csv.writer(f, delimiter=",", lineterminator="\n")
    writer.writerow(['username'])
    for user in all_participants:
        accept = True

        if (user.bot):
            accept = False

        elif (user.deleted):
            accept = False

        elif (user.username == 'None'):
            accept = False

        elif not user.username:
            accept = False

        elif (user.is_self):
            accept = False

        elif (isinstance(user.status, types.UserStatusRecently)):
            accept = True

        elif (isinstance(user.status, types.UserStatusLastWeek)):
            accept = True

        elif (isinstance(user.status, types.UserStatusLastMonth)):
            accept = False

        elif (isinstance(user.status, types.UserStatusOnline)):
            accept = True

        elif (isinstance(user.status, types.UserStatusOffline)):
            accept = False
        else:
            accept = False

        if (accept):
            if user.username:
                username = "@" + user.username
            else:
                username = ""
            if user.first_name:
                first_name = user.first_name
            else:
                first_name = ""
            if user.last_name:
                last_name = user.last_name
            else:
                last_name = ""
            name = (first_name + ' ' + last_name).strip()
            writer.writerow([name, username])

print('Members scraped successfully.')
