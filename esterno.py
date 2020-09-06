import telepot
from telepot.loop import MessageLoop
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton



def getKeyboard():

    keyboard = ReplyKeyboardMarkup(
                                keyboard=[
                                    [KeyboardButton(text="Subito.it"), KeyboardButton(text="Casa.it"),KeyboardButton(text="Immobiliare.it"),],
                                    [KeyboardButton(text="Tecnocasa.it"), KeyboardButton(text="Myhome.it")]
                                ]
                            )
    return keyboard       


     
        