
#!/usr/bin/python3
#coding: utf-8
import telepot, time, json, requests
from datetime import date, timedelta

 
codigo_monicipio = "2304400"

def principal(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)

    if content_type == 'text':
        chat_id = msg['chat']['id']
        mensagem = msg['text']

        if mensagem.upper() == 'CLIMA':
            requisicao = requests.get("https://apiprevmet3.inmet.gov.br/previsao/"+codigo_monicipio).json()
            data = date.today()
            resposta = "O clima para " + requisicao[codigo_monicipio][str(data.strftime("%d/%m/%Y"))]["manha"]["entidade"] + "\n"
            for i in range(2):
                dataf = data.strftime("%d/%m/%Y")
                resposta += dataf + "\nmanhã - " + requisicao[codigo_monicipio][str(dataf)]["manha"]["resumo"] + "\n"
                resposta += "tarde - " + requisicao[codigo_monicipio][str(dataf)]["tarde"]["resumo"] + "\n"
                resposta += "noite - " + requisicao[codigo_monicipio][str(dataf)]["noite"]["resumo"] + "\n"
                data = data + timedelta(days = +1)
            for i in range(3):
                dataf = data.strftime("%d/%m/%Y")
                resposta += dataf + " - " + requisicao[codigo_monicipio][str(dataf)]["resumo"] + "\n"
                data = data + timedelta(days = +1)
            bot.sendMessage(chat_id,resposta)

bot = telepot.Bot('6293729431:AAGMg3IvVrP7FC4grj5kwXhlwzUZUQ1f8zI')
bot.message_loop(principal)

while 1:
    time.sleep(5)