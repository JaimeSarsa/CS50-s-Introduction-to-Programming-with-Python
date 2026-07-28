import sys

class ValueErrorZero(ValueError):
    pass #Error personalizado

def how_much_gasoline(str):
    
    str = str.split("/")
    try:
        if int(str[1]) == 0:
            raise ValueErrorZero("Error, el denominador no puede ser igual a 0")
    except ValueErrorZero as error:
        print(error)
        return False
    
    if int(str[0]) > int(str[1]):
        raise ValueError("Error el numerador no puede ser mayor al denominador")
    
    gasoline = int(str[0]) / int(str[1])

    if gasoline <= 0.01:
        print("E")
    elif gasoline >= 0.99:
        print("F")
    else:
        print(f"{gasoline * 100}%")

 

def main():
    
    Fraction = input("Fraction: ")
    
    how_much_gasoline(Fraction)
    


if __name__ == "__main__":
    sys.exit(main())