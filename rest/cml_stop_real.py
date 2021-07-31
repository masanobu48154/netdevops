#!user/bin/python

import apple
import env
import ciscosparkapi
from logging import Formatter, getLogger, StreamHandler, DEBUG


logger = getLogger("cml2_stop_real.")
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
host = env_object.my_env["cml2_0"]
webex_token = env_object.my_env["webex_token"]
webex_room = env_object.my_env["webex_room"]

ob = apple.Cml2(host)
ob.delete_labs()

webex = ciscosparkapi.CiscoSparkAPI(access_token=webex_token)
webex.messages.create(
    webex_room,
    text="Successfully Cml stoped !!"
)

logger.debug("Successfully Cml stopde!!")
