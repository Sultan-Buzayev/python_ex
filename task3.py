
import re


open_file = open("xyz.txt", "rt")

working_text = open_file.read()

#name

name_protocol = re.findall(r'^L|C|S|R|M|B|D|EX|O|IA|N1|N2|E1|E2|E|i|L1|o|a', working_text)


if name_protocol == 'L':
print("Protocol: local")

elif name_protocol == 'C':
print("Protocol: connected")

elif name_protocol == 'S':
print("Protocol: Static")

elif name_protocol == 'R':
print("Protocol: RIP")

elif name_protocol == 'M':
print("Protocol: Mobile")

elif name_protocol == 'B':
print("Protocol: BGP")

elif name_protocol == 'D':
print("Protocol: EIGRP")

elif name_protocol == 'EX':
print("Protocol: EIGRP external")

elif name_protocol == 'O':
print("Protocol: OSPF")

elif name_protocol == 'IA':
print("Protocol: OSPF inter area")

elif name_protocol == 'N1':
print("Protocol: OSPF nssa type 1")

elif name_protocol == 'N2':
print("Protocol: OSPF nssa type 2")

elif name_protocol == 'E1':
print("Protocol: OSPF type 2")

elif name_protocol == 'E2':
print("Protocol: OSPF type 2")

elif name_protocol == 'E':
print("Protocol: EGP")

elif name_protocol == 'o':
print("Protocol: ODR")

elif name_protocol == 'a':
print("Protocol: application router")

elif name_protocol == 'C':
print("Protocol: ")

elif pattern1 == 'C':
print("Protocol: ")

else:

print ("Invalid input")


#prefex
prefex = re.findall(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', working_text)

#AD/Metric

ad_metric = re.findall(r'\d{1,3}\\d{1,3}', working_text)

#Next-Hop

next_hop = re.findall(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', working_text)

#Last Update

last_update = re.findall(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', working_text)

#Outbound interface

outbound = re.findall('Ethernet\d', working_text)


        print ("Prefix:", prefex)
        print ("AD/Metric: ", ad_metric)
        print ("Next-Hop: ", next_hop)
        print ("Last Update: ", last_update)
        print ("Outbound interface: ", outbound)