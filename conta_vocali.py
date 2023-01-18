i = 0
contatore = 0
n_vocali = 0
stringa=input("inserisci na stringa: ")
lunghezza=len(stringa)
while i<lunghezza:
    carattere=stringa[i]
    if(carattere=="A"):
        n_vocali=contatore+1
        contatore=contatore+1
    if(carattere=="E"):
        n_vocali=contatore+1
        contatore=contatore+1
    if(carattere=="I"):
        n_vocali=contatore+1
        contatore=contatore+1
    if(carattere=="O"):
        n_vocali=contatore+1
        contatore=contatore+1
    if(carattere=="U"):
        n_vocali=contatore+1
        contatore=contatore+1
    i=i+1
print(n_vocali)
     