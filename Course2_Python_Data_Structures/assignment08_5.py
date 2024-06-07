# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
try:
    fh = open(fname)
except:
    print('Invalid input')
    quit()

count = 0
for line in fh:
    line = line.rstrip()

    if not line.startswith('From '):
        continue
    words = line.split()
    sw = words[1]
    
    count = count + 1
    print(sw)
print('There were', count, 'lines in the file with From as the first word')