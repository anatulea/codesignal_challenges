'''
An IP address is a numerical label assigned to each device (e.g., computer, printer) participating in a computer network that uses the Internet Protocol for communication. There are two versions of the Internet protocol, and thus two versions of addresses. One of them is the IPv4 address.

Given a string, find out if it satisfies the IPv4 address naming rules.

Example

For inputString = "172.16.254.1", the output should be
isIPv4Address(inputString) = true;

For inputString = "172.316.254.1", the output should be
isIPv4Address(inputString) = false.

316 is not in range [0, 255].

For inputString = ".254.255.0", the output should be
isIPv4Address(inputString) = false.

There is no first number.
'''
def isIPv4Address(inputString):
    ip = inputString.split(".")
    l = len(ip)
    test = []
    if l!=4:
        return False
    for i in range(256):
        test.append(str(i))
    for j in range(l):
        if ip[j] not in test:
            return False
    return True


def isIPv4Address2(s):
    p = s.split('.')
    return len(p) == 4 and all(n.isdigit() and 0 <= int(n) < 256 for n in p)


import ipaddress
def isIPv4Address3(inputString):
    try:
        ipaddress.ip_address(inputString)        
    except:
        return False
    return True