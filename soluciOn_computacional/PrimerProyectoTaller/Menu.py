#Modulos
from Funcion1 import funcion1
from Funcion2 import funcion2



#Funcion de menu para llamar a Funcion1 "Depreciacion Anual"  o Funcion2 "Depreciacion hasta la fecha"
def menuPrincipal():
  print("[ ->>> Bienvenido al Sistema <<<- ]\n")

  validezMenu = True
  while validezMenu:

    opcionIngresada = input("[Por favor ingrese una opcion:] \n1). Ver la Depreciacion Anual\n2). Ver la Depreciacion hasta la Fecha\n3). Salir\nIngrese una opción >>  ")
    if opcionIngresada.isdigit():
      opcionIngresada = int(opcionIngresada)
      if opcionIngresada==1:
          funcion1()
          break  
      elif opcionIngresada==2:
          funcion2()
          break
      elif opcionIngresada==3:
          print("Saliendo del Sistema")
          break
      else:
        print("ADVERTENCIA: La opcion ingresada no es valida, intente de nuevo\n")
    else:
      print("ADVERTENCIA: La entrada no corresponde a ninguna opcion, intente de nuevo\n")
menuPrincipal()
