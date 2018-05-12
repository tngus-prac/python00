fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"
fhand = open(fname)
counts = dict()
for line in fhand:
    if line.startswith('From '):
        email = line.split()[1]
        counts[email] = counts.get(email, 0) + 1

lst = list()
for key, val in counts.items():
    newtup = (val, key)
    lst.append(newtup)
lst = sorted(lst, reverse=True)
for (val, key) in lst[:1]:
    print(key, val)
