
tam_max_clave = 26


def obtenerModo():
    while True:
        print("¿Deseas encriptar o desencriptar un mensaje? ")
        modo = input().lower()
        if modo in 'encriptar desencriptar bruta e d b'.split():
            return modo
        else:
            print("Ingresa 'encriptar' 'e' 'desencriotar' 'd' 'b' ")

def obtenerMensaje():
    print('Ingresa tu mensaje:')
    return input()

def obtenerClave():
    clave = 0
    while True:
        print(f'ingresa el numero de clave {1-tam_max_clave}')
        clave = int(input())
        if (clave >= 1 and clave <= tam_max_clave):
            return clave

def obtenerMensajeTraducido(modo,mensaje,clave):
    if modo[0] == 'd':
        clave = -clave
    traduccion = ''

    for simbolo in mensaje:
        if simbolo.isalpha():
            num = ord(simbolo)
            num +=clave

            if simbolo.isupper():
                if num > ord('Z'):
                    num -=26
                elif num < ord('A'):
                    num += 26
            elif simbolo.islower():
                if num > ord('z'):
                    num -= 26
                elif num < ord('a'):
                    num += 26
            traduccion += chr(num)
        else:
            traduccion += simbolo
    return traduccion

modo = obtenerModo()
mensaje = obtenerMensaje()
clave = obtenerClave()

if modo[0] != 'b':
    clave = obtenerClave()
print('Tu mensaje traducido es: ')

if modo[0] != 'b':
    print(obtenerMensajeTraducido(modo,mensaje,clave))
else:
    for clave in range(1, tam_max_clave + 1):
        print(clave,obtenerMensajeTraducido('d',mensaje,clave))
    
