getmsg = input("please enter your msg: ")
i = len(getmsg)-1

reversmsg = ""

while (i >= 0):
    reversmsg += getmsg[i]
    i = i -1

print(reversmsg)    