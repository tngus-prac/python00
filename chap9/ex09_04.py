fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"
fhand = open(fname)
counts = dict()
for line in fhand:
    if line.startswith('From '):
        email = line.split()[1]
        counts[email] = counts.get(email, 0) + 1


bigcount = None
bigword = None
for word, count in counts.items():
    if bigcount is None or bigcount < count:
        bigcount = count
        bigword = word

print(bigword, bigcount)
