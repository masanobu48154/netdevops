#!user/bin/python

import ciscosparkapi
import env
from logging import Formatter, getLogger, StreamHandler, DEBUG

logger = getLogger("webex_module...")
logger.setLevel(DEBUG)
handler = StreamHandler()
handler.setLevel(DEBUG)
fmt = Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    "%Y-%m-%dT%H:%M:%S"
)
handler.setFormatter(fmt)
logger.addHandler(handler)
logger.propagate = False

env_object = env.MyEnv()
webex_token = env_object.my_env["webex_token"]
webex_room = env_object.my_env["webex_room"]


class WebexTeamsMessage():

    def send_sessage(self, msg, file_list=None):
        webex = ciscosparkapi.CiscoSparkAPI(access_token=webex_token)
        webex.messages.create(
            webex_room,
            text=msg,
            files=file_list)
        logger.debug("Successfully meesage sended !!")


if __name__ == '__main__':
    webex_obj = WebexTeamsMessage()
    webex_obj.send_sessage("test")
