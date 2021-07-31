#!user/bin/python

from logging import Formatter, getLogger, StreamHandler, DEBUG
import webex_msg
import argparse
from genie import testbed
from module import test_mod
import sys
sys.path.append('./rest')

parser = argparse.ArgumentParser()
parser.add_argument("device", help="Target Device name")
parser.add_argument("sid", help="Target srv6 sid (fc00:cafe:4:4 etc...)")
args = parser.parse_args()

dev_arg = args.device
sid_arg = args.sid

logger = getLogger("get_srv6_sid...")
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

testbed_path = "./testbed/testbed.yaml"
srv6sid = sid_arg

tb = testbed.load(testbed_path)
devname = tb.devices[dev_arg]
devname.connect()

webex_obj = webex_msg.WebexTeamsMessage()

if test_mod.search_srv6_sid(devname, srv6sid):
    devname.disconnect()
    message = 'Successfully checked !! {0} srv6 sid is {1} !!'.format(
        dev_arg, srv6sid)
    logger.debug(message)
    webex_obj.send_sessage(message)
else:
    devname.disconnect()
    message = 'Failed !! SRv6 sids ({0}) of {1} is unreachable !!'.format(
        srv6sid, dev_arg)
    logger.debug(message)
    webex_obj.send_sessage(message)
    # raise Exception
