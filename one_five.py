import one_three as ot

def textToHex (s):
    t = ''
    for c in s:
        o = ord(c)
        h = hex(o)
        if o > 0xf:
            t = t + h[2:]
        else:
            t = t + '0' + h[2:]
    return t

def enc (p_text, key):
    pt = textToHex(p_text)
    print pt
    k = textToHex(key)
    stream = k * (len(pt) / len(k))
    stream = stream + k[:len(pt) % len(k)]
    return ot.xor(stream, pt)

st1 = "Burning 'em, if you ain't quick and nimble\n"
st2 = "I go crazy when I hear a cymbal"
st = st1 + st2

print enc(st, 'ICE')
