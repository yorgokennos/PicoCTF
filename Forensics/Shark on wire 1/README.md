Description
We found this packet capture. Recover the flag.

Solution: 
- open the packet capture file with Wireshark, make sure you understand what streams are: https://www.wireshark.org/docs/wsug_html_chunked/ChAdvFollowStreamSection.html
- the packets we're interested in are probably UDP or TCP. By analyzing the UDP stream and looking through each stream
  I was able to find the flag!
  
  
