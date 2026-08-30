n = int(input("Enter a number : "))
print("n         = ",n,"->",bin(n))
print("n - 1 =",n-1,"->",bin(n-1))
print("n&(n-1) = ",n&(n-1)),"-> ",bin(n&(n-1))
print("This trick removes the rightmost set bit.")

def power2(num):
    return num > 0 and num & (num-1) == 0
print("POWER OF 2 CHECK ")
numbers = [2,4,6,8,10,12,16,32,64]
for num in numbers:
    print(num,"->",bin(num),"->"is power2(num))