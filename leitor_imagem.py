#!/usr/bin/python3
#coding: utf-8
import telepot, time
from PIL import Image
import pytesseract

# telepot.api.set_proxy('http://192.168.0.1:3128',('usuário','senha'))

def principal(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)

    if content_type == 'photo':
        caminho = ""
        imagem = msg[content_type][-1]['file_unique_id'] + ".jpg"
        bot.download_file(msg[content_type][-1]['file_id'], caminho + imagem)
        pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
        tessdata_dir_config = '--tessdata-dir "C:\\Program Files\\Tesseract-OCR\\tessdata"'
        foto = Image.open(imagem + caminho)
        texto = pytesseract.image_to_string(foto, lang='por', config=tessdata_dir_config)
        bot.sendMessage(chat_id,"O texto da imagem:\n" + texto)

bot = telepot.Bot('6293729431:AAGMg3IvVrP7FC4grj5kwXhlwzUZUQ1f8zI')
bot.message_loop(principal)

while 1:
        time.sleep(5)