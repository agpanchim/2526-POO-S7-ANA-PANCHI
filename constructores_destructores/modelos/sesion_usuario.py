from datetime import datetime

class SesionUsuario:
    """
    Modelo que representa una sesión de usuario.
    Demuestra el uso de __init__ y __del__ con registro en archivo .log
    """

    def __init__(self, usuario: str):
        """
        CONSTRUCTOR (__init__)
        Inicializa:
        - nombre del usuario
        - fecha y hora de inicio de sesión

        Registra el inicio en consola y en un archivo sesion.log
        """
        self.usuario = usuario
        self.inicio = datetime.now()

        mensaje = f"{self.inicio} - Sesión iniciada: {self.usuario}"

        print(mensaje)
        self._escribir_log(mensaje)

    def registrar_accion(self, accion: str):
        """
        Registra una acción realizada por el usuario.
        """
        momento = datetime.now()
        mensaje = f"{momento} - {self.usuario}: {accion}"

        print(mensaje)
        self._escribir_log(mensaje)

    def _escribir_log(self, mensaje: str):
        """
        Método interno para escribir mensajes en el archivo sesion.log
        """
        with open("sesion.log", "a", encoding="utf-8") as archivo:
            archivo.write(mensaje + "\n")

    def __del__(self):
        """
        DESTRUCTOR (__del__)
        Se ejecuta cuando el objeto se elimina o el programa termina.

        Registra el cierre de la sesión en consola y en el archivo .log
        """
        fin = datetime.now()
        mensaje = f"{fin} - Sesión cerrada: {self.usuario}"

        print(mensaje)
        self._escribir_log(mensaje)
