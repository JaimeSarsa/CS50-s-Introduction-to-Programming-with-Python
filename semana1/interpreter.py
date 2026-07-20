

calculadora = input("Operacion a realizar\n")
calculadora = calculadora.split(" ")

if calculadora[1] == "+":
    print(int(calculadora[0]) + int(calculadora[2]))
if calculadora[1] == "-":
    print(int(calculadora[0]) - int(calculadora[2]))
if calculadora[1] == "*":
    print(int(calculadora[0]) * int(calculadora[2]))
if calculadora[1] == "/":
    print(int(calculadora[0]) / int(calculadora[2]))
        
        