fname = input("Enter a file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"
fhand = open(fname)
counts = dict()
for line in fhand:
    if line.startswith('From '):
        dayw = line.split()[2]
        counts[dayw] = counts.get(dayw, 0) + 1

print(counts)
