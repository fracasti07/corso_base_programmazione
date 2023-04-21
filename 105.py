s_a = 0
s_e = 0
s_i = 0
s_o = 0
s_u = 0
y = 0
lunghezza_stringa = 0
nome_stringa: str=""
caratteri_stringa: str=""
nome_stringa=input("inserisci una stringa: ")
lunghezza_stringa=len(nome_stringa)
while( y<lunghezza_stringa):
    caratteri_stringa=nome_stringa[y]
    if(caratteri_stringa=="a" or caratteri_stringa=="A"):
        s_a = s_a + 1
    if(caratteri_stringa=="e" or caratteri_stringa=="E"):
        s_e = s_e + 1
    if(caratteri_stringa=="i" or caratteri_stringa=="I"):
        s_i = s_i + 1
    if(caratteri_stringa=="o" or caratteri_stringa=="O"):
        s_o = s_o + 1
    if(caratteri_stringa=="u" or caratteri_stringa=="U"):
        s_u = s_u + 1
    y = y + 1
print("a="+str(s_a))
print("e="+str(s_e))
print("i="+str(s_i))
print("o="+str(s_o))
print("u="+str(s_u))

