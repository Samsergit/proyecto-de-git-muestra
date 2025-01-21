from registros.Registros import Registros
from config.constantes import credenciales, nombre_documento
import firebase_admin
from firebase_admin import credentials, firestore
from google.cloud.firestore_v1.base_query import FieldFilter

class Usuarios(Registros):

    def __init__(self, mail: str, password: str, modulos: str = "1,2"):
        self.email = mail
        self.password = password
        self.modulos = modulos
        self.db = None
        self.inicializar_app()

    def inicializar_app(self):
        try:
            cred = credentials.Certificate(credenciales)
            firebase_admin.initialize_app(cred)
            self.db = firestore.client()
            print("Conexión con Firebase exitosa.")
        except Exception as e:
            print(f"Error al conectar con Firebase: {e}")
            raise

    def verificar_registro(self):
        """
        Verifica si el usuario existe en la base de datos.
        """
        try:
            usuarios_ref = self.db.collection(nombre_documento)
            # Usar el método where correctamente
            query = usuarios_ref.where(filter=FieldFilter("email",  "==", self.email)).get()
            print("Consulta realizada")  # Para depuración

            # Procesar los resultados
            if query:
                for doc in query:
                    print(f"ID del documento: {doc.id}")
                    print(f"Datos: {doc.to_dict()}")
                    return doc.to_dict()
            else:
                print("No se encontró el usuario.")
                return None
                
        except Exception as e:
            print(f"Error al realizar la consulta: {e}")
            return None

    def registro(self):
        try:
            if self.verificar_registro():
                return print("Ya existe el usuario.")
            else:
                doc_ref = self.db.collection(nombre_documento).add(
                    {"email": self.email, "password": self.password, "modulos": self.modulos}
                )
                return doc_ref.id
        except Exception as e:
            print(f"Error al agregar documento: {e}")
            raise
    
    def iniciar_sesion(self):
        """
        Verifica el inicio de sesión del usuario.
        """
        try:
            usuario = self.verificar_registro()
            if usuario:
                print(f"Acceso concedido: {usuario}")
            else:
                print(f"El usuario {self.email} no existe")
        except Exception as e:
            print(f"Error al iniciar sesión: {e}")
            raise
    
    def eliminar_registro(self):
        """
        Elimina un registro de usuario (pendiente de implementación).
        """
        print("Pendiente de implementación.")
    
    def helper(self):
        """
        Función de ayuda para mostrar los métodos disponibles (pendiente de implementación).
        """
        print("Pendiente de implementación.")
