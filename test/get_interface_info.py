#!user/bin/python

from logging import Formatter, getLogger, StreamHandler, DEBUG
import webex_msg
import argparse
import json
from genie import testbed
from module import test_mod
import sys
sys.path.append('./rest')

parser = argparse.ArgumentParser()
parser.add_argument("device", help="Device name")
parser.add_argument("interface", help="Interface name")
args = parser.parse_args()

dev_arg = args.device
int_arg = args.interface
int_list = [int_arg]

logger = getLogger("get_int_info...")
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

result = test_mod.get_interface_info(dev, int_list)
dev.disconnect()
result_json = json.dumps(result)

file_path = "./logs/send_msg/int_info_{0}_{1}.json".format(
    int_arg.replace("/", "_"), dev_arg)

with open(file_path, mode="w") as f:
    f.write(result_json)

message = "Successfully got interface {0} info of {1} !!".format(
    dev_arg, int_arg)
file_path_list = [file_path]
logger.debug(message)
webex_obj.send_sessage(msg=message, file_list=file_path_list)
