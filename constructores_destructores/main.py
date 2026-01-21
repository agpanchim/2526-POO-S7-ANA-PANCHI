from servicios.gestor_sesiones import GestorSesiones

def mostrar_titulo():
    print()
    print("   SISTEMA DE GESTIÓN DE SESIONES")
    print()

def main():
    mostrar_titulo()

    print("--- INICIO DEL PROGRAMA ---\n")

    gestor = GestorSesiones()

    # Ejecuta __init__
    sesion = gestor.iniciar_sesion("AnaPanchi")

    gestor.realizar_acciones(sesion)

    # Ejecuta __del__
    del sesion

    print("\n--- FIN DEL PROGRAMA ---")

if __name__ == "__main__":
    main()
