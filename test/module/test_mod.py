#!user/bin/python

import genie.libs.sdk.apis.iosxr.traceroute.get as trace
import genie.libs.sdk.apis.iosxr.utils as utls
import genie.libs.sdk.apis.iosxr.interface.get as get_interface
import genie.libs.sdk.apis.iosxr.interface.configure as conf_interface

def search_srv6_sid(dev, target_sid):
    ipv6route_isis = dev.parse("show route ipv6 isis")
    sid_dic = ipv6route_isis["vrf"]["default"]["address_family"]["ipv6"]["routes"]
    for sid in sid_dic.keys():
        print(sid)
        if target_sid in sid:
            return True
    return False


def search_traceroute_label(dev, target_address, target_label):
    trace_result = trace.get_traceroute_parsed_output(dev, target_address)
    label = trace_result["traceroute"][target_address]["hops"]["1"]["paths"][1]["label_info"]["MPLS"]["label"]
    if label == target_label:
        return True
    else:
        return False


def ping_vrf(dev, target_address, source_address, target_vrf=None):
    ping_result = utls.verify_ping(
        device=dev, address=target_address, source=source_address)
    return ping_result


def get_interface_info(dev, int_list):
    int_info = get_interface.get_interface_information(dev, int_list)
    return int_info


def conf_interface_shut(dev, int_list):
    conf_interface.configure_interfaces_shutdown(dev, int_list)


def conf_interface_noshut(dev, int_list):
    conf_interface.configure_interfaces_unshutdown(dev, int_list)
