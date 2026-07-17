import sys 

def convert(str):
    str = str.replace(":)", "🙂")
    str = str.replace(":(", "🙁")

    return str

def main():
    cadena = input("Introduzca una cadena: ")
    cadenon = convert(cadena)
    print(cadenon)

if __name__ == "__main__":
    sys.exit(main())