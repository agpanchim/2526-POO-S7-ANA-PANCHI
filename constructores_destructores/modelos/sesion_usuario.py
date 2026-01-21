from datetime import datetime


class SesionUsuario:
    """
    Modelo que representa una sesión de usuario.
    Demuestra el uso de __init__ y __del__ sin usar archivos externos.
    """

    def __init__(self, usuario: str):
        """
        CONSTRUCTOR (__init__)
        Se ejecuta automáticamente al crear el objeto.

        Inicializa:
        - nombre del usuario
        - fecha y hora de inicio de sesión
        """
        self.usuario = usuario
        self.inicio = datetime.now()

        print(f"{self.inicio} - Sesión iniciada: {self.usuario}")

    def registrar_accion(self, accion: str):
        """
        Registra una acción realizada por el usuario.
        """
        momento = datetime.now()
        print(f"{momento} - {self.usuario}: {accion}")

    def __del__(self):
        """
        DESTRUCTOR (__del__)
        Se ejecuta cuando el objeto deja de existir o el programa finaliza.

        Limpieza lógica:
        - registra el cierre de la sesión
        - libera el objeto de memoria
        """
        fin = datetime.now()
        print(f"{fin} - Sesión cerrada: {self.usuario}")
