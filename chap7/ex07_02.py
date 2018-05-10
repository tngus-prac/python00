txt = input("Enter the file name: ")
fhand = open(txt)
count = 0
sum = 0.0
for lx in fhand:
    if lx.startswith("X-DSPAM-Confidence:"):
        ipos = lx.find(':')
        value = lx[ipos+1:]
        fvalue = float(value)
        sum = sum + fvalue
        count = count + 1

print("Average spam confidence:", sum / count)
