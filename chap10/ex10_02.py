fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"
fhand = open(fname)
counts = dict()
for line in fhand:
    if line.startswith('From '):
        time = line.split()[-2]
        hour = time.split(':')[0]
        counts[hour] = counts.get(hour, 0) + 1

hour = int(hour)
lst = sorted(counts.items())

for hour, count in lst:
    print(hour, count)
