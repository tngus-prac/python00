txt = input("Enter a file name: ")
fhand = open(txt)
for lx in fhand:
    ly = lx.rstrip()
    print(ly.upper())
