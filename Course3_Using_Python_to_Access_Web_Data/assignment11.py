import re

fname = input('Enter file name: ')
if len(fname) < 1 :
    fname = 'assignment11data.txt'
handle = open(fname)

#Finding Numbers in a Haystack
lst = list()
for line in handle:
    line=line.rstrip()

    num = re.findall('[0-9]+', line)
    if len(num) < 1 :continue

    lst.extend(num)

int_lst = list(map(int,lst))
total = sum(int_lst)
print(total)