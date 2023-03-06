#!/usr/bin/python3
#coding: utf-8
import telepot, time, magic, os

# telepot.api.set_proxy('http://192.168.0.1:3128',('usuario','senha'))

def principal(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)

    if content_type == 'document':
        bot.download_file(msg[content_type]['file_id'],msg[content_type]['file_id'])
        mensagem = "*O arquivo que você enviou é do tipo:* "
        mensagem += magic.from_file(msg[content_type]['file_id'])
        bot.sendMessage(chat_id,mensagem,parse_mode='Markdown')
        os.remove(msg[content_type]['file_id'])

bot = telepot.Bot('6293729431:AAGMg3IvVrP7FC4grj5kwXhlwzUZUQ1f8zI')
bot.message_loop(principal)

while 1:
    time.sleep(5)