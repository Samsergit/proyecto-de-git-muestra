
import firebase_admin
from firebase_admin import credentials, firestore

class PermisoManager:
    def __init__(self, db):
        self.db = db

    def obtener_permisos(self, usuario_id):
        """Obtiene los permisos de un usuario dado su ID.

        Args:
            usuario_id: El ID del usuario.

        Returns:
            Una lista con los IDs de los módulos a los que tiene acceso el usuario.
        """
        doc_ref = self.db.collection('usuarios').document(usuario_id)
        doc = doc_ref.get()
        if doc.exists:
            return doc.to_dict().get('permisos', [])
        else:
            return []

    def asignar_permisos(self, usuario_id, nuevos_permisos):
        """Asigna nuevos permisos a un usuario.

        Args:
            usuario_id: El ID del usuario.
            nuevos_permisos: Una lista con los IDs de los nuevos permisos.
        """
        doc_ref = self.db.collection('usuarios').document(usuario_id)
        doc_ref.update({'permisos': nuevos_permisos})

    def revocar_permisos(self, usuario_id, permisos_a_revocar):
        """Revoca permisos a un usuario.

        Args:
            usuario_id: El ID del usuario.
            permisos_a_revocar: Una lista con los IDs de los permisos a revocar.
        """
        doc_ref = self.db.collection('usuarios').document(usuario_id)
        doc = doc_ref.get()
        if doc.exists:
            permisos_actuales = doc.to_dict().get('permisos', [])
            nuevos_permisos = [p for p in permisos_actuales if p not in permisos_a_revocar]
            doc_ref.update({'permisos': nuevos_permisos})
    