#!user/bin/python

import ciscosparkapi
import env
from logging import Formatter, getLogger, StreamHandler, DEBUG


logger = getLogger("cml2_start_demo")
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

webex = ciscosparkapi.CiscoSparkAPI(access_token=webex_token)
webex.messages.create(
    webex_room,
    text="Successfully Cml started !!"
)

logger.debug("Successfully Cml started !!")
