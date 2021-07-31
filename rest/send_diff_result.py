#!user/bin/python

from logging import Formatter, getLogger, StreamHandler, DEBUG, WARNING
import webex_msg
import env
import sys
sys.path.append('./rest')


logger = getLogger("send_diff_check")
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

message = "Successfully sended diff logs ({0})!!"

collect_log_path = {
    "./logs/ops_after/routing/": ["diff_result.log"],
    "./logs/ops_after/isis/": ["diff_result.log"],
    "./logs/ops_after/bgp/": ["diff_result.log"]
}

webex_obj = webex_msg.WebexTeamsMessage()

for path in collect_log_path.keys():
    for log in collect_log_path[path]:
        file_path = path + log
        file_path_list = [file_path]
        webex_obj.send_sessage(msg=message.format(path),
                               file_list=file_path_list)
        logger.debug(message.format(path))
