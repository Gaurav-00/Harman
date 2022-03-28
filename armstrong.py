#Python program to check if the number is an Armstrong number or not
n=int(input("enter a number-:"))
temp=n
while temp>0:
    {
        digit = temp % 10
        rev += digit**3
        temp //= 10
    }
if(n==rev):
    print(n" is armstrong")
else:
    print(n" is not armstrong")