# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
try:
    fh = open(fname)
except:
    print('Invalid input')

count = 0
total = 0
for line in fh:
    if not line.startswith('X-DSPAM-Confidence:'):
        continue
    fpos = line.find(':')
    fval = float(line[fpos+2:].strip())
    count = count + 1
    total = total + fval
    
avg = total/count
print('Average spam confidence:' , avg)