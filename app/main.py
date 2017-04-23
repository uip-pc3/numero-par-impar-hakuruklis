def ParImpar(numero):
    if numero%2 == 0 :
        return 1
    else:
        return 0

if __name__ == "__main__":
    numero = int(input("Ingrese un numero: "))
    if par_impar(numero)==1 :
        print("Es par")
    else:
        print("Es impar")