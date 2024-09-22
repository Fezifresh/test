def main ():
    print("Wie heißt du?")
    name = input()
    print(f"Hallo ,{name}!")
    if name == "Felix":
        print("Mach weiter an deinem Projekt!")
    elif name == "Ivana":
        print("Ich glaube du solltest deinen Mann dazu überreden, Schnitzel zu bestellen!")
    else:
        print("Schön, dass du da bist!")
main()