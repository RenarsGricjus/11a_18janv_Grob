with open("3uzd.txt", "r") as red:
    rindas = red.readlines()
    if len(rindas) >= 3:
        print(rindas[2].strip())

