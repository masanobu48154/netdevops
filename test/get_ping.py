#!user/bin/python

from logging import Formatter, getLogger, StreamHandler, DEBUG
import argparse
from genie import testbed
from module import test_mod
import sys
sys.path.append('./rest')
import webex_msg

parser = argparse.ArgumentParser()
parser.add_argument("device", help="Device name")
parser.add_argument("source", help="Source address")
parser.add_argument("destination", help="Destination address")
args = parser.parse_args()

dev_args = args.device
source_addr = args.source
target_addr = args.destination


logger = getLogger("get_ping.......")
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

tb_path = "./testbed/testbed.yaml"

tb = testbed.load(tb_path)
devname = tb.devices[dev_args]
devname.connect()

webex_obj = webex_msg.WebexTeamsMessage()

if test_mod.ping_vrf(dev=devname, target_address=target_addr, source_address=source_addr):
    devname.disconnect()
    message = "Successfully pinged to {0} {1} from {2} !!".format(
        devname, target_addr, source_addr)
    logger.debug(message)
    webex_obj.send_sessage(message)
else:
    devname.disconnect()
    message = "Failed !! {0} is unreachable from {1} {2} !!".format(
        target_addr, devname, source_addr)
    logger.debug(message)
    webex_obj.send_sessage(message)
    # raise Exception
