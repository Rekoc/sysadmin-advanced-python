from scapy.all import *


def main():
   result = sniff(iface="wlo1")
   result.summary()
   # Ether / IP / TCP 192.168.1.189:46802 > 23.51.103.163:https A
   # Ether / IP / TCP 192.168.1.189:46222 > 199.232.170.49:https A
   # Ether / IP / TCP 199.232.170.49:https > 192.168.1.189:46222 A
   # Ether / IP / TCP 23.51.103.163:https > 192.168.1.189:46802 A
   # Ether / IPv6 / TCP 2a01:e0a:4e1:e070:88a5:ceb5:394e:2dc1:58624 > 2606:4700:90:0:6995:5424:4b9b:3a3d:https A
   # ...

   print(result[2])
   # <Ether  dst=f0:9e:4a:8a:93:c3 src=20:66:cf:18:e0:10 type=IPv4 |<IP  version=4 ihl=5 tos=0x0 len=52 id=7402 flags=DF frag=0 ttl=59 proto=tcp chksum=0xee5a src=199.232.170.49 dst=192.168.1.189 |<TCP  sport=https dport=46222 seq=2435580336 ack=1630719328 dataofs=8 reserved=0 flags=A window=312 chksum=0xdaf urgptr=0 options=[('NOP', None), ('NOP', None), ('Timestamp', (1440811652, 1492451907))] |>>>

   for packet in result:
      if IP in packet:
         print(f"{packet.getlayer(IP).src} --> {packet.getlayer(IP).dst}")


   # Output
   # 192.168.1.189 --> 23.51.103.163
   # 192.168.1.189 --> 199.232.170.49
   # 199.232.170.49 --> 192.168.1.189
   # 23.51.103.163 --> 192.168.1.189
   # 192.168.1.189 --> 46.105.50.201
   # 46.105.50.201 --> 192.168.1.189
   # 192.168.1.189 --> 46.105.50.201
   # 46.105.50.201 --> 192.168.1.189
   # 46.105.50.201 --> 192.168.1.189
   # 192.168.1.189 --> 46.105.50.201
   # 192.168.1.189 --> 23.51.103.163
   # 23.51.103.163 --> 192.168.1.189
   # 18.164.52.34 --> 192.168.1.189
   # 18.164.52.34 --> 192.168.1.189
   # 192.168.1.189 --> 18.164.52.34
   # 18.164.52.34 --> 192.168.1.189


   f = rdpcap("./statics/test.pcap")
   # <test.pcap: TCP:14 UDP:6 ICMP:0 Other:5>

   for packet in f:
      print(packet)

   # Output
   # Ether / IP / TCP 162.159.134.234:https > 192.168.1.189:39094 PA / Raw
   # Ether / IP / TCP 192.168.1.189:39094 > 162.159.134.234:https A
   # Ether / IPv6 / TCP 2a01:e0a:4e1:e070:8064:f658:3367:254d:60860 > 2606:4700:90:0:6995:5424:4b9b:3a3d:https A
   # Ether / IPv6 / TCP 2606:4700:90:0:6995:5424:4b9b:3a3d:https > 2a01:e0a:4e1:e070:8064:f658:3367:254d:60860 A
   # Ether / IP / TCP 162.159.134.234:https > 192.168.1.189:39094 PA / Raw
   # ...


   result = sniff(iface="wlo1", filter="tcp")

   t = AsyncSniffer(iface="enp0s3", count=200)
   t.start()
   t.join()


if __name__ == '__main__':
    main()