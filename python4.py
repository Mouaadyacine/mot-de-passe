a=input("entrer le mot de passe")
rep="true"
if a=="DEV@2023":
    print("bonjour")
else:
    for i in range(0,2):
        if a!="DEV@2023":
         rep="false"  
        print("le mot de passe incorrect")
        input("entrer le mot de passe")
if rep=="false":
    print("le mot de passe incorrect")
    b=input("qui ce que le nom de ton film prefere")
    if b=="harry poter":
            print("correct")
    else:
            print("incorrect")
