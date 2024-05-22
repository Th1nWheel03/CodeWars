from struct import unpack
from socket import inet_aton

def ip_to_int32(ip):
    return unpack("!L", inet_aton(ip))[0]

print(ip_to_int32("128.114.17.104"))