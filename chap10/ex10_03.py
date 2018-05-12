fname = input("Enter a file name: ")
if len(fname) < 1 : fname = 'clown.txt'
fhand = open(fname)
counts = dict()
for line in fhand:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1
lst = list()
for word, count in counts.items():
    newt = count, word
    lst.append(newt)
lst = sorted(lst, reverse=True)
for count, word in lst[:5]:
    print(word, count)
