#figure out who has sent the greatest number of mail messages.
handle = open('mbox-short.txt')

counts = dict()
for line in handle:
    line = line.rstrip()
    if not line.startswith('From '):continue

    words = line.split()
    mail = words[1]
    counts[mail] = counts.get(mail, 0) + 1

    bw = None
    bc = None
    for w,c in counts.items():
        if bc is None or c>bc:
            bw = w
            bc = c

print(bw,bc)

    
    
    