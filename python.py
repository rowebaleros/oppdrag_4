import json, os

FILNAVN = "varer.json"

def printMeny():
    print("*******************LAGRINGSYSTEM*********************")
    print("1. Registrer ny vare")
    print("2. Søk etter vare")
    print("3. Skriv ut rapport")
    print("4. Avslutt programmet")

def registrerVare():
    varenavn = input("Skriv inn varenavn: ")

    while True:
        try:
            varenummer = int(input("Skriv inn varenummer (kun tall): "))
            break
        except ValueError:
            print("Ugyldig input. Varenummer må være et tall.")

    antall = input("Skriv inn antall: ")

    while True:
        try:
            pris = int(input("Skriv inn pris (kun tall): "))
            break
        except ValueError:
            print("Ugyldig input. Pris må være et tall.")

    nyvare = {
        "varenavn": varenavn,
        "varenummer": varenummer,
        "antall": antall,
        "pris": pris
    }

    varer = []
    if os.path.exists(FILNAVN):
        with open(FILNAVN, "r") as fil:
            varer = json.load(fil)

    varer.append(nyvare)

    with open(FILNAVN, "w") as fil:
        json.dump(varer, fil, indent=4)

    print("Varen ble registrert.")

def sokVare():
    try:
        varenummer = int(input("Skriv inn varenummer for å søke: "))
    except ValueError:
        print("Ugyldig input. Varenummer må være et tall.")
        return

    if os.path.exists(FILNAVN):
        with open(FILNAVN, "r") as fil:
            varer = json.load(fil)
            for vare in varer:
                if vare["varenummer"] == varenummer:
                    print(f"Funnet: {vare['varenavn']}, Antall: {vare['antall']}, Pris: {vare['pris']}")
                    return
            print("Varen ble ikke funnet.")
    else:
        print("Ingen varer registrert ennå.")

def skrivUtRapport():
    if os.path.exists(FILNAVN):
        with open(FILNAVN, "r") as fil:
            varer = json.load(fil)
            for vare in varer:
                print(f"{vare['varenavn']} (#{vare['varenummer']}) - Antall: {vare['antall']}, Pris: {vare['pris']}")
    else:
        print("Ingen varer registrert.")

def avsluttProgram():
    print("Programmet avsluttes.")
    return True

avslutt = False
while not avslutt:
    printMeny()
    valg = input("Velg ønsket menyvalg 1-4: ")
    if valg == "1":
        registrerVare()
    elif valg == "2":
        sokVare()
    elif valg == "3":
        skrivUtRapport()
    elif valg == "4":
        avslutt = avsluttProgram()
    else:
        print("Ugyldig valg. Skriv et tall mellom 1 og 4.")
