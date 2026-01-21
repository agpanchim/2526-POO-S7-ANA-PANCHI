from modelos.sesion_usuario import SesionUsuario


class GestorSesiones:
    """
    Servicio que gestiona las sesiones de usuario.
    """

    def iniciar_sesion(self, usuario: str) -> SesionUsuario:
        return SesionUsuario(usuario)

    def realizar_acciones(self, sesion: SesionUsuario):
        sesion.registrar_accion("Acceder al sistema")
        sesion.registrar_accion("Consultar datos")