
#!/usr/bin/python3
#coding: utf-8
import telepot, time

token = '6293729431:AAGMg3IvVrP7FC4grj5kwXhlwzUZUQ1f8zI'

def principal(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)

    if content_type == 'text':
        chat_id = msg['chat']['id']
        mensagem = msg['text']

        if mensagem.lower() == 'oi':
            bot.sendMessage(chat_id,"Olá, Mundo!")

bot = telepot.Bot(token)
bot.message_loop(principal)

while 1:
    time.sleep(5)