text: str=""
lenght_text: int=0
i: int=0
c: int=0
while True:
    text=input("inserisci una stringa di soli numeri: ")
    lenght_text=len(text)
    i=0
    while i<lenght_text:
        c=text[i]
        if(c.isnumeric()==False):
            break
        i=i+1
print("fine programma")