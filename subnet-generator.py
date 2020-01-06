#!/usr/bin/env python3

import ipaddress


def generate(network):
    for subnet in network.subnets(new_prefix=28):
        hosts = list(subnet.hosts())
        router = hosts[0]
        range_from = hosts[6]
        range_to = hosts[-1]
        print("subnet {} netmask {} {{".format(subnet.network_address, subnet.netmask))
        print("  pool {")
        print("    failover peer \"failover-partner\";")
        print("    range {} {};".format(range_from, range_to))
        print("  }")
        print("  option routers {};".format(router))
        print("}")
        print()


generate(ipaddress.ip_network('100.65.0.0/21'))
generate(ipaddress.ip_network('100.65.128.0/21'))
