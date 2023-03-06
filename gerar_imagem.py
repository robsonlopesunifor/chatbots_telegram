
#!/usr/bin/python3
#coding: utf-8
import telepot, time
from PIL import Image, ImageDraw, ImageFont

# telepot.api.set_proxy('http://192.168.0.7:3128',('usuário','senha'))

def principal(msg):
        content_type, chat_type, chat_id = telepot.glance(msg)

        if content_type == 'text':
            chat_id = msg['chat']['id']
            mensagem = msg['text']

            if mensagem.upper()[0:6] == 'IMAGEM':
                texto = mensagem.split(':')
                img = Image.new('RGB', (100, 30), color = 'red')
                fnt = ImageFont.truetype('C:\Windows\Fonts\calibri.ttf', 15)
                d = ImageDraw.Draw(img)
                d.text((10,10), texto[1], font=fnt, fill=(255,255,255))
                img.save('teste.png')
                bot.sendPhoto(chat_id,photo=open("teste.png","rb"))

bot = telepot.Bot('6293729431:AAGMg3IvVrP7FC4grj5kwXhlwzUZUQ1f8zI')
bot.message_loop(principal)

while 1:
    time.sleep(5)