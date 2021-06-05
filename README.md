# What is it?
There are two scripts in this repository:
- AutoExtract.py
- ManualExtraction.py

Both scripts help you scrape Telegram group members using [Telegram API](https://my.telegram.org/) and [Telethon](https://github.com/LonamiWebs/Telethon). The difference is `AutoExtract.py` will scrape all groups automatically, creating a seperate csv file for each group while `ManualExtraction.py` will list all your groups and prompt you to chose a specific one.

# How to use?
There is a code in both scripts that looks like this:
```python
# ------ YOUR PERSONAL INFO
api_id = 0000000  # Replace this with your own api_id
api_hash = 'YOUR HASH HERE'  # Replace this with your own api_hash
phone = '+00000000000'  # Your phone number goes here with the area code and +
client = TelegramClient(phone, api_id, api_hash)
```
You have to go to [your personal Telegram API](https://my.telegram.org/) page and get `api_id` and `api_hash`. Then enter those values in the appropriate place. Also make sure to put your phone number in `phone`.

# Dependencies
You have to have [Telethon](https://github.com/LonamiWebs/Telethon) installed to run these scripts.


# License
This repository follows an MIT license.
