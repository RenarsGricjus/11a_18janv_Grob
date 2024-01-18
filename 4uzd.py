import os

def lasit_saturu(saturs):
    try:
        with open(saturs, "r", encoding="utf8") as filee:
            redd = filee.read()
        print(f"Faila saturs: {saturs}")
        print(redd)
    except FileNotFoundError:
        print("Fails nav atrasts!")

def ievads():
    saturs = input(f"Ievadiet faila nosaukumu: ")
    faila_pap = input(f"Ievadiet faila paplašinājumu: ")

    pilnais_nos = f"{saturs}.{faila_pap}"

    if os.path.exists(pilnais_nos):
        lasit_saturu(pilnais_nos)
    else:
        print(f"Fails{pilnais_nos} nav atrasts!")

ievads()


