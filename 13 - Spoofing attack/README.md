## 13 - Spoofing attack
### Flag
F2A29020EF3132E01DD61DF97FD33EC8D7FCD1388CC9601E7DB691D17D4D6188

### Reproduce
We examinated the source code of this page '/?page=b7e44c7a40c5f80139f0a50f3650fb2bd8d00b0d24667c4c2ca32c88e13b758f' which we will call the 'albatroz' page. One comment stood out namely 'You must come from : "https://www.nsa.gov/".'.<br>
In HTTP request headers we changed the 'Referer' header to 'https://www.nsa.gov/' with curl like this `curl -s -H 'Referer: https://www.nsa.gov/' 'http://172.20.10.4/?page=b7e44c7a40c5f80139f0a50f3650fb2bd8d00b0d24667c4c2ca32c88e13b758f'`, which gave us a new page source code with the comment 'FIRST STEP DONE' and another one 'use this browser : "ft_bornToSec". It will help you a lot.'.<br>
Based on the last comment we changed the HTTP request header 'User-Agent' to 'ft_bornToSec' using curl like this 
`curl -s -H 'User-Agent: ft_bornToSec' -H 'Referer: https://www.nsa.gov/' 'http://192.168.1.116/?page=b7e44c7a40c5f80139f0a50f3650fb2bd8d00b0d24667c4c2ca32c88e13b758f' | grep -i 'flag'`, which successfully gave us the flag.

### Understand
This is a spoofing attack because we disguise ourselves, through HTTP header manipulation, as a trusted entity to get what we want as a hacker at the detriment of the victim.<br>
We make the server believe we come from a certain IP address and use a specific browser while we do not.

The danger here lies in the server changing our permissions thus potentially giving unauthorized access to malicious hackers by believing we are someone else.<br>
With a fake source address, hackers can appear like a trusted device on your network, then request sensitive information that your device will freely give away.<br>
IP Spoofing could also be a way for attackers to hide their IP address instead of using a VPN.<br>
Botnet attacks are used to flood websites with DDoS attacks, those botnets usually hide their IP address by spoofing.<br>
Using this IP spoofing method, man-in-the-middle attackers can intercept communication between two devices in order to quietly alter or steal IP packets.

To avoid this breach the server should not blindly trust incoming HTTP headers. Firewalls (A firewall is a tool designed to intercept and assess incoming and outgoing packets) can also help monitor suspicious activity by using a packet filter that inspects IP packet headers and who can detect fake source IP addresses.
