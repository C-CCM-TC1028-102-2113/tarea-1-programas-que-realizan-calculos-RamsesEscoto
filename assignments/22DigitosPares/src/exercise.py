def main():
    #escribe tu código abajo de esta línea
      digito=int(input("Dame el número: "))
    par=0
    if digito>-10000 and digito<=-1000 or digito>=1000 and digito<10000:
        while (digito>0):
            if digito%2==0:
                par=par+1
            else: 
                par=par+0
            digito=digito//10
        print("El número de dígitos pares es: "+ str(par))
    pass


if __name__ == '__main__':
    main()
