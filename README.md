# 2526-POO-S7-ANA-PANCHI
Segundo "B" PROGRAMACION ORIENTADA A OBJETOS-SEMANA7

# Proyecto Sesiones de Usuario en Python

## Descripción del Programa
Este proyecto esta enfocado en el uso de constructores (__init__) y destructores (__del__).  

El programa simula un sistema sencillo de Gestión de sesiones de usuario, donde se registran 
acciones realizadas durante la sesión y se evidencia cuándo se inicia y cierra una sesión.

### Objetivos
- Demostrar cómo se inicializan los atributos de un objeto usando __init__.
- Mostrar cómo __del__ puede utilizarse para realizar tareas de limpieza o liberar recursos al eliminar un objeto.
- Organizar el código en capas: modelos, servicios y punto de entrada (main.py).

### Explicación de cada componente

1. modelos/sesion_usuario.py  
   Contiene la clase `SesionUsuario`, que representa una sesión de usuario.  
   - Constructor (`__init__`)**: Se ejecuta al crear un objeto e inicializa:
     - `usuario`: nombre del usuario.
     - `inicio`: fecha y hora de inicio de sesión.  
     También imprime en consola que la sesión ha iniciado.  
   - Destructor (`__del__`): Se ejecuta cuando el objeto se elimina o cuando el programa termina.  
     Imprime en consola que la sesión ha cerrado, simulando la liberación de recursos.

2. servicios/gestor_sesiones.py  
   Contiene la clase `GestorSesiones`, responsable de gestionar la lógica del sistema:  
   - `iniciar_sesion(usuario)`: crea un objeto `SesionUsuario`, ejecutando su constructor.  
   - `realizar_acciones(sesion)`: simula acciones que realiza el usuario durante la sesión.

3. main.py  
   Punto de entrada que muestra el flujo principal del programa:  
   - Se crea una instancia de `GestorSesiones`.
   - Se inicia una sesión para un usuario (ejecuta `__init__`).
   - Se registran acciones simuladas del usuario.
   - Se elimina el objeto de sesión usando `del`, ejecutando `__del__`.
