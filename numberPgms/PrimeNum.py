#  title :prime number pgm
#  
num=7

for i in range(2,num):
    if  num%i==0 :
        break

if i==num:
    print(num," is a prime number")
else :
    print(num," is NOT a prime number")


