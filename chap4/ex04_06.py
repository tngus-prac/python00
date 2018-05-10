
def computepay(hours, rate):
    #print("In computepay")
    if hours > 40 :
        pay = (hours - 40) * 1.5 * rate + 40 * rate

    else :
        pay = hours * int(rate)
    #print("Returning", pay)
    return pay

sh = input("Enter Hours: ")
sr = input("Enter Rate: ")
fh = float(sh)
fr = float(sr)

xp = computepay(fh, fr)

print("Pay:", xp)
