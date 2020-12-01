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

There is no first number.'''
def isIPv4Address(inputString):

    nums = inputString.split('.')
    print(nums)
    if len(nums) != 4:
        return False
    if '' in nums:
        return False
    for i in nums:
        try:
            n= int(i)
        except ValueError:
            return False
        if len(i)>1 and int(i[0]) == 0:
            return False
        if  int(i) > 255:
            return False
    
    return True

string = "0.254.255.0"
inputString= "0..1.0"
print(isIPv4Address(string))
print(isIPv4Address(inputString))