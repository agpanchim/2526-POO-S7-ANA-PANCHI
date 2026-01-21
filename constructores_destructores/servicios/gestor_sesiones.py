from modelos.sesion_usuario import SesionUsuario

class GestorSesiones:

    def iniciar_sesion(self, usuario):
        return SesionUsuario(usuario)

    def usar_sesion(self, sesion):
        sesion.registrar_actividad("Accedió al sistema")
        sesion.registrar_actividad("Consultó datos")