
fname = input("Enter a file name: ")
fhand = open(fname)
counts = dict()
for line in fhand:
    if line.startswith('From'):
        if not '@' in line : continue
        str = line.split('@')
        words = str[1].split()
    for word in words:
        domain = words[0]
        counts[domain] = counts.get(domain, 0) + 1
print(counts)
