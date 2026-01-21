from servicios.gestor_sesiones import GestorSesiones

def main():
    gestor = GestorSesiones()
    sesion = gestor.iniciar_sesion("AnaPanchi")
    gestor.usar_sesion(sesion)
    del sesion  # fuerza el destructor

if __name__ == "__main__":
    main()