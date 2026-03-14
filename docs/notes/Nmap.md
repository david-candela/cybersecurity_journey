
Nmap is an open-source network scanner.

IP range using `-`: If you want to scan all the IP addresses from 192.168.0.1 to 192.168.0.10, you can write `192.168.0.1-10`.
  
IP subnet using `/`: If you want to scan a subnet, you can express it as `192.168.0.1/24`, and this would be equivalent to `192.168.0.0-255`.

You can also specify your target by hostname, for example, `example.thm`.

`-sn`ping scan, aims to discover live hosts without attempting to discover the services running on them

Example: `nmap -sn 192.168.66.0/24`

Scanning ports:
`-sT` tries to complete the TCP three-way handshake with every target TCP port.
`-sS`SYN Scan stealthy because it only executes the first step of the three way handshake.
`-sU` to scan for UDP services.
`-F` is for Fast mode, which scans the 100 most common ports (instead of the default 1000).
`-p[range]` allows to specify a range of ports to scan. For example, `-p10-1024` scans from port 10 to port 1024, while `-p-25` will scan all the ports between 1 and 25. Note that `-p-` scans all the ports and is equivalent to `-p1-65535` and is the best option if you want to be as thorough as possible.

`-O`to enable OS detection.
`-sV`enable service detection.
`-A`OS detection, version scanning, and traceroute.
`-v`verbose option with levels of `-v` `-vv` `-vvv`
`-d`debugging-level option 

Saving the scan:
`-oN <filename>` - Normal output
`-oX <filename>` - XML output
`-oG <filename>` - `grep`-able output (useful for `grep` and `awk`)
`-oA <basename>` - Output in all major formats
