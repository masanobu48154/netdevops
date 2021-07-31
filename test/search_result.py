#!user/bin/python

from logging import Formatter, getLogger, StreamHandler, DEBUG

logger = getLogger("search_diff....1")
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


def check_routing():
    with open('./logs/ops_after/routing/diff_result.log') as temp_f:
        datafile = temp_f.readlines()
    for line in datafile:
        if 'found' in line:
            return False
    return True


def check_bgp():
    with open('./logs/ops_after/bgp/diff_result.log') as temp_f:
        datafile = temp_f.readlines()
    for line in datafile:
        if 'found' in line:
            return False
    return True


def check_isis():
    with open('./logs/ops_after/isis/diff_result.log') as temp_f:
        datafile = temp_f.readlines()
    for line in datafile:
        if 'found' in line:
            return False
    return True


if check_routing():
    logger.debug('Routing is Identical !!')
else:
    # raise Exception
    logger.debug('Routing is Differenct !!')

if check_bgp():
    logger.debug('BGP is Identical !!')
else:
    # raise Exception
    logger.debug('BGP is Differenct !!')

if check_isis():
    logger.debug('ISIS is Identical !!')
else:
    # raise Exception
    logger.debug('ISIS is Differenct !!')
