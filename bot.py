from flask import Flask, request, abort
from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import (MessageEvent, TextMessage, TextSendMessage)
from Functions import *

app = Flask(__name__)
line_bot_api = LineBotApi(r'your_api')
handler = WebhookHandler(r'your_webhook')

def replyMessage(event,TextMessage):
    line_bot_api.reply_message(event.reply_token,TextSendMessage(text=TextMessage))

def sendMessage(userID,TextMessage):
    line_bot_api.push_message(userID,TextSendMessage(text=TextMessage))

@app.route('/')
def index():
    return 'Hello World!'

@app.route('/webhook',methods=['GET','POST'])
def webhook():
    try:
        signature = request.headers['X-Line-Signature']
        body = request.get_data(as_text=True)
        app.logger.info("Request body: " + body)
        try:
            handler.handle(body, signature)
        except InvalidSignatureError:
            abort(400)
        return 'Connection'
    except:
        return 'Connection'
    

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    row_input = event.message.text
    UID = event.source.user_id
    if row_input in ['stop','Stop']:
        Mi.music.stop()
        Mi.music.unload()
        remove("$music_temp.mp3")
        replyMessage(event,"Music stopped!")
    elif 'valume' in row_input:
        valume = int(row_input[-2:])
        Mi.music.set_volume(valume/10)
    elif row_input == "ql":
        show = "Queue list\n" + "\n".join(Name_Queue)
        sendMessage(UID,show)
    elif Mi.music.get_busy() == 1:
        titleq = MusicQueue(row_input)
        sendMessage(UID,f"Add to queue...\n{titleq}")
    else:
        sendMessage(UID,"Loading music...")
        try:
            title = MusicPlayDirect(row_input)
            sendMessage(UID,f"Playing...\n{title}")
        except:
            sendMessage(UID,"Loading music Failed!")
    
    while Mi.music.get_busy() == 1:
        if Mi.music.get_busy() == 0:
            print("Music was end!")
            PlayQueue()
        else: continue
    
if __name__ == '__main__':
   app.run(debug=True)
