
#!/usr/bin/python3
#coding: utf-8
import telepot, time
from telepot.namedtuple import ReplyKeyboardMarkup, KeyboardButton
from random import randint

# telepot.api.set_proxy('http://192.168.0.1:3128',(usuário,senha))

opcoes = []


def principal(msg):
    global opcoes
    content_type, chat_type, chat_id = telepot.glance(msg)

    if content_type == "text":
        chat_id = msg["chat"]["id"]
        mensagem = msg["text"]

        if mensagem.upper() == "JOGAR" or mensagem.upper() == "SIM":
            opcoes = [["1","2","3"],["4","5","6"],["7","8","9"]]
            bot.sendMessage(chat_id,"Selecione uma opção:", reply_markup=ReplyKeyboardMarkup(keyboard=opcoes, resize_keyboard = True, one_time_keyboard = True))

        try:
            if int(mensagem) in range(0,10):
                if mensagem == "1": opcoes[0][0] = "X"
                if mensagem == "2": opcoes[0][1] = "X"
            
                if mensagem == "3": opcoes[0][2] = "X"
                if mensagem == "4": opcoes[1][0] = "X"
                if mensagem == "5": opcoes[1][1] = "X"
                if mensagem == "6": opcoes[1][2] = "X"
                if mensagem == "7": opcoes[2][0] = "X"
                if mensagem == "8": opcoes[2][1] = "X"
                if mensagem == "9": opcoes[2][2] = "X"
                l = randint(0,2)
                c = randint(0,2)
                cont = 0
                while opcoes[l][c] == "X" or opcoes[l][c] == "O" and cont < 9:
                    l = randint(0,2)
                    c = randint(0,2)
                    cont = cont + 1
                opcoes[l][c] = "O"
                fim = 0
                # - Usuário ganha
                if opcoes[0][0] == "X" and opcoes[0][1] == "X" and opcoes[0][2] == "X": fim = 1
                if opcoes[1][0] == "X" and opcoes[1][1] == "X" and opcoes[1][2] == "X": fim = 1
                if opcoes[2][0] == "X" and opcoes[2][1] == "X" and opcoes[2][2] == "X": fim = 1
                if opcoes[0][0] == "X" and opcoes[1][0] == "X" and opcoes[2][0] == "X": fim = 1
                if opcoes[0][1] == "X" and opcoes[1][1] == "X" and opcoes[2][1] == "X": fim = 1
                if opcoes[0][2] == "X" and opcoes[1][2] == "X" and opcoes[2][2] == "X": fim = 1
                if opcoes[0][0] == "X" and opcoes[1][1] == "X" and opcoes[2][2] == "X": fim = 1
                if opcoes[0][2] == "X" and opcoes[1][1] == "X" and opcoes[2][0] == "X": fim = 1
                # - Programa ganha
                if opcoes[0][0] == "O" and opcoes[0][1] == "O" and opcoes[0][2] == "O": fim = 2
                if opcoes[1][0] == "O" and opcoes[1][1] == "O" and opcoes[1][2] == "O": fim = 2
                if opcoes[2][0] == "O" and opcoes[2][1] == "O" and opcoes[2][2] == "O": fim = 2
                if opcoes[0][0] == "O" and opcoes[1][0] == "O" and opcoes[2][0] == "O": fim = 2
                if opcoes[0][1] == "O" and opcoes[1][1] == "O" and opcoes[2][1] == "O": fim = 2
                if opcoes[0][2] == "O" and opcoes[1][2] == "O" and opcoes[2][2] == "O": fim = 2
                if opcoes[0][0] == "O" and opcoes[1][1] == "O" and opcoes[2][2] == "O": fim = 2
                if opcoes[0][2] == "O" and opcoes[1][1] == "O" and opcoes[2][0] == "O": fim = 2
                if fim == 0:
                    bot.sendMessage(chat_id,"Selecione uma posição:", reply_markup=ReplyKeyboardMarkup(keyboard=opcoes, resize_keyboard = True, one_time_keyboard = True))
                if fim == 1 or fim == 2:
                    if fim == 1:
                        bot.sendMessage(chat_id,"Parabéns! Você ganhou!")
                        
                    if fim == 2:
                        bot.sendMessage(chat_id,"Legal! Eu ganhei!")
                    jogo = ""
                    for i in range(0,3):
                        for j in range(0,3):
                            jogo = jogo + opcoes[i][j] + "\t"
                        jogo = jogo + "\n"
                    bot.sendMessage(chat_id,jogo)
                    opcoes = [["Sim","Não"]]
                    bot.sendMessage(chat_id,"Jogar novamente?", reply_markup=ReplyKeyboardMarkup(keyboard=opcoes, resize_keyboard = True, one_time_keyboard = True))
        except ValueError:
            pass


bot = telepot.Bot('6293729431:AAGMg3IvVrP7FC4grj5kwXhlwzUZUQ1f8zI')

bot.message_loop(principal)

while 1:
        time.sleep(5)