a=input("enter a  name :")
b= int(input("enter age:"))
c=float(input("height:"))
print("name is ",a)
if(b>=18 and c >=165.50):
   print("he is eligible ")
elif(b<18 and c<165.50):
   print("minor and not eligible")
elif (b>=18  and c<165.50):
    print("not eligible")
else :
    print("wrong entry")
