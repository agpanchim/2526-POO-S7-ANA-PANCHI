# 2526-POO-S7-ANA-PANCHI
Segundo "B" PROGRAMACION ORIENTADA A OBJETOS-SEMANA7
Semana 7: Constructores y Destructores en Python  

## Proyecto: Sesiones de Usuario en Python

## Descripción del Programa
Este proyecto está enfocado en el uso de **constructores (`__init__`)** y **destructores (`__del__`)** en Python, aplicando el paradigma de **Programación Orientada a Objetos (POO)** y una arquitectura organizada por capas.

El programa simula un sistema sencillo de **gestión de sesiones de usuario**, donde se registran las acciones realizadas durante la sesión y se evidencia claramente cuándo una sesión inicia y cuándo finaliza.

## Objetivos
- Demostrar cómo se inicializan los atributos de un objeto usando el constructor `__init__`.
- Mostrar cómo el destructor `__del__` puede utilizarse para realizar tareas de limpieza o cierre lógico de recursos.
- Organizar el código en capas: **modelos**, **servicios** y **punto de entrada (`main.py`)**,

## Explicación del programa

### 1. modelos/sesion_usuario.py
Contiene la clase `SesionUsuario`, que representa una sesión de usuario.

- **Constructor (`__init__`)**:
  - Se ejecuta al crear un objeto.
  - Inicializa:
    - `usuario`: nombre del usuario.
    - `inicio`: fecha y hora de inicio de sesión.
  - Registra el inicio de la sesión tanto en consola como en el archivo `sesion.log`.

- **Destructor (`__del__`)**:
  - Se ejecuta cuando el objeto se elimina o cuando el programa finaliza.
  - Registra el cierre de la sesión en consola y en el archivo `sesion.log`, simulando la liberación de recursos.

### 2. servicios/gestor_sesiones.py
Contiene la clase `GestorSesiones`, responsable de la lógica del sistema.

- `iniciar_sesion(usuario)`: crea un objeto `SesionUsuario`, ejecutando su constructor.
- `realizar_acciones(sesion)`: simula acciones que el usuario realiza durante la sesión.

### 3. main.py
Es el punto de entrada del programa.

- Muestra un título y separadores para una mejor visualización.
- Crea una instancia de `GestorSesiones`.
- Inicia una sesión de usuario (ejecuta `__init__`).
- Registra acciones durante la sesión.
- Elimina el objeto de sesión usando `del`, ejecutando el destructor `__del__`.


## Archivo de Registro (sesion.log)
Al ejecutar el programa se genera automáticamente el archivo **`sesion.log`**, donde se registran:

- Inicio de la sesión (constructor `__init__`)
- Acciones realizadas
- Cierre de la sesión (destructor `__del__`)

Este archivo sirve como evidencia de la ejecución correcta del programa.