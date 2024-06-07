#figure out the distribution by hour of the day for each of the messages.
name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

d = dict()
for line in handle:
    line = line.rstrip()
    if not line.startswith('From '):continue

    hpos = line.find(':')
    hour = line[hpos-2 : hpos].strip()
    
    d[hour] = d.get(hour , 0) + 1
    
for k,v in sorted(d.items()):
    print(k,v)
