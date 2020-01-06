# Subnet Generator

A simple generator to create DHCP subnet configurations for use with /etc/dhcpd.conf 

## Requirements

Should support the following ranges in the dedicated space for carrier-grade NAT deployment:

100.65.0.0 to 100.65.8.0
100.65.128.0 to 100.65.137.0

## Template

subnet 100.65.128.176 netmask 255.255.255.240 {
  pool {
    failover peer "failover-partner";
    range 100.65.128.183 100.65.128.190;
  }
  option routers 100.65.128.177;
}

## Dependencies

- python3
- ipaddress
