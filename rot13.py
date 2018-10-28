alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
inp1=input("Please enter Msg with captal word: ")
shift=13
n = len(inp1)
output = ""
for i in range(n):
    c=inp1[i]
    loc=alphabet.find(c)
    newloc=(loc + shift)%26
    output +=alphabet[newloc]

print ("Encrypted msg is : ",output)