n=int(input("Enter n value"))

rev=0

temp=n
#sameer_5500
while(n>0):
    
    rem=n%10
    
    rev=(rev*10)+rem
    
    n=n//10
    
if temp==rev:
        
    print("Palindrome number")
        
else:
            
    print("It is not a palindrome number")
