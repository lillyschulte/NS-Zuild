def moderatie():
    """
    nog te beschrijven
    :return:
    """
    modmail = input("Email van moderator")
    modname = input("Naam van de moderator")
    if "@" in modmail:
        print("Success")
    else:
        print("Incorrect email format")
        exit()
    f = open('NS-bericht.txt', 'r')
    lines = f.readlines()
    for line in lines:
        msginfo = line.split(';')
        naam = msginfo[0]
        datum = msginfo[1]
        tijd = msginfo[2]
        bericht = msginfo[3]
        station = msginfo[4]

        print(bericht)
        print(naam)
        print(datum + "" + tijd)
        print(station)
        beoordeling = input('Gebruik y voor goedkeuren en n voor afkeuren.')

        if beoordeling == 'y' or beoordeling == '':
            print("Goed" + modname + " " + modmail)
        elif beoordeling == 'n':
            print("Fout")
        else:
            print("Error")

    f.close()
#    f = open('NS-bericht.txt', 'w')
#    f.close()