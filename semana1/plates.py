import sys
import re

def is_valid(s):
    contador_caracteres = 0
    
    for leter in s:
        contador_caracteres += 1

    if (
        s.startswith("0")
        or
        contador_caracteres < 2 or contador_caracteres > 6
        or 
        (re.search(r"[0-9][a-z]", s, re.IGNORECASE) and re.search(r"[a-z][0-9]", s, re.IGNORECASE))
        ):
        return False
    else:
        return True
   

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

if __name__ == "__main__":
    sys.exit(main())