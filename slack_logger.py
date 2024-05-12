from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
from slack_sdk import WebClient

import configparser
import logging

# # load the tokens and signatures 
config = config = configparser.ConfigParser()
config.read("bot.ini")

# # configure the tokens and secret signature
app_token = config["KEYS"]["AppToken"]
bot_token = config["KEYS"]["BotToken"]
signing_secret = config["KEYS"]["SlackSignature"]
channel = config["INFO"]["BroadcastChannel"]

# # start the slack interface
app = App(token=bot_token, signing_secret=signing_secret)
client = WebClient(token=bot_token)

class SlackLoggingHandler(logging.Handler):
    def __init__(self) -> None:
        self.sender = LogSender()
        logging.Handler.__init__(self=self)

    def emit(self, record) -> None:
        msg = self.format(record)
        self.sender.writeLog(msg)

class LogSender:
    def __init__(self) -> None:
        pass

    def writeLog(self, msg) -> None:
        client.chat_meMessage(channel=channel, text=msg)

class SlackFilter(logging.Filter):
    def __init__(self) -> None:
        pass

    def filter(self, record: logging.LogRecord) -> bool:
        if "slack" in record.name:
            return False
        else:
            return True