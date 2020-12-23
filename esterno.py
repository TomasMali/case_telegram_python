import telepot
from telepot.loop import MessageLoop
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton
import sqlLite as sql


def getKeyboard(id):
 
 # se aministratore
    if sql.getUser(id)[0][4] == 1:
       keyboard = ReplyKeyboardMarkup(
                                keyboard=[
                                    [KeyboardButton(text="Autisti"), KeyboardButton(text="Documenti_oggi")]
                                ]
                            )
       return keyboard  
    else:
        keyboard = ReplyKeyboardMarkup(
                                keyboard=[
                                    [KeyboardButton(text="Consegne di oggi")]
                                ]
                            )
        return keyboard  



     


     
        