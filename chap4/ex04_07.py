def computegrade(score):
    if 0 < score < 1.0:
        if score > 0.9:
            print("A")
        elif score > 0.8:
            print("B")
        elif score > 0.7:
            print("C")
        elif score > 0.6:
            print("D")
        else:
            print("F")

    elif score == 10:
        print("Bad score")

    else:
        print("Error")

ss = input("Enter score: ")

try:
    fs = float(ss)

except:
    print("Bad score")
    quit()

computegrade(fs)
