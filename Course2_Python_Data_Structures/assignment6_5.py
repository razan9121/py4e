text = "X-DSPAM-Confidence:    0.8475"
numpos = text.find('0')
estr = text[numpos:]
fnum = float(estr)
print(fnum)