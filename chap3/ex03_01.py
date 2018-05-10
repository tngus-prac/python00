# Rewrite your pay computation to give the employee 1.5 times the hourly rate for hours worked above 40 hours.

hrs = input("Enter Hours: ")
rate = input("Enter Rate: ")
hrs = int(hrs)
rate = int(rate)
if hrs > 40 :
    pay = (hrs - 40) * 1.5 * rate + 40 * rate

else :
    pay = hrs * int(rate)

print("Pay:", pay)
