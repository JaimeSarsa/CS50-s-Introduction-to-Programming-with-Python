import sys
import re

def erase_vowels(str):
    cadena = re.sub(r"[aeiou]", "", str, flags=re.IGNORECASE)
    return cadena

def main():
    string = input("Input: ")
    print(erase_vowels(string))

if __name__ == "__main__":
    sys.exit(main())