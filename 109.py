stringa1 = input("inserisci la prima stringa: ")
stringa2 = input("inserisci la seconda stringa: ")
lunghezza_stringa1 = len(stringa1)
i=0
carattere=stringa1[i]
while i < lunghezza_stringa1:
    risultato=(carattere in stringa2)
    i = i + 1
print(risultato)

lunghezza_stringa2= len(stringa2)
i_2 = 0
carattere_2 = stringa2[i_2]
while i_2 < lunghezza_stringa2:
    risultato_2 = (carattere_2 in stringa1)
    i_2 = i_2 + 1
print(risultato_2)