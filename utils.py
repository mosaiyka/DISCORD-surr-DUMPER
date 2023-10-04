import os
import random
import requests
import json
from urllib.parse import quote

def write_messages_to_json(channel_id, count, token, useragent, media):
    n = 0
    headers = {
        'User-Agent': f'{useragent}',
        'Authorization': f'{token}'
    }
    params = {
        'limit': 100
    }
    messages = []

    while count > 0:
        response = requests.get(url=f'https://discord.com/api/v8/channels/{channel_id}/messages', headers=headers, params=params)

        if response.status_code == 200:
            new_messages = response.json()
            messages.extend(new_messages)

            if len(new_messages) < 100:
                break

            params['before'] = new_messages[-1]['id']
            count -= 100
        else:
            print('Ошибка при получении сообщений.')
            return

    message_data = []
    pro = 0

    for message in messages:
        pro += 1
        print(f"{pro}/{len(messages)}")
        message_info = {
            "id message": message['id'],
            "id user": message['author']['id'],
            "nickname": message['author']['username'],
            "datatime": message['timestamp'],
            "content message": message['content']
        }
        message_data.append(message_info)

    with open('messages.json', 'w', encoding='utf-8') as file:
        json.dump(message_data, file, indent=4, ensure_ascii=False)
    if media == True:
        if not os.path.exists('media'):
            os.makedirs('media')
        for message in messages:
            if 'attachments' in message:
                attachments = message['attachments']
                for attachment in attachments:
                    file_url = attachment['url']
                    file_name = quote(attachment['filename'])
                    file_path = os.path.join('media', file_name)
                    response = requests.get(file_url)
                    if response.status_code == 200:
                        with open(file_path, 'wb') as file:
                            file.write(response.content)
                            n += 1
                            print(f"download: {n}/{len(messages)}")
                else:
                    print("\n")
                    #print(f'Ошибка при загрузке файла с URL: {file_url}')

    print('Сообщения успешно записаны в файл JSON.')
    
def get_server_name(server_id):
    headers = {
        'User-Agent': f'{useragent}',
        'Authorization': f'{token}'
    }

    response = requests.get(f'https://discord.com/api/v8/guilds/{server_id}', headers=headers)

    if response.status_code == 200:
        server_data = response.json()
        return server_data['name']
    else:
        print(f'Ошибка при получении информации о сервере {server_id}')
        return 'Unknown Server'

def get_messages(channel_id, count, token, useragent, media):
    n = 0
    headers = {
        'User-Agent': f'{useragent}',
        'Authorization': f'{token}'
    }
    params = {
        'limit': 100
    }
    messages = []
    
    while count > 0:
        response = requests.get(url=f'https://discord.com/api/v8/channels/{channel_id}/messages', headers=headers, params=params)
        
        if response.status_code == 200:
            new_messages = response.json()
            messages.extend(new_messages)
            
            if len(new_messages) < 100:
                break

            params['before'] = new_messages[-1]['id']
            count -= 100
        else:
            print('Ошибка при получении сообщений.')
            return

    words = []
    mes = count
    pro = 0
    for message in messages:
        pro += 1
        mm = [f"{message['id']}\n{message['timestamp']}\n{message['author']['id']}:{message['author']['username']}\n{message['content']}\n"]
        words = words + mm
        print(f"{pro}/{mes}")


    with open('messages.txt', 'a') as file:
        file.write('\n'.join(words))
        
    if media == True:
        if not os.path.exists('media'):
            os.makedirs('media')
        for message in messages:
            if 'attachments' in message:
                attachments = message['attachments']
                for attachment in attachments:
                    file_url = attachment['url']
                    file_name = quote(attachment['filename'])
                    file_path = os.path.join('media', file_name)
                    response = requests.get(file_url)
                    if response.status_code == 200:
                        with open(file_path, 'wb') as file:
                            file.write(response.content)
                            n += 1
                            print(f"download: {n}/{len(messages)}")
                else:
                    print("\n")
                    #print(f'Ошибка при загрузке файла с URL: {file_url}')
            
    print('Сообщения успешно записаны в файл.')
        