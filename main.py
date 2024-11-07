n1=input("Enter the first number:")
n1=float(n1)
n2=input("Enter the second number:")
n2=float(n2)

result=0;

operant= input("Enter the operant (*,/,+,-):")

if operant=="+":
    result=n1+n2;
elif operant=="-":
    result=n1-n2;
elif operant=="*":
    result=n1*n2;
elif operant=="/":
    result=n1/n2;
else:
    result="Invalid Operation";

print(result)