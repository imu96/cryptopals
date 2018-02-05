def xor (m,n):
    r = hex(int(m,16) ^ int(n,16))[2:]
    if(r[-1:] == 'L'):
        return r[:-1]
    return r

print xor("1c0111001f010100061a024b53535009181c", "686974207468652062756c6c277320657965")
