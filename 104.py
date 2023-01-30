stringa=input("inserisci una stringa: ")
carattere=input("scegli un carattere della stringa: ")
contatore=len(stringa)
y = " "
i = 0
tot = 0
while i < contatore:
    y=stringa[i]
    if(y == carattere):
        tot = tot + 1
    i = i + 1
print(tot)