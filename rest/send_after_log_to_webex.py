#!user/bin/python

from logging import Formatter, getLogger, StreamHandler, DEBUG
import webex_msg
import sys
sys.path.append('./rest')

logger = getLogger("send_log_webex.")
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

message = "Successfully sended logs pulled from nodes after changing !!"

collect_log_path = {
    "./logs/ops_after/routing/": [
        "routing_iosxr_core_01_ops.txt",
        "routing_iosxr_core_02_ops.txt",
        "routing_iosxr_l3edge_01_ops.txt",
        "routing_iosxr_l3edge_02_ops.txt"],
    "./logs/ops_after/isis/": [
        "isis_iosxr_core_01_ops.txt",
        "isis_iosxr_core_02_ops.txt",
        "isis_iosxr_l3edge_01_ops.txt",
        "isis_iosxr_l3edge_02_ops.txt"],
    "./logs/ops_after/bgp/": [
        "bgp_iosxr_core_01_ops.txt",
        "bgp_iosxr_core_02_ops.txt",
        "bgp_iosxr_l3edge_01_ops.txt",
        "bgp_iosxr_l3edge_02_ops.txt"]
}

webex_obj = webex_msg.WebexTeamsMessage()

for path in collect_log_path.keys():
    for log in collect_log_path[path]:
        file_path = path + log
        file_path_list = [file_path]
        webex_obj.send_sessage(msg=message, file_list=file_path_list)
        logger.debug(message)
