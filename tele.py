#!/usr/bin/env python3
import sys
import time
import telepot
import os
from telepot.loop import MessageLoop
import esterno
import webSearching as ws
import sqlLite as sql
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton

#pip3 install urllib3==1.24.1




  #  for el in resultAsList:
  #      bot.sendMessage(chat_id, el[0] )
   


############################################################
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

def on_chat_message(msg):
    first_name = msg['from']['first_name']
    last_name = msg['from']['last_name']
    user_id = msg['from']['id']
    content_type, chat_type, chat_id = telepot.glance(msg)
   # print('Chat Message:', content_type, chat_type, chat_id)
    print(content_type)
    if content_type == 'text':
       if msg['text'] == '/start':
            sql.insertUsers(user_id, first_name, last_name)
            keyboard = esterno.getKeyboard(user_id)
            # se pending
            if sql.getUser(chat_id)[0][3] == 1:
               print(sql.getUser(chat_id)[0])
               bot.sendMessage(chat_id, 'Registrazione effettuata correttamente \n In attessa che un utente admin accetti la vostra richiesta!')
               
               print(sql.getAdminUsers())
               print(sql.getPendingUsers())
            else:
               bot.sendMessage(chat_id, 'Usa la tastiera sotto', reply_markup=keyboard)   

       elif msg['text'] == 'Autisti':
             print(sql.getUser(chat_id)[0][0])
             bot.sendMessage(chat_id, 'Autisti' )
       elif msg['text'] == '/setmeadmin':
             sql.setAdmin(chat_id)
             keyboard = esterno.getKeyboard(user_id)
             bot.sendMessage(chat_id, 'Adesso sei admin', reply_markup=keyboard)  
       elif msg['text'] == 'Documenti_oggi': 
             bot.sendMessage(chat_id, 'Documenti_oggi' )
       elif msg['text'] == 'Consegne di oggi':    
             bot.sendMessage(chat_id, 'Sto cercando le consegne di oggi...' ) 
             arr = os.listdir('das')
             print(arr)
             pdf_list_keyboard = []
             for li in arr:
               pdf_list_keyboard.append([InlineKeyboardButton(text=li, callback_data=li)])
               print(li)
             keyboard = InlineKeyboardMarkup(inline_keyboard= pdf_list_keyboard)            
             bot.sendMessage(chat_id, 'Lista dei pdf', reply_markup=keyboard)
       else:
             bot.sendMessage(chat_id, 'Commando non riconosciuto! Premere /start per iniziare.') 

def on_callback_query(msg):
    query_id, from_id, query_data = telepot.glance(msg, flavor='callback_query')
   # print('Callback Query:', query_id, from_id, query_data)
    bot.answerCallbackQuery(query_id, text='Got it')
    file="das/" + query_data
    bot.sendDocument(chat_id=from_id, document=open(file, 'rb')) 
    print(query_data)




bot = telepot.Bot("1471780969:AAFA4sWIn01T_mohDhRZGKn2rI7e6Ywh7A4")
MessageLoop(bot, {'chat': on_chat_message,
                  'callback_query': on_callback_query}).run_as_thread()
print('Listening ...')
starttime = time.time()

while 1:
    print("tick ogni 20 min")



    time.sleep(10)
    #time.sleep((60.0 * 1) - ((time.time() - starttime) % 60.0))



