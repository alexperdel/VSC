miEmail=input("Introduce tu email: ")

arrobaDelante=miEmail.find("@")
arribaAtras=miEmail.rfind("@")

arroba=0
punto=0

for i in miEmail:
    if i =="@":
        arroba+=1
    if i ==".":
        punto+=1

if arroba==1 and punto>=1 and arrobaDelante!=0 and arribaAtras!=len(miEmail)-1:
    print("Email correcto")
else:
    print("Email incorrecto")
