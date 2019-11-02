import sys

# Checking octets
# Checking for:
# Looback: 127.0.0.0 - 127.255.255.255
# Multicast: 224.0.0.0 - 239.255.255.255
# Broadcast: 255.255.255.255
# Link-Local: 169.254.0.0 - 169.254.255.255
# Reserved for future use: 240.0.0.0 - 255.255.255.254


def ip_addr_valid(list):
    for ip in list:
        ip = ip.rstrip("\n")  # removes "\n from line"
        octet_list = ip.split('.')
		if (len(octet_list) == 4) and (1 <= int(octet_list[0]) <= 223) and (int(octet_list[0]) != 127) and (int(octet_list[0]) != 169 or int(octet_list[1]) != 254) and ( 0 <= int(octet_list[1]) <= 255 and 0 <= int(octet_list[2]) <= 255 and 0 <= int(octet_list[3]) <= 255):
			continue
		else:
			print('\n* There was an invalid IP address in the file: {} :(\n'.format(ip))
			sys.exit()


a = [ 10.10.10.2, 192.168.1.2]
ip_addr_valid(a)