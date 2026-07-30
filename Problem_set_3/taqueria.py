import sys

dict = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

def Price(str):
    for item, price in dict.items():
        if str == item:
           return price 
    

def main():
    Item = input("Item: ")
    print(f"Price: {Price(Item):.2f}")

if __name__ == "__main__":
    sys.exit(main())