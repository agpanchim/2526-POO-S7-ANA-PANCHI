from servicios.gestor_sesiones import GestorSesiones


def main():
    gestor = GestorSesiones()

    # Se ejecuta __init__
    sesion = gestor.iniciar_sesion("AnaPanchi")

    gestor.realizar_acciones(sesion)

    # Forzamos la ejecución del destructor
    del sesion


if __name__ == "__main__":
    main()
