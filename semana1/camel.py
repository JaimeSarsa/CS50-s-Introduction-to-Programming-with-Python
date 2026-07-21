import sys

def convertToSneakCase(str):
    for letra in range(len(str)):
        if str[letra].isupper():
            print(f"_", end="")
        print(str[letra], end="")
        
    
    


def main():
    cadena = input("camelCase: ")
    print("snake_case: ", end="")
    convertToSneakCase(cadena)
    print("\n")


if __name__ == "__main__":
    sys.exit(main())