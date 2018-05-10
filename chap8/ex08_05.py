#print("python fromcount.py")
fname = input("Enter a file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"
fh = open(fname)
count = 0
for line in fh:
    if line.startswith('From:'):
        continue
    if line.startswith('From'):
        count += 1
        line = line.split()
        print(line[1])

print("There were %d lines in the file with From as the first word" % count)
