import sys
import re

def empiezaPorHola(str):
    if re.search(r"^Hola", str, re.IGNORECASE): 
        return True
    else:
        return False

def empiezaPorH(str):
    if re.search(r"^H.*", str, re.IGNORECASE):
        return True
    else:
        return False



def main():
    cadena = input("Saludo del banco: ")
    if empiezaPorHola(cadena):
        print("$0")
    elif empiezaPorH(cadena):
        print("$20")
    else:
        print("$100")


if __name__ == "__main__":
    sys.exit(main())

#Importamos expresiones regulares