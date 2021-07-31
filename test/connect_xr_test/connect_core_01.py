#!user/bin/python

from logging import Formatter, getLogger, StreamHandler, DEBUG
import time
from genie import testbed
import sys
sys.path.append('./rest')
import webex_msg

logger = getLogger("con_2_core_01..")
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

dev = "core_01"


def check_connection(target):
    tb = testbed.load("./testbed/testbed.yaml")
    dev = tb.devices[target]
    dev.connect()
    dev.disconnect()


webex_obj = webex_msg.WebexTeamsMessage()

for i in range(51):
    time.sleep(10)
    try:
        check_connection(dev)
        webex_obj.send_sessage("Successfully connected to {0} !!".format(dev))
        logger.debug("Successfully connected to {0} !!".format(dev))
        break
    except:
        if i == 50:
            webex_obj.send_sessage("Failed connectrion to {0} !!".format(dev))
            logger.debug("Failed connectrion to {0} !!".format(dev))
            raise Exception
        pass
