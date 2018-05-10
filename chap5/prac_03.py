#find the smallest value using a for loop

#my_list = [14,654,32,8,5,7,543,432,4324]
#smallest_so_far = my_list[0]

#for the_num in my_list:
    #if smallest_so_far > the_num:
        #smallest_so_far = the_num
#print(smallest_so_far)

smallest = None
for value in [231,4,23,23,4,232,32]:
    if smallest is None :
        smallest = value
    elif value < smallest :
        smallest = value
print(smallest)
