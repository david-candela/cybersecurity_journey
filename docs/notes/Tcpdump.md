Packet analyzer for Linux/Unix systems, used to capture, filter, and inspect network traffic in real-time or save it to a file (`.pcap`)

Basic commands:

`-i INTERFACE`which network interface to listen. We can choose `-i any`or specify `-i eth0` 
`ip address show` (or `ip a s`) list the available network interfaces
`-w FILE`saves a file of the packets we captured
`-r FILE`to read the file of captured packets
`-c COUNT`limits the number of captured packets
`-n`this argument prevents DNS lookups or `-nn`to prevent both DNS and port numbers resolved
`-v` will print the time to live, identification, total length and options in an IP packet

Examples: 
`tcpdump -i eth0 -c 50 -v` 
`tcpdump -i wlo1 -w data.pcap` 

Filtering:

`host IP` or `host HOSTNAME` to limit the captured packets to a specific host
`src host IP` or `src host HOSTNAME` to limit packets from a particular source IP address
`dst host IP` or `dst host HOSTNAME` to limit packets sent to a specific destination
`port PORT_NUMBER`to limit captured packets to that port `port 53`captures DNS traffic
`src port PORT_NUMBER` and `dst port PORT_NUMBER` can also be used
`ip`, `ip6`, `udp`, `tcp`, and `icmp` to limit captures by protocol 

we can use logical operators as `and`, `or`, `not`

Example:
`tcpdump -i eth0 host example.com and tcp port 443 -w https.pcap` 

More filters:

`greater LENGTH`: Filters packets that have a length greater than or equal to the specified length
`less LENGTH`: Filters packets that have a length less than or equal to the specified length

Tcpdump allows you to refer to the contents of any byte in the header using the following syntax `proto[expr:size]`, where:

- `proto` refers to the protocol. For example, `arp`, `ether`, `icmp`, `ip`, `ip6`, `tcp`, and `udp` refer to ARP, Ethernet, ICMP, IPv4, IPv6, TCP, and UDP respectively.
- `expr` indicates the byte offset, where `0` refers to the first byte.
- `size` indicates the number of bytes that interest us, which can be one, two, or four. It is optional and is one by default.

Even more arguments:

`-q`: Quick output; print brief packet information
`-e`: Print the link-level header (MAC addresses)
 `-A`: Show packet data in ASCII
`-xx`: Show packet data in hexadecimal format, referred to as hex
`-X`: Show packet headers and data in hex and ASCII