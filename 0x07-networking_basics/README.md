# Networking Basics - Project 0x07

![Project Banner](link_to_your_banner_image)

We're moving to Discord! 🎉
In a few days, we will be leaving Slack in favor of Discord. For more information, [click here](link_to_more_information).

## Table of Contents

- [About](#about)
- [Resources](#resources)
- [Tasks](#tasks)
  - [0. OSI Model](#0-osi-model)
  - [1. Types of Network](#1-types-of-network)
  - [2. MAC and IP Address](#2-mac-and-ip-address)
  - [3. UDP and TCP](#3-udp-and-tcp)
  - [4. TCP and UDP Ports](#4-tcp-and-udp-ports)
  - [5. Is the Host on the Network](#5-is-the-host-on-the-network)
- [Requirements](#requirements)
- [Usage](#usage)
- [Copyright and Plagiarism](#copyright---plagiarism)

## About

This project, part of the ALX DevOps curriculum, focuses on networking basics. It covers fundamental concepts related to networking, including the OSI Model, types of networks, MAC and IP addresses, TCP/UDP, and more.

## Resources

Before you start, it's recommended to read or watch the following resources:

- [OSI model](link_to_osi_model)
- [Different types of network](link_to_types_of_network)
- [LAN network](link_to_lan_network)
- [WAN network](link_to_wan_network)
- [Internet](link_to_internet)
- [MAC address](link_to_mac_address)
- [What is an IP address](link_to_ip_address)
- [Private and public address](link_to_private_public_address)
- [IPv4 and IPv6](link_to_ipv4_ipv6)
- [Localhost](link_to_localhost)
- [TCP and UDP](link_to_tcp_udp)
- [TCP/UDP ports list](link_to_tcp_udp_ports_list)
- [What is ping / ICMP](link_to_ping_icmp)
- [Positional parameters](link_to_positional_parameters)

For additional information and guidance, consider reading the man pages for the following commands:

- `netstat`
- `ping`

## Tasks

### 0. OSI Model

**Task:** Answer the following questions related to the OSI Model.

1. What is the OSI model?
   - [ ] Set of specifications that network hardware manufacturers must respect
   - [x] The OSI model is a conceptual model that characterizes the communication functions of a telecommunication system without regard to their underlying internal structure and technology
   - [ ] The OSI model is a model that characterizes the communication functions of a telecommunication system with a strong regard for their underlying internal structure and technology

2. How is the OSI model organized?
   - [ ] Alphabetically
   - [x] From the lowest to the highest level
   - [ ] Randomly

### 1. Types of Network

**Task:** Answer questions related to different types of networks.

1. What type of network is a computer in a local area connected to?
   - [ ] Internet
   - [ ] WAN
   - [x] LAN

2. What type of network could connect an office in one building to another office in a building a few streets away?
   - [ ] Internet
   - [x] WAN
   - [ ] LAN

3. What network do you use when you browse www.google.com from your smartphone (not connected to Wi-Fi)?
   - [x] Internet
   - [ ] WAN
   - [ ] LAN

### 2. MAC and IP Address

**Task:** Answer questions related to MAC and IP addresses.

1. What is a MAC address?
   - [ ] The name of a network interface
   - [x] The unique identifier of a network interface
   - [ ] A network interface

2. What is an IP address?
   - [ ] Is to devices connected to a network what a postal address is to houses
   - [ ] The unique identifier of a network interface
   - [x] Is a number that network devices use to connect to networks

### 3. UDP and TCP

**Task:** Answer questions related to UDP and TCP.

1. Which statement is correct for the TCP box:
   - [ ] It is a protocol that is transferring data in a slow way but surely
   - [x] It is a protocol that is transferring data in a fast way and might lose data along in the process

2. Which statement is correct for the UDP box:
   - [ ] It is a protocol that is transferring data in a slow way but surely
   - [x] It is a protocol that is transferring data in a fast way and might lose data along in the process

3. Which statement is correct for the TCP worker:
   - [x] Have you received boxes x, y, z?
   - [ ] May I increase the rate at which I am sending you boxes?

### 4. TCP and UDP Ports

**Task:** Write a Bash script that displays listening ports.

- The script should only show listening sockets.
- It should display the PID and name of the program to which each socket belongs.

**Example:**

```bash
sylvain@ubuntu$ sudo ./4-TCP_and_UDP_ports
Active Internet connections (only servers)
Proto Recv-Q Send-Q Local Address           Foreign Address         State       PID/Program name
tcp        0      0 *:sunrpc                *:*                     LISTEN      518/rpcbind
tcp        0      0 *:ssh                   *:*                     LISTEN      1240/sshd
tcp        0      0 *:32938                 *:*                     LISTEN      547/rpc.statd
tcp6       0      0 [::]:sunrpc             [::]:*                  LISTEN      518/rpcbind
tcp6       0      0 [::]:ssh                [::]:*                  LISTEN      1240/sshd
tcp6       0      0 [::]:33737              [::]:*                  LISTEN      547/rpc.statd
udp        0      0 *:sunrpc                *:*                                 518/rpcbind
udp        0     

