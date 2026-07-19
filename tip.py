import sys

def main():
    dolares = dolares_a_flotante(input("Cuanto ha costado la comida? "))
    porcentaje = porcentaje_a_flotante(input("Porcentaje de propina? "))
    propina = dolares * porcentaje
    print(f"propina: ${propina:.2f}")

def dolares_a_flotante(dollars):
    dollars = dollars.replace("$","")
    return float(dollars)

def porcentaje_a_flotante(percentage):
    percentage = percentage.replace("%","")
    return float(percentage) / 100

if __name__ == "__main__":
    sys.exit(main())