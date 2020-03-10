##########################################################################
#                               LIBRERIAS                                #
##########################################################################
from termcolor import colored, cprint
import os
from random import choice
import hashlib


##########################################################################
#                               MENU PRINCIPAL                           #
##########################################################################

def inicio():
    os.system('reset')
    cprint('''
 ___   ___  __  __  ____  ____  ___  ____  ___  ____   ___    
/ __) / _ \(  \/  )(  _ \(  _ \(__ )(  _ \(__ )(  _ \ / _ \   
\__ \( (_) ))    (  ) _ < )   / (_ \ )   / (_ \ )   /( (_) )  
(___/ \___/(_/\/\_)(____/(_)\_)(___/(_)\_)(___/(_)\_) \___/   ''', 'green', 'on_grey')
 
    cprint('MACHINE                               Version: 1.0, Marzo 2020', 'red', 'on_grey')
    cprint('\nSelecciona una opcion:', 'yellow', 'on_grey')
    cprint('1)Generador passwords', 'white', 'on_grey')
    cprint('2)Encriptador', 'white', 'on_grey')
    cprint('3)Generador de Diccionarios', 'white', 'on_grey')
    cprint('4)Escaneo de red', 'white', 'on_grey')
    cprint('5)Analisis web\n', 'white', 'on_grey')

    a = input('>')

    if a == '1':
        claves = ('0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"·$%&/()={[]}|@#')
        cprint('¿Cuantos caracteres quieres para tu Password?', 'yellow', 'on_grey')
        longitud = int(input('>'))
        l = ''
        l = l.join([choice(claves) for i in range(longitud)])

        cprint('TU PASSWORD ES:', 'yellow', 'on_grey')
        cprint('\n'+str(l), 'cyan', 'on_grey')
        cprint('\nPresiona Enter para continuar..', 'yellow', 'on_grey')
        input('')
        inicio()

    elif a == '2':
        cprint('Introduce una plabra para cifrar', 'yellow', 'on_grey')
        a = input('>')
        a1 = hashlib.sha256(str.encode(a)).hexdigest()
        a2 = hashlib.sha512(str.encode(a)).hexdigest()
        a3 = hashlib.md5(str.encode(a)).hexdigest()

        cprint('\nTu palabra cifrada en SHA256:', 'yellow', 'on_grey')
        cprint(a1, 'cyan', 'on_grey')

        cprint('\nTu palabra cifrada en SHA512:', 'yellow', 'on_grey')
        cprint(a2, 'cyan', 'on_grey')
        
        cprint('\nTu palabra cifrada en MD5:', 'yellow', 'on_grey')
        cprint(a3, 'cyan', 'on_grey')

        cprint('\nPresiona Enter para continuar..', 'yellow', 'on_grey')
        input('')
        inicio()

    elif a == '3':
        pass
    elif a == '4':
        pass
    elif a == '5':
        pass
    else:
        cprint('Opcion no valida', 'red', 'on_grey')





inicio()