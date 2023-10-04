import os
import confign
import utils

#Подгрузка данных
localhost = confign.localhost
channel_id = confign.channelid
messagesl = confign.messages
useragent = confign.useragent
token = confign.token
media = confign.media
dump = confign.dump
crypto = confign.dump
print("""
╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╭╮
╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱┃┃
╭╮╭┳━━┳━━┳━━┳┳╮╱╭┫┃╭┳━━╮
┃╰╯┃╭╮┃━━┫╭╮┣┫┃╱┃┃╰╯┫╭╮┃
┃┃┃┃╰╯┣━━┃╭╮┃┃╰━╯┃╭╮┫╭╮┃
╰┻┻┻━━┻━━┻╯╰┻┻━╮╭┻╯╰┻╯╰╯
╱╱╱╱╱╱╱╱╱╱╱╱╱╭━╯┃
╱╱╱╱╱╱╱╱╱╱╱╱╱╰━━╯""")
#ms

if dump == "txt":
    utils.get_messages(channel_id, messagesl, token, useragent, media)
else:
    utils.write_messages_to_json(channel_id, messagesl, token, useragent, media)
#ms