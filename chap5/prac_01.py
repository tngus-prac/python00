#find largest number using for loop
my_list = [213,546,12,5,675,324,123,876,67,1000]
largest_so_far = my_list[0]

for the_num in my_list:
    if the_num > largest_so_far:
        largest_so_far = the_num

print(largest_so_far)
