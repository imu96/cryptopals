# vector of letter frequencies
#lf = [.0817, .015, .0278, .0425, .127, .0223, .0202,
#    .0609, .0697, .0015, .0077, .0403, .0241, .0675, .0751,
#    .0193, .0010, .0599, .0633, .0906, .0276, .0098, .0236,
#    .0015, .0197, .0007] 
#lf = [ 1000 * x for x in lf]

lf = [81.5, 14.4, 27.6, 37.9, 131.1, 29.2, 19.9, 52.6, 63.5,
        1.3, 4.2, 33.9, 25.4, 71.0, 80.0, 19.8, 1.2, 68.3,
        61.0, 104.7, 24.6, 9.2, 15.4, 1.7, 19.8, .8]

def xor (m,n):
    r = hex(int('1' + m,16) ^ int(n,16))[3:]
    if(r[-1:] == 'L'):
        return r[:-1]
    return r

def text (s):
    for i in range(0, len(s), 2):
        n = int(s[i: i+2], 16)
        if(n > 126 or n < 32):
            return False
    return True

def dist (v):
    d = 0
    for i in xrange(26):
        d += (lf[i] - v[i])**2
    return d

def freq (s, c, d):
    t = s
    ls = lt = len(s) / 2
    n = 0
    while(lt > 0):
        if(t[:2] == c or t[:2] == d):
            n += 1
        t = t[2:]
        lt -= 1
    n *= 1000
    return (n + 0.0) / ls

# l is the list of ascii characters that could appear in the key
def decrypt (s, l):
    l = len(s)
    c = -1
    m = 75000
    for i in l:
        h = hex(i)[2:].zfill(2)
        key = h * (l / 2)
        t = xor(s,key)
        if(text(t)):
            v = make_v(t)
            d = dist(v)
            if(d < m):
                m = d
                c = i
    return c
#            if(d < 30000):
#                print t.decode('hex')
#                print d
#                print i
#                print "\n"

def make_v (s):
    l = range(26)
    for i in xrange(26):
        l[i] = freq(s, hex(i + 65)[2:], hex(i+97)[2:])
    return l 

#s = decrypt("1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736", xrange(256))
