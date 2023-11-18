
#SI SE ROMPE, TUTORIAL: https://www.youtube.com/watch?v=ps1yeWwd6iA
from telegram import CHAT_ID, TELE_BOT

def sendTelegram(message):
    import requests
    chatId = CHAT_ID
    teleBot = TELE_BOT
    url = 'https://api.telegram.org/'+teleBot+'/sendMessage?chat_id='+chatId+'&text="{}"'.format(message)
    requests.get(url)
    return

