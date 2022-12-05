import os
import sys

from flask import Flask, request, abort, send_file
from dotenv import load_dotenv
from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage

from fsm import TocMachine
from utils import send_text_message

load_dotenv()
USER_ID={}
def createMachine():
    machine = TocMachine(
        states=["user","start", "input_course", "add_course_day","add_course_item","search_course_day","delete_course_day"],
        transitions=[
            {"trigger": "advance","source": "user","dest": "start","conditions": "is_going_to_Start"},
            
            # course
            {"trigger": "advance","source": "start","dest": "input_course","conditions": "is_going_to_course"},
            # add course
            {"trigger": "advance","source": "input_course","dest": "add_course_day","conditions": "is_going_to_add_course_day"},
            {"trigger": "advance","source": "add_course_day","dest": "add_course_item","conditions": "is_going_add_course_item"},
            {"trigger": "advance","source": "add_course_item","dest": "user","conditions": "is_going_to_return"},
            # search course
            {"trigger": "advance","source": "input_course","dest": "search_course_day","conditions": "is_going_to_search_course_day"},
            {"trigger": "advance","source": "search_course_day","dest": "user","conditions": "is_going_to_return"},
            # delete course
            {"trigger": "advance","source": "input_course","dest": "delete_course_day","conditions": "is_going_to_delete_course_day"},
            {"trigger": "advance","source": "delete_course_day","dest": "user","conditions": "is_going_to_return"},

        ],
        initial="user",
        auto_transitions=False
        # show_conditions=True
    )
    return machine

app = Flask(__name__, static_url_path='')


# get channel_secret and channel_access_token from your environment variable
channel_secret = os.getenv("LINE_CHANNEL_SECRET", None)
channel_access_token = os.getenv("LINE_CHANNEL_ACCESS_TOKEN", None)

if channel_secret is None:
    print("Specify LINE_CHANNEL_SECRET as environment variable.")
    sys.exit(1)
if channel_access_token is None:
    print("Specify LINE_CHANNEL_ACCESS_TOKEN as environment variable.")
    sys.exit(1)

line_bot_api = LineBotApi(channel_access_token)
parser = WebhookParser(channel_secret)


@app.route("/callback", methods=["POST"])
def callback():
    signature = request.headers["X-Line-Signature"]
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # parse webhook body
    try:
        events = parser.parse(body, signature)
    except InvalidSignatureError:
        abort(400)

    # if event is MessageEvent and message is TextMessage, then echo text
    for event in events:
        if not isinstance(event, MessageEvent):
            continue
        if not isinstance(event.message, TextMessage):
            continue

        line_bot_api.reply_message(
            event.reply_token, TextSendMessage(text=event.message.text)
        )

    return "OK"


@app.route("/webhook", methods=["POST"])
def webhook_handler():
    signature = request.headers["X-Line-Signature"]
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info(f"Request body: {body}")

    # parse webhook body
    try:
        events = parser.parse(body, signature)
    except InvalidSignatureError:
        abort(400)

    # if event is MessageEvent and message is TextMessage, then echo text
    for event in events:
        if not isinstance(event, MessageEvent):
            continue
        if not isinstance(event.message, TextMessage):
            continue
        if not isinstance(event.message.text, str):
            continue
        if event.source.user_id not in USER_ID:
            print(f"Create ! {event.source.user_id}")
            USER_ID[event.source.user_id] = createMachine()
                
        response = USER_ID[event.source.user_id].advance(event)
        if response == False:
            send_text_message(event.reply_token, "Not Entering any State")

    return "OK"


@app.route("/show-fsm", methods=["GET"])
def show_fsm():
    machine.get_graph().draw("fsm.png", prog="dot", format="png")
    return send_file("fsm.png", mimetype="image/png")

if __name__ == "__main__":
    port = os.environ.get("PORT", 8000)
    app.run(host="0.0.0.0", port=port, debug=True)
