
x=int(input("Enter the number:"))
if x<0:
    print(False)
if x%10==0 and x!=0:
    print(False)
rev=0
while x>rev:
    rev=rev*10+(x%10)
    x//=10
print(x==rev or x==rev//10)
        