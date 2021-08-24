def main():
    #escribe tu código abajo de esta línea
    nuevo=int(input("inserta el numero de juegos nuevos: "))
   usado=int(input("inserta el numero de juegos usados: ")) 
   nuevos= nuevo*1000
   usados= usado*350
   total= nuevos+usados
   print("El total de la compra es: "+str(total))
   pass



if __name__ == '__main__':
    main()
