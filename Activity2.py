n = int(input("Enter a number : "))
is_power4 = (n & (n-1)) == 0 and n>0 and n%3 == 1
if is_power4:
    print("Its a power of 4  : ",is_power4,"Binary :  ",bin(n))
else:
    print("Its not a power of 4 : ",is_power4,"Binary ",bin(n))
n = int(input("Enter a number : "))
is_power8 = (n & (n-1)) == 0 and n>0 and n%7 == 1
if is_power8:
    print("Its a power of 8  : ",is_power4,"Binary :  ",bin(n))
else:
    print("Its not a power of 8 : ",is_power4,"Binary ",bin(n))
    