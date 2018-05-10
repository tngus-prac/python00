txt = input("Enter the file name: ")

if txt == "na na boo boo":
    print("NA NA BOO BOO TO YOU - You have been punk'd!")
    quit()

try:
    fhand = open(txt)
except:
    print("File cannot be opened:", txt)
    quit()

count = 0
for line in fhand:
    count = count + 1
print("There were %s subject lines in %s" % (count, txt))
