#!/usr/bin/env python3
import sys
import time
import telepot
from telepot.loop import MessageLoop
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton
import esterno
import webSearching as ws

#pip3 install urllib3==1.24.1


def askForData(msg, functionName):
    chat_id = msg['chat']['id']
    resultAsList = []
    if functionName == "subito":
       resultAsList = ws.subito(True)
    elif functionName == "casa":
       resultAsList = ws.casa(True)
    elif functionName == "immobiliare":
       resultAsList = ws.immobiliare(True)   
    elif functionName == "myhome":
       resultAsList = ws.myhome(True)
    elif functionName == "tecnocasa":
       resultAsList = ws.tecnocasa(True)

    for el in resultAsList:
        bot.sendMessage(chat_id, el[0] )
   


############################################################
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

def on_chat_message(msg):
    first_name = msg['from']['first_name']
    last_name = msg['from']['first_name']
    user_id = msg['from']['id']
    content_type, chat_type, chat_id = telepot.glance(msg)
   # print('Chat Message:', content_type, chat_type, chat_id)
    if content_type == 'text':
       if msg['text'] == '/start':
            keyboard = esterno.getKeyboard()
            ws.insertUser(user_id, first_name, last_name)
            bot.sendMessage(chat_id, 'Use inline keyboard', reply_markup=keyboard)
       elif msg['text'] == 'Subito.it':
             askForData(msg, "subito")
       elif msg['text'] == 'Casa.it':
             askForData(msg, "casa")
       elif msg['text'] == 'Immobiliare.it':
             askForData(msg, "immobiliare")   
       elif msg['text'] == 'Myhome.it': 
             askForData(msg, "myhome") 
       elif msg['text'] == 'Tecnocasa.it':    
             askForData(msg, "tecnocasa") 



def on_callback_query(msg):
    query_id, from_id, query_data = telepot.glance(msg, flavor='callback_query')
   # print('Callback Query:', query_id, from_id, query_data)
    bot.answerCallbackQuery(query_id, text='Got it')




bot = telepot.Bot("1294970700:AAErfuHIs_sKWOQsiz7cgDDouHMy66d1WsQ")
MessageLoop(bot, {'chat': on_chat_message,
                  'callback_query': on_callback_query}).run_as_thread()
print('Listening ...')
starttime = time.time()

while 1:
    print("tick ogni 20 min")
    # Call all the methods as thread
    listSendingMessage_subito = ws.subito()
    listSendingMessage_casa = ws.casa()
    listSendingMessage_immobiliare = ws.immobiliare()
    listSendingMessage_myhome = ws.myhome()
    listSendingMessage_tecnocasa = ws.tecnocasa()

    # reperisco gli utenti
    users_id = ws.viewUsers()

    for id in users_id:
        for el in listSendingMessage_subito:
            bot.sendMessage(id[0] , el)
        for el in listSendingMessage_casa:
            bot.sendMessage(id[0] , el)
        for el in listSendingMessage_immobiliare:
            bot.sendMessage(id[0] , el) 
        for el in listSendingMessage_myhome:
         #   print('ho trovato: ' + el)
            bot.sendMessage(id[0] , el) 
        for el in listSendingMessage_tecnocasa:
            print('ho trovato: ' + el)
            bot.sendMessage(id[0] , el) 

    time.sleep((60.0 * 1) - ((time.time() - starttime) % 60.0))



