import telepot
from telepot.loop import MessageLoop
import google.generativeai as genai
genai.configure(api_key="AIzaSyCYsUgB5Vg0vZiT4o5fC_lyGdW8XlQbcRk")
model = genai.GenerativeModel('gemini-pro')

def handle(msg):
    chat_id = msg['chat']['id']
    text = msg['text']
    response = model.generate_content(text)
    telepot.bot.sendMessage(chat_id, response.text)

telepot.bot = telepot.Bot('6415112556:AAF2NrAxUmXmtwIhP8wTt5yTnCpqLpIRdjg')
MessageLoop(telepot.bot, handle).run_forever()
print('Listening ...')
