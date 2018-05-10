str = 'X-DSPAM-Confidence: 0.8475 '
copos = str.find(':')
#print(copos)
sf = str[copos+2:]
#print(sf)
ff = float(sf)
print(ff)
