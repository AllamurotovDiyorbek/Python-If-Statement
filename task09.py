a=int(input("a= "))
b=int(input("b= "))
c=int(input("c= "))
if a==b==c: 
    print("Teng tomonli")
elif a==b or b==c or a==c:
    print("Teng yonli")
else:
    print("Turli tomonli")