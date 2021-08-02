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
parser.add_argument("target_address", help="Target address(10.0.0.4 etc...)")
parser.add_argument("target_label", help="Target label(16004 etc...)")

args = parser.parse_args()

dev_arg = args.device
addr_arg = args.target_address
label_arg = args.target_label

logger = getLogger("get_sr_mpls_sid")
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
target_address = addr_arg
target_label = label_arg

tb = testbed.load(tb_path)
devname = tb.devices[dev_arg]
devname.connect()

webex_obj = webex_msg.WebexTeamsMessage()

try:
    test_mod.search_traceroute_label(devname, target_address, target_label)
    devname.disconnect()
    message = "Successfully checked !! {0} labal is {1}.".format(
        target_address, target_label)
    logger.debug(message)
    webex_obj.send_sessage(message)
except:
    devname.disconnect()
    message = "Failed !! Label of SR-MPLS is unassigned !!"
    logger.debug(message)
    webex_obj.send_sessage(message)
    # raise Exception
