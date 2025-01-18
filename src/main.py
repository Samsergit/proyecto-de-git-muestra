
import firebase_admin
from firebase_admin import credentials, auth

#estas son las credenciales para manejar firebase 

credencial = credentials.Certificate("/home/samuelserrano/Descargas/mis_entornos/src/usuarios-8cc30-firebase-adminsdk-la3bp-f5e96bda72.json")

# me conecto a firebase 
firebase_admin.initialize_app(credencial)


def verificar_usuario(email):
    try:
        user = auth.get_user_by_email(email)
        print('El usuario ya existe')
        return True
    except :
        return False

def registrarse(email, password):
    if verificar_usuario(email):
        print("El usuario ya está registrado.")
        return
    try:
        user = auth.create_user(email=email, password=password)
        print('Usuario registrado exitosamente:')
    except :
        print('Error al registrar usuario:')

def iniciar_sesion(email):
    try:
        user = auth.get_user_by_email(email)
        print('Inicio de sesión exitoso:')
    except :
        print('Error: usuario no encontrado')

def eliminar_usuario(email):
    if  verificar_usuario(email):
        print('El usuario no está registrado')
        return

    try:
        user = auth.get_user_by_email(email)
        auth.delete_user(user)
        print('Usuario eliminado exitosamente')
    except :
        print('Error al eliminar usuario')

def helper_user():
    email = input('Ingrese email: ')
    contrasena = input('Ingrese contrasena: ')
    return email, contrasena

while True:
    option = input('INICIO\n 1: Iniciar sesión \n 2: Registrarse \n 3: Eliminar cuenta \n 4: Salir \n:')

    match option:
        case '1':
            email, contrasena = helper_user()
            iniciar_sesion(email)
        case '2':
            email, contrasena = helper_user()
            registrarse(email, contrasena)
        case '3':
            email, contrasena = helper_user()
            eliminar_usuario(email)
        case '4':
            break
        case _:
            print('Caracter no válido')

        