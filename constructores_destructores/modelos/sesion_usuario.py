from datetime import datetime

class SesionUsuario:
    """
    Modelo que representa una sesión de usuario en el sistema.
    """

    def __init__(self, usuario):
        """
        Constructor (__init__):
        - Inicializa el usuario
        - Marca la sesión como activa
        - Abre un archivo de registro (recurso del sistema)
        """
        self.usuario = usuario
        self.activa = True
        self.log = open("sesiones.log", "a")  # recurso real
        self.log.write(f"{datetime.now()} - Sesión iniciada: {self.usuario}\n")
        print(f"[INIT] Sesión iniciada para {self.usuario}")

    def registrar_actividad(self, actividad):
        if self.activa:
            self.log.write(f"{datetime.now()} - {self.usuario}: {actividad}\n")
            print(f"[ACTIVIDAD] {actividad}")

    def __del__(self):
        """
        Destructor (__del__):
        - Registra el cierre de la sesión
        - Cierra el archivo de log
        - Libera el recurso del sistema
        """
        if self.activa:
            self.log.write(f"{datetime.now()} - Sesión cerrada: {self.usuario}\n")
            self.activa = False
        self.log.close()
        print(f"[DEL] Sesión cerrada y recurso liberado para {self.usuario}")