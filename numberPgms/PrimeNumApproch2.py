#  title :prime number pgm
#  
num=53
print((int)(num/2)+1)
for i in range(2,(int)(num/2)+1):
    if  num%i==0 :
        break

print(i)
if i==((int)(num/2)):
    print(num," is a prime number")
else :
    print(num," is NOT a prime number")


