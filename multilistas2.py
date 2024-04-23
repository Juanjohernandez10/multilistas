''' elaborar un sistema en python que utilizando multilistas y realiza las siguientes funciones 
1. registrar candidatos a una oportunidad de empleo el cual debe seguir las siguientes condiciones 

      a) edad (24-35 años )
      b) profesion: ING. SISTEMAS  / ING.INFORMATICO
      b) experiencia: 2 a 4 años 
      
2. consultar candidadtos : mostrar todos los candidatos 
3. informacion a capturar
    - nombres y apellidos 
    - correo electronico 
    - identificacion 
    -contacto
    - edad 
    - años de experiencia 
    - profesion 
    - ciudad 
    - sexo '''
    
ls_nombre_completo = []
ls_correo = []
ls_identificacion = []
ls_contacto = []
ls_edad = []
ls_años_experiencia = []
ls_profesion = []
ls_ciudad = []
ls_sexo = []
import os

def fnt_limpiar():
    os.system('cls')
    print('AUTOR: juan jose hernandez ')
    print('FECHA: 18 de abril 24')

def fnt_registrar_candidatos(nombres, correo, identificacion, contacto, edad, años_experiencia, profesion, ciudad, sexo):
    if nombres == ' ' or correo == ' ' or identificacion == ' ' or contacto == ' ' or edad == ' ' or años_experiencia == ' ' or profesion == ' ' or ciudad == ' ' or sexo == ' ':
        print('los campos no pueden estar vacios')
    elif (24 <= edad <= 35) and (2 <= años_experiencia <= 4) and (profesion == 'sistemas' or profesion == 'informatica') :
        ls_nombre_completo.append(nombres)
        ls_correo.append(correo)
        ls_identificacion.append(identificacion)
        ls_contacto.append(contacto)
        ls_edad.append(edad)
        ls_años_experiencia.append(años_experiencia)
        ls_profesion.append(profesion)
        ls_ciudad.append(ciudad)
        ls_sexo.append(sexo)
        enter = input('\n ya se encuentra registrado <ENTER>')
    else:
        enter = input('Las condiciones no se cumplen< ENTER>')

def fnt_consultar_candidatos():
    fnt_limpiar()
    for i in range(len(ls_identificacion)):
        print(f'nombre :{ls_nombre_completo[i]}   correo:{ls_correo[i]}    identificacion:{ls_identificacion[i]}  contacto:{ls_contacto[i]}  edad:{ls_edad[i]}  años_experiencia:{ls_años_experiencia[i]} profesion:{ls_profesion[i]} ciudad:{ls_ciudad[i]} sexo:{ls_sexo[i]}')
        
def fnt_selector(op):
    if op == '1':
        identificacion = input('ingrese la identificacion -> ')
        if identificacion in ls_identificacion:
            enter = input('la identificacion ya se encuentra registrada <ENTER>')
        else:
            nombres = input('ingrese el nombre completo -> ')
            correo = input('ingrese el correo -> ')
            contacto = input('ingrese el contacto -> ')
            edad = int(input('ingrese la edad -> '))
            años_experiencia = int(input('ingrese los años de experiencia '))
            profesion = input(' ingrese la profesion -> ')
            ciudad = input(' ingrese la ciudad -> ')
            sexo = input(' ingrese el sexo -> ')
            fnt_registrar_candidatos(nombres, correo, identificacion, contacto, edad, años_experiencia, profesion, ciudad, sexo)
    elif op == '2':
        fnt_consultar_candidatos()
        enter = input('\nPresiona <ENTER> para continuar...')
    elif op == '3':
        print('Gracias por usar el sistema')
        sw = False

sw = True
while sw == True:
    fnt_limpiar()
    op = input(' <<<<MENU>>>> \n1. registrar candidatos \n2. listas candidatos \n3. salir \n-> ')
    fnt_selector(op)