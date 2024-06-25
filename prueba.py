

def categoria():
    {

         "'ensayo":2,
 "'ciencia ficcion":2,
 " LITERATURA":1,
 "FICCION":3,
 "NOVELA":1,
 "fantas":3,
 "literatura CL":1,
 "historia":1,
 "biografia":1,
 "cuento":1,
 "teatro":2,
 "poes":0
  



 }

while True:
    print('************************************')
    print('           MUNDO LIBRO              ')
    print('************************************')
    print('1. -Mantenedor de usuarios')
    print('2. -Reportes')
    print('3. -salir')
    
    opcion = input("Seleccione una opcion: ")  
    
    if opcion == '1':
        while True:
            print('********************************')
            print('     MANTENEDOR DE USUARIOS      ')
            print('********************************')
            print('1. Agregar usuario')
            print('2. Editar usuario')
            print('3. Eliminar usuario')
            print('4. Buscar usuario')
            print('5. Volver')
            
            user_option = input("Seleccione una opcion: ")
            
    elif opcion=="2":

        print('**************************************************')
        print('* CATEGORIA           -       CANTIDAD DE LIBROS *')
        print('**************************************************')

        print(f"{categoria}")
    
    
    
    elif opcion =="3":

        print('saliendo...')
        break



                
   
