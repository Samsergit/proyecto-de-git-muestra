from abc import ABC, abstractmethod

class Registros(ABC):

    @abstractmethod
    def inicializar_app(self):
        pass

    @abstractmethod
    def verificar_registro(self):
        pass

    @abstractmethod
    def registro(self):
        pass

    @abstractmethod
    def iniciar_sesion(self):
        pass

    @abstractmethod
    def eliminar_registro(self):
        pass

    @abstractmethod
    def helper(self):
        pass
