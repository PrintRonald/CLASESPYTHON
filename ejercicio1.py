# tipos de datos

# int nmros enteros
#n = 1
#print(type(n))


#lista = []
#temperaturas = input('Ingrese temperaturas: ')
#lista.append(temperaturas)
#print(lista)

#i = input('Ingrese si estamos de dia para trabajar: Respinda Si/No ')
#while True:
#  if i == 'Si':
#    print('es de dia podemos trabajar')
#    break
#  else:
#    print('Es de noche no se puede trabajar. Vuelva a consultar')
#    i = input('Ingrese si estamos de dia para trabajar: Respinda Si/No ')  
#
#ListaT = []
#temperatura = int(input('Ingrese la temperatura: '))
#while True:
#  if temperatura < 0:
#    temperatura = int(input('Ingrese la temperatura: '))
#  elif temperatura == -1:
#     break
#     print(ListaT)
#  else:
#     ListaT.append(temperatura)  
#
     
     
ListaR = []
while True:
    Kilometros = input('Ingrese cantidad de kilimetros recorridos')
    try:
        Kilometros = int(Kilometros)
        if Kilometros >= 0:
            ListaR.append(Kilometros)
            continuar = input('Desea ingresar otra cantidad?')
            if continuar == 'S' or continuar == 's':
                pass
            else:
                maximo = max(ListaR)
                print(f'La cantidad mas alta es: {maximo}')
                promedio = sum(ListaR)/len(ListaR)
                print(f'El promedio es: {promedio}')
                break

        else:
            print('Error. Numero fuera de rango')
            pass
    except ValueError:
        print('Error. No es un numero')