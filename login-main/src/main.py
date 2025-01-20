from usuarios.Usuarios import Usuarios

def main():
    email = input('Ingrese email: ')
    contrasena = input('Ingrese contraseña: ')  # Corregido de 'contrasena' a 'contraseña'
    return email, contrasena

if __name__ == "__main__":
    email, contrasena = main()
    new_user = Usuarios(email, contrasena)

    while True:
        option = input('INICIO\n 1: Iniciar sesión \n 2: Registrarse \n 3: Eliminar cuenta \n 4: Salir \n:')
        match option:
            case '1':
                new_user.iniciar_sesion()
            case '2':
                new_user.registro()  # Cambiado de 'registrarse()' a 'registro()'
            case '3':
                new_user.eliminar_registro()  # Cambiado de 'eliminar_usuario()' a 'eliminar_registro()'
            case '4':
                print("Saliendo de la aplicación...")
                break
            case _:
                print('Caracter no válido')
