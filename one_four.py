import onethree as ot

filename = '4.txt'
ct = open(filename, 'r')
for line in ct:
    s = line[:-3]
    pt = ot.decrypt(s, xrange(256))
    if pt is not None:
        print pt
