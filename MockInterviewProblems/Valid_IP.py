'''
Validate IP Address
Validate an IP address (IPv4). An address is valid if and only if it is in the form "X.X.X.X", where each X is a number from 0 to 255.

For example, "12.34.5.6", "0.23.25.0", and "255.255.255.255" are valid IP addresses, while "12.34.56.oops", "1.2.3.4.5", and "123.235.153.425" are invalid IP addresses.

Examples:


ip = '192.168.0.1'
output: true

ip = '0.0.0.0'
output: true

ip = '123.24.59.99'
output: true

ip = '192.168.123.456'
output: false
'''

def validateIP(ip: str) -> bool:
    ip_list = ip.split('.')

    if len(ip_list) != 4:
        return False
        
    for ch in ip_list:
        if not ch.isdigit():
            return False
        # check for leading 0
        if len(ch) >= 2 and ch[0] == '0':
            return False
        
        num = int(ch)
        if num > 255 or num < 0:
            return False

    return True

# debug your code below
print(validateIP('192.168.0.1'))




# or here is with helper func
def validateIP(ip: str) -> bool:
    ip_list = ip.split('.')

    if len(ip_list) != 4:
        return False


    # Helper 
    def check_num(num):
        if not num.isdigit():
            return False
        # check for leading 0
        if len(num) > 1 and num[0] == '0':
            return False
        numm = int(num)
        if numm > 255 or numm < 0:
            return False
        return True


    for ch in ip_list:
        if not check_num(ch):
            return False
    return True
