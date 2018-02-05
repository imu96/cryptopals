import one_three as ot
import one_five as of

def textToBin (s):
    t = ''
    for c in s:
        o = ord(c)
        h = bin(o)[2:].zfill(8)
        t = t + h
    return t

def ham_dist (x,y):
    d = 0
    a = textToBin(x)
    b = textToBin(y)
    for cs in zip(a,b):
        if(cs[0] != cs[1]):
            d += 1
    return d

def key_size (s):
    ks = 0
    ks_d = 2.0
    for i in range(48):
        k = i + 2
        d = 0
        for j in range(4):
            d += ham_dist(s[j * k: (j + 1) * k])
        d /= 4.0
        n = d / (i + 1.0)
        if(n < ks_d):
            ks_d = n
            ks = k
    return ks

def split (s,n):
    return [s[i: i+n] for i in range(0, len(s), n)]

def transp (s):
    return map(''.join, map(list, zip(*s)))

def dec (ct):
    key = ''
    l = transp(split(ct, key_size(ct)))
    for b in l:
       k = ot.decrypt(b, range(32, 122))
       key += chr(k)
    return of.enc(ct, key)

l = string.ascii_uppercase + string.ascii_lowercase 
l += string.digits + '+/'

def baseToBin (s):
    r = ''
    for c in s:
        if not c == '\n':
            n = l.index(c)
            r += bin(n)[2:].zfill(6)
        if c == '=':
            r += '0' * 6
    return r

def binToHex (s):
    r = ''
    for i in xrange(0, len(s), 8):
        n = l.index(s[i:i+8])
        r += hex(n)[2:].zfill(2)
    return r

filename = '6.txt'
f = open(filename, 'r')
ct = ''
for line in f:
    c += line

print c
print baseToHex(c)
print oo.
#dec(baseToHex(ct))
