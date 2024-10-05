num=7

# range (a,b)==> a to b-1   values only

for i in range(2,num):
    if  num%i==0 :
        break

if i==num:
    print(num," is a prime number")
else :
    print(num," is NOT a prime number")


