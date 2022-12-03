import os

from linebot import LineBotApi, WebhookParser
from linebot.models import MessageEvent, TextMessage, TextSendMessage,TemplateSendMessage, ImageCarouselColumn, ImageCarouselTemplate, URITemplateAction, ButtonsTemplate, MessageTemplateAction, ImageSendMessage,FlexSendMessage


channel_access_token = os.getenv("LINE_CHANNEL_ACCESS_TOKEN", None)


def send_text_message(reply_token, text):
    line_bot_api = LineBotApi(channel_access_token)
    line_bot_api.reply_message(reply_token, TextSendMessage(text=text))

    return "OK"


"""
def send_image_url(id, img_url):
    pass
"""
# def send_button_message(reply_token, text, buttons,title):
#     line_bot_api = LineBotApi(channel_access_token)
#     message = TemplateSendMessage(
#         alt_text = 'button template',
#         template = ButtonsTemplate(
#             title = title, 
#             text = text,
#             actions = buttons
#         )
#     )
#     line_bot_api = LineBotApi(reply_token, message)
#     return "OK"

