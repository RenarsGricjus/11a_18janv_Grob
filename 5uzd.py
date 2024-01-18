def veidot(vards):
    try:
        with open("lietotajs.txt", "a") as make:
            make.write(vards)
    except FileExistsError:
        print(f"Fails jau eksistē!")
    except PermissionError:
        print(f"Nav atļauja rakstīt!")
    except Exception as error:
        print(f"Kļūda: {error}")

def ievade():
    lietot_vards = input("Ievadiet vārdu: ")
    veidot(lietot_vards)

if __name__ =="__main__":
    ievade()