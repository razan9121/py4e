# Use words.txt as the file name
fname = input("Enter file name: ")
try:
    fh = open(fname)
except:
    print('Invalid input.')
    quit()

for line in fh:
    line = line.rstrip()
    
rfile = fh.read().upper()
print(rfile)