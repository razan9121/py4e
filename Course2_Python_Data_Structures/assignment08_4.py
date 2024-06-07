# Use the file name romeo.txt as the file name
fname = input('Enter file name: ')
try:
    fh = open(fname)
except:
    print('Invalid file name')
    quit()
    
lst = list()
for line in fh:
    line = line.rstrip()  
    words = line.split()    

    for w in words:
        if w not in lst:
            lst.append(w)

lst.sort()
print(lst)