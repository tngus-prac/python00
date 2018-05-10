numlist = list()
while True:
    num = input("Enter a number: ")
    if num == "done" : break
    num = float(num)
    numlist.append(num)

max = max(numlist)
min = min(numlist)

print("Maximum:", max)
print("Minimum:", min)
