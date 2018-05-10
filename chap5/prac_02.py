#find the average in a for loop

count = 0
sum = 0
for value in [453,543,216,543,12,3,5,32]:
    count = count + 1
    sum = sum + value
    print(count, value, sum)

print(sum / count)
