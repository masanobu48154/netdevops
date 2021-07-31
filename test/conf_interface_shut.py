#!user/bin/python

from logging import Formatter, getLogger, StreamHandler, DEBUG
import webex_msg
import argparse
from genie import testbed
from module import test_mod
import sys
sys.path.append('./rest')

parser = argparse.ArgumentParser()
parser.add_argument("device", help="Device name")
parser.add_argument("interface", help="Shutdown interface number")
args = parser.parse_args()

dev_arg = args.device
int_arg = args.interface
int_list = [int_arg]

logger = getLogger("conf_int_shut..")
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
dev = tb.devices[dev_arg]
dev.connect()

webex_obj = webex_msg.WebexTeamsMessage()

test_mod.conf_interface_shut(dev, int_list)
dev.disconnect()

message = "Successfully shutdown interface {0} of {1} !!".format(int_arg, dev)
logger.debug(message)
webex_obj.send_sessage(message)
