print("12 & 11 = ", 12 & 11,"Binary = ",bin(12 & 11)[2:])
print("8 & 7 = ", 8 & 7 ,"Binary = ",bin(8 & 7)[2:])
n = int(input("Enter 4 or 6 : "))
if n > 0  and(n&(n-1))==0:
    print("It is power of 2 ",bin(n))
else:
    print("Its not a power of 2 ",bin(n))