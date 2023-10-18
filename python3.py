a=int(input("entrer un entier"))
b=0
c=""
s=0
for i in range(1,-1):
 if a%i==0:
    b=b+1
    c=c+i
    s=s+i
p=0
for i in range(1,-1):
  if s%i==0:
    b=b+1
    c=c+1
    P=P+1
    if p==a:
      print(p,"et",a,"est amie")
      