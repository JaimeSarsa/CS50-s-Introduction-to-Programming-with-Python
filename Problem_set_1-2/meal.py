import sys

def hora_a_flotante(str):
    str = str.split(":")
    hora = int(str[0])
    minuto = int(str[1]) / 6
    if hora >= 7 and hora < 8 or hora == 8 and minuto == 0:
        return "Hora de desayunar"
    elif hora >= 12 and hora < 13 or hora == 13 and minuto == 0:
        return "Hora de comer"
    elif hora >= 18 and hora < 19 or hora == 19 and minuto == 0:
        return "Hora de cenar"
    else:
        return "No es hora de comer"
    


def main():
    string = input("Introduce una hora: ")
    print(hora_a_flotante(string))
    

if __name__ == "__main__":
    sys.exit(main())