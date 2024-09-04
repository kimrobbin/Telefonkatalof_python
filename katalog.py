telefonkatalog = [] # listeformat ["fornavn", "etternavn", "telefonummer"]


def printMeny():
    print("------------------Telefonkatalog--------------------")
    print("| 1. Legg til ny person                            |")
    print("| 2. Søk opp person eller telefonnummmer           |")
    print("| 3. Vis alle personer                             |")
    print("| 4. Avslutt                                       |")
    print("----------------------------------------------------")
    menyvalg = input("Skriv inn tall for å vlge fra menyen: ")
    utenfoerMenyvalg(menyvalg)



def utenfoerMenyvalg(valgtTall):
    if valgtTall == "1": # input returner string, derfor "1"
        registrerPerson()
    elif (valgtTall) == "2":
        sokPerson()    
        printMeny()
    elif valgtTall == "3":
        visAllePersoner()
    elif valgtTall == "4":
        bekreftelse = input("Er du sikker på at du vil avslutte J/N" )
        if (bekreftelse == "j" or bekreftelse == "J"): #sjekker bare for ja 
            exit()
    else: nyttForsoek = input("Ugyldig valg. Velg et tall mellom 1-4: ")



def registrerPerson():
    fornavn = input("Skriv in fornavn: ")
    etternavn = input("Skriv inn etternavn: ")
    telefonnummmer = input("Skriv inn telefonnummmer ")

    nyRegistrering = [fornavn, etternavn, telefonnummmer]
    telefonkatalog.append(nyRegistrering)

    print("{0} {1} er registrert med tellefonnumer {2}"
        .format(fornavn, etternavn, telefonnummmer))
    input("trykk en tast for å gå tilbake til menyen ")
    printMeny()



def visAllePersoner():
    if not telefonkatalog:
        print("Det er ingen registrerte personer i katalogen")
        input("Trykk en tast for å gå tilbaket til menyen ")
    else:
        print("****************************************************"
              "****************************************************")
        for personer in telefonkatalog:
            print("* Fornavn: {:15s} Etternavn: {:15s} Telefonnummer:{:8s}"
            .format(personer[0], personer[1], personer[2]))
        print("****************************************************"
              "****************************************************")
        input("Trykk en tast for å gå tilbake til menyen ")
        printMeny()



def sokPerson():
    if not telefonkatalog:
        print("Det er ingen registrerte personer i katalogen")
        printMeny()
    else:
        print("1. Søk på fornavn")
        print("2. Søk på etternanv")
        print("3. Søk på telefonnummer")
        print("Tilbake til hovedmeny")
        sokefelt = input("Velg ønsket søk 1-3, eller 4 for å gå tilbaket: ")
        if sokefelt == "1":
            navn = input("Fornavn: ")
            finnPerson("fornavn", navn)
        elif sokefelt == "2":
            navn = input("Etternavn: ")
            finnPerson("etternavn", navn)
        elif sokefelt == "3":
            tlfnummer = input("Telefonnummer")
            finnPerson("telefonnummer", tlfnummer)

        elif sokefelt == "4":
            printMeny()
        else:
            print("Ugyldig valg. Velg et tall mellom 1-4: ")
            sokPerson()

# typeSok angir om man søker på fornavn, etternavn eller telfonnummer
def finnPerson(typeSok, sokeTekst):
    for personer in telefonkatalog:
        if typeSok == "fornavn":
            if personer[0] == sokeTekst:
                print("{0} {1} har telefonnummer"
                      .format(personer[0], personer[1], personer[2]))
            else:
                print("Finner ingen personer med fornavn " + sokeTekst)
                sokPerson()
        elif typeSok == "etternavn":
            if personer[1] == sokeTekst:
                print("{0} {1} har telefonnummer {2}"
                      .format(personer[0], personer[1], personer[2]))
            else:
                print("Finner ingen personer med etternavn " + sokeTekst)
                sokPerson()
        elif typeSok == "telefonnummer":
            if personer[2] == sokeTekst:
                print("Telefonnummer {0} tilhører {1} {2}"
                      .format(personer[2], personer[1], personer[1]))
            else:
                print("Telefonnummer " + sokeTekst + " er ikke registrert. /n")
                sokPerson()
                

printMeny() # Starter programmet ved å skrive menyen første gang