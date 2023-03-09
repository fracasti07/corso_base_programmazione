elementi = ["carbonio" , "azoto", "fosforo", "zolfo", "iodio", "cloro", "bromo", "fluoro", "idrogeno", "ossigeno"]
n_ossidazione=["+2,+4","+1,+2,+3,+4,+5","+3,+5","-2,+4,+6","+1,+5,+7","+1,+3,+5,+7","+1,+3,+5","-1","+1","-2"]
m_atomica=["12,011","14,0067","30,97376","32,06","126,9046","35,453","79,904","18,99840","1,0079","15,9994",]
simboli=["C","N","P","S","I","Cl","Br","F","H","O"]
while True:
    elemento_utente=input("inserisci l'elemento che ti serve tra: carbonio, azoto, fosforo, zolfo, iodio, cloro, bromo, fluoro, idrogeno, ossigeno: ")
    if(elemento_utente in elementi):
        print("ok")
        break
while True:
    if(elemento_utente=="carbonio"):
        simbolo_C=input("Vuoi il simbolo del carbonio?: ")
        if(simbolo_C=="si"):
            print(simboli[0])
        else:
            if(simbolo_C=="no"):
                print("va bene")
        risposta_1=input("Vuoi il numero di ossidazione del carbonio? ")
        if(risposta_1=="si"):
            print(n_ossidazione[0])
        else:
            if(risposta_1=="no"):
                print("va bene")
        risposta_2=input("Vuoi la massa atomica del carbonio? ")
        if(risposta_2=="si"):
            print(m_atomica[0])
        else:
            if(risposta_2=="no"):
                print("ok")
        break
    if(elemento_utente=="azoto"):
        simbolo_N=input("Vuoi il simbolo dell'azoto?: ")
        if(simbolo_N=="si"):
            print(simboli[1])
        else:
            if(simbolo_N=="no"):
                print("va bene")
        risposta_1=input("Vuoi il numero di ossidazione dell'azoto? ")
        if(risposta_1=="si"):
            print(n_ossidazione[1])
        else:
            if(risposta_1=="no"):
                print("va bene")
        risposta_2=input("Vuoi la massa atomica dell'azoto? ")
        if(risposta_2=="si"):
            print(m_atomica[1])
        else:
            if(risposta_2=="no"):
                print("va bene")
        break
    if(elemento_utente=="fosforo"):
        simbolo_P=input("Vuoi il simbolo del fosforo?: ")
        if(simbolo_P=="si"):
            print(simboli[2])
        else:
            if(simbolo_P=="no"):
                print("va bene")
        risposta_1=input("Vuoi il numero di ossidazione del fosforo? ")
        if(risposta_1=="si"):
            print(n_ossidazione[2])
        else:
            if(risposta_1=="no"):
                print("va bene")
        risposta_2=input("Vuoi la massa atomica del fosforo? ")
        if(risposta_2=="si"):
            print(m_atomica[2])
        else:
            if(risposta_2=="no"):
                print("va bene")
        break
    if(elemento_utente=="zolfo"):
        simbolo_S=input("Vuoi il simbolo dello zolfo?: ")
        if(simbolo_S=="si"):
            print(simboli[3])
        else:
            if(simbolo_S=="no"):
                print("va bene")
        risposta_1=input("Vuoi il numero di ossidazione delo zolfo? ")
        if(risposta_1=="si"):
            print(n_ossidazione[3])
        else:
            if(risposta_1=="no"):
                print("va bene")
        risposta_2=input("Vuoi la massa atomica dello zolfo? ")
        if(risposta_2=="si"):
            print(m_atomica[3])
        else:
            if(risposta_2=="no"):
                print("va bene")
        break
    if(elemento_utente=="iodio"):
        simbolo_I=input("Vuoi il simbolo dello iodio?: ")
        if(simbolo_I=="si"):
            print(simboli[4])
        else:
            if(simbolo_I=="no"):
                print("va bene")
        risposta_1=input("Vuoi il numero di ossidazione dello iodio? ")
        if(risposta_1=="si"):
            print(n_ossidazione[4])
        else:
            if(risposta_1=="no"):
                print("va bene")
        risposta_2=input("Vuoi la massa atomica dello iodio? ")
        if(risposta_2=="si"):
            print(m_atomica[4])
        else:
            if(risposta_2=="no"):
                print("va bene")
        break
    if(elemento_utente=="cloro"):
        simbolo_Cl=input("Vuoi il simbolo del cloro?: ")
        if(simbolo_Cl=="si"):
            print(simboli[5])
        else:
            if(simbolo_Cl=="no"):
                print("va bene")
        risposta_1=input("Vuoi il numero di ossidazione del cloro? ")
        if(risposta_1=="si"):
            print(n_ossidazione[5])
        else:
            if(risposta_1=="no"):
                print("va bene")
        risposta_2=input("Vuoi la massa atomica del cloro? ")
        if(risposta_2=="si"):
            print(m_atomica[5])
        else:
            if(risposta_2=="no"):
                print("va bene")
        break
    if(elemento_utente=="bromo"):
        simbolo_Br=input("Vuoi il simbolo del bromo?: ")
        if(simbolo_Br=="si"):
            print(simboli[6])
        else:
            if(simbolo_Br=="no"):
                print("va bene")
        risposta_1=input("Vuoi il numero di ossidazione del bromo? ")
        if(risposta_1=="si"):
            print(n_ossidazione[6])
        else:
            if(risposta_1=="no"):
                print("va bene")
        risposta_2=input("Vuoi la massa atomica del bromo? ")
        if(risposta_2=="si"):
            print(m_atomica[6])
        else:
            if(risposta_2=="no"):
                print("va bene")
        break
    if(elemento_utente=="fluro"):
        simbolo_F=input("Vuoi il simbolo del fluoro?: ")
        if(simbolo_F=="si"):
            print(simboli[7])
        else:
            if(simbolo_F=="no"):
                print("va bene")
        risposta_1=input("Vuoi il numero di ossidazione del fluoro? ")
        if(risposta_1=="si"):
            print(n_ossidazione[7])
        else:
            if(risposta_1=="no"):
                print("va bene")
        risposta_2=input("Vuoi la massa atomica del fluoro? ")
        if(risposta_2=="si"):
            print(m_atomica[7])
        else:
            if(risposta_2=="no"):
                print("va bene")
        break
    if(elemento_utente=="idrogeno"):
        simbolo_H=input("Vuoi il simbolo dell'idrogeno?: ")
        if(simbolo_H=="si"):
            print(simboli[8])
        else:
            if(simbolo_H=="no"):
                print("va bene")
        risposta_1=input("Vuoi il numero di ossidazione del idrogeno? ")
        if(risposta_1=="si"):
            print(n_ossidazione[8])
        else:
            if(risposta_1=="no"):
                print("va bene")
        risposta_2=input("Vuoi la massa atomica dell'idrogeno? ")
        if(risposta_2=="si"):
            print(m_atomica[8])
        else:
            if(risposta_2=="no"):
                print("va bene")
        break
    if(elemento_utente=="ossigeno"):
        simbolo_O=input("Vuoi il simbolo dell'ossigeno?: ")
        if(simbolo_O=="si"):
            print(simboli[9])
        else:
            if(simbolo_O=="no"):
                print("va bene")
        risposta_1=input("Vuoi il numero di ossidazione dell'ossigeno? ")
        if(risposta_1=="si"):
            print(n_ossidazione[9])
        else:
            if(risposta_1=="no"):
                print("va bene")
        risposta_2=input("Vuoi la massa atomica dell'ossigeno? ")
        if(risposta_2=="si"):
            print(m_atomica[9])
        else:
            if(risposta_2=="no"):
                print("va bene")
        break
print("grazie per aver consultato questa tavola periodica dei non metalli")