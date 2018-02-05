import string

b64 = string.ascii_uppercase + string.ascii_lowercase 
b64 = b64 + string.digits + '+/'

# converts hex string to bin string WITHOUT the '0b' prepended
def hexToBin (s):
    t = ''
    while (len(s) > 0):
        n = int(s[0], 16)
        w = bin(n)[2:] 
        w = '000'[:4 - len(w)] + w
        t = t + w
        s = s[1:]
    return t

def binTo64 (s):
    t = s
    n = len(s) % 6
    if n != 0:
        for i in xrange(6 - n):
            t = t + '0'
    ret_str = ''
    while(len(t) > 0):
        bin_str = t[:6]
        t = t[6:]
        b = int(bin_str, 2)
        ret_str = ret_str + b64[b]
    return ret_str

def hexTo64 (s):
    return binTo64( hexToBin (s))

s = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
print hexTo64(s)
