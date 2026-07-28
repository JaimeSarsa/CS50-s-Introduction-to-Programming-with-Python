import sys

def payment():
    coke_price = 50
    while(coke_price != 0):
        print(f"Amont due: {coke_price}")
        num = int(input("Insert coin: "))
        if num == 25 or num == 10 or num == 5:
            coke_price = coke_price - num
        else:
            print("Introduce 25, 10 o 5 cents")
        if coke_price <= 0:
            print(f"Changed Owed: {abs(coke_price)}")
            sys.exit()
    
def main():
    payment()

if __name__ == "__main__":
    sys.exit(main())

