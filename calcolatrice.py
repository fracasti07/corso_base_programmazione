ricorda="per fare un'addizione digita 1, per fare una sottrazione digita 2, per fare una moltiplicazione digita 3, per fare una divisione digita 4, digita ESC se vuoi chiudere la calcolatrice."
while True:
    print(ricorda)
    azione = input("Inserisci il numero dell'operazione che vuoi svolgere: ")
    if(azione == "1"):
        print("Hai scelto: Addizione")
        a = float(input("Inserisci il Primo Numero -> "))
        b = float(input("Inserisci il Secondo Numero -> "))
        print("Il risultato dell'Addizione è: ", str(a + b))
    if(azione == "2"):
        print("Hai scelto: Sottrazione")
        a = float(input("Inserisci il Primo Numero -> "))
        b = float(input("Inserisci il Secondo Numero -> "))
        print("Il risultato dell'Sottrazione è: ", str(a - b))
    if(azione == "3"):
        print("Hai scelto: Moltiplicazione")
        a = float(input("Inserisci il Primo Numero -> "))
        b = float(input("Inserisci il Secondo Numero -> "))
        print("Il risultato dell'Moltiplicazione è: ", str(a * b))
    if(azione == "4"):
        print("Hai scelto: Divisione")
        a = float(input("Inserisci il Primo Numero -> "))
        b = float(input("Inserisci il Secondo Numero -> "))
        print("Il risultato dell'Divisione è: ", str(a / b))
    if(azione == "ESC"):
        print("applicazione chiusa!")
        break
    nuova_azione = input("Desideri continuare ad utilizzare l'Applicazione? Y/N ")
    if(nuova_azione == "Y" or nuova_azione == "y"):
        print("Sto tornando al menù principale!")
        continue
    else:
        print("ciao!")
        break