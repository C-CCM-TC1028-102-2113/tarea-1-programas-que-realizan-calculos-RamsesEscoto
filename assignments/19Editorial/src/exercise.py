def main():
    #escribe tu código abajo de esta línea
       palabrast=int(input("ingresa número de palabras: "))
    pags=(math.ceil(palabrast/475))
    total=pags*60
    descuento=total*.10
    totals=total-descuento
    totals=round(totals,1)
    pass


if __name__ == '__main__':
    main()
