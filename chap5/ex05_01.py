
count = 0
tot = 0

while True:
    num = input("Enter a number: ")
    if num == "done":
        print(tot, count, tot / count)
        quit()
    my_list = [num]
    for value in my_list:
        try:
            int(value)
            count = count + 1
            tot = int(value) + tot

        except:
            print("Invalid input")
