from linebot import LineBotApi
from linebot.models import TextSendMessage
from linebot.exceptions import LineBotApiError

def line_text(name):
    line_bot_api = LineBotApi('your line bot API')
    try:
        line_bot_api.broadcast(TextSendMessage(text= (name + ' is detected')))
    except LineBotApiError as e:
        # error handle
        print("Error: Line")
        ...

