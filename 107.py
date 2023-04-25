i=0
stringa=input("inserisci una stringa: ")
output=""
lunghezza_stringa=len(stringa)
while i<lunghezza_stringa:
    if stringa[i]!="a" and stringa[i]!="e" and stringa[i]!="i" and stringa[i]!="o" and stringa[i]!="u" and stringa[i]!="A" and stringa[i]!="E" and stringa[i]!="I" and stringa[i]!="O" and stringa[i]!="U":
        output=output+stringa[i]
    i=i+1
print(output)