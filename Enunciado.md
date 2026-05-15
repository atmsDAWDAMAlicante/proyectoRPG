# PROYECTO FINAL  

# Juego de Combate por Turnos con Personajes y Habilidades  

Desarrollar un **juego de combate** por turnos donde el usuario pueda crear personajes, asignarles un tipo predefinido y luchar en combates estratégicos. Cada tipo de personaje debe tener habilidades especiales con recarga de turnos y estadísticas únicas.  

El sistema debe aplicar **POO**: herencia, polimorfismo, encapsulación, constructores y métodos especiales (`__init__`, `__str__`). Además, los personajes y combates deben poder guardarse y cargarse en archivos JSON, con posibilidad de ampliar el proyecto.  

**Este proyecto servirá como examen para evaluar los Resultados de Aprendizaje 3.1 y 3.2. del módulo de Programación Orientada a Objetos de Python.**  


## Definición de Clases Personaje (superclase)  

### Posibles Atributos:  
nombre (*str*), vida (*int*), ataque (*int*), defensa (*int*), habilidad_nombre (*str*),
habilidad_damage (*int*), recarga_maxima (*int*), recarga_actual (*int*)

### Métodos recomendados:  
  ✓ `__init__`  
  ✓ `__str__`  
  ✓ atacar(objetivo)  
  ✓ recibir_daño(cantidad)  
  ✓ usar_habilidad(objetivo)  
  ✓ puede_usar_habilidad()  
  ✓ reducir_recarga()  
  ✓ esta_vivo()  
**Nota:** vida y recarga_actual nunca pueden ser negativas.  


## Tipos de Personaje (Subclases por defecto)  

El juego debe incluir **al menos 5 tipos de personajes** por defecto.  
Ejemplos típicos que no tenéis el por qué seguir, de hecho, es muy aconsejable que sean otros tipos para crear tu propio universo:  

  * Guerrero  
    - Alta vida y defensa  
    - Ataque físico  
    - Habilidad especial: "Golpe Brutal"  
    - Puede tener probabilidad de ataque crítico  

  * Mago  
    - Alto ataque  
    - Baja defensa  
    - Habilidad especial: "Bola de Fuego"  
    - Puede ignorar parte de la defensa del enemigo  

  * Cada subclase:  
    - Cada subclase debe redefinir atributos y comportamiento según corresponda.  
    - Cada subclase deberá:  
      • Heredar de Personaje  
      • Definir sus propios atributos iniciales  
      • Redefinir comportamientos si es necesario (polimorfismo)  

  * Mago  
    - Alto ataque  
    - Baja defensa  
    - Habilidad especial: "Bola de Fuego"  
    - Puede ignorar parte de la defensa del enemigo  

  * Cada subclase  
    - Cada subclase debe redefinir atributos y comportamiento según corresponda.  
    - Cada subclase deberá:  
      • Heredar de Personaje  
      • Definir sus propios atributos iniciales  
      • Redefinir comportamientos si es necesario (polimorfismo)  


## Creación de Personajes  

  * Flujo de creación:  
      1. Introducir nombre del personaje.  
      2. Elegir tipo desde el listado predefinido.  
      3. Sistema instancia automáticamente la clase correspondiente.  
      4. Se asignan estadísticas y habilidades según el tipo.  
  * Todos los atributos sensibles pueden usar **encapsulación** (`__vida`,`__recarga_actual`) con getters y setters.  

## Sistema de Combate:  
- Combate por turnos entre **dos personajes**.  
- Cada turno, el jugador elige:  
        - Ataque normal  
        - Usar habilidad especial (si la recarga lo permite)  
- Después de cada acción:  
        - Se aplicará el daño correspondiente  
        - Se actualizará la recarga de habilidades  
        - Se mostrará el estado actualizado  
- El combate termina cuando uno de los personajes tiene vida ≤ 0.  
- Funciona con polimorfismo: no importa el tipo de personaje.  
- Inclusión de **elementos de azar en el combate**:  
        - Probabilidad de crítico: 10–20% (ataques normales).  
        - Probabilidad de fallo: 5%.  
        - Variación de daño: ±10%.  
        - Efectos de estado opcionales: quemadura, congelado, parálisis. Por ejemplo, congelado pierde el siguiente turno.  
- Habilidades con recarga:  
        - Cada habilidad especial tendrá una recarga definida por recarga_maxima  
        - No podrá utilizarse hasta que la recarga llegue a 0  
        - La recarga disminuirá automáticamente cada turno  


## Guardado y Carga en JSON  
  - Guardar todos los personajes en un archivo JSON.  
  - Cargar personajes previamente guardados y reconstruir su clase correcta usando un campo "tipo".  
  - Crear un módulo específico de persistencia para separar responsabilidades.  
  - Convertir objetos a diccionarios antes de guardar.  
  - Validar que el sistema siga funcionando correctamente tras la carga.  

### Requisitos Técnicos obligatorios de la POO:  
  - Cada clase debe estar en un **archivo independiente** (personaje.py, guerrero.py, mago.py, etc.).  
  - Uso obligatorio de:  
        - **Herencia**  
        - **Polimorfismo**  
        - **Encapsulación**  
        - **Constructores y métodos especiales**  
  - Manejo de excepciones y validaciones (ej: vida > 0).  
  - Diseño preparado para añadir nuevos tipos sin modificar la lógica de combate.  


## Menú principal (mínimo, interactivo y ampliable)  
El sistema debe ofrecer un **menú de opciones** que pueda ser extendido fácilmente:  
  1. **Crear personaje** 
      o Solicita nombre y tipo desde el listado de personajes.  
  2. **Iniciar combate**  
      - Selecciona dos personajes para combatir.  
  3. **Ver personajes existentes**  
      - Lista todos los personajes y sus estadísticas.  
  4. **Guardar personajes en JSON**  
      - Persistir todos los personajes creados.  
  5. **Cargar personajes desde JSON**  
      - Reconstruir correctamente las clases de los personajes.  
  6. **Salir**  

### Nota técnica del menú:  
  - Cada opción del menú debe estar encapsulada en una función separada para facilitar futuras ampliaciones.  
  - El alumno podrá añadir nuevas opciones solo agregando nuevas funciones y entradas en el menú, sin tocar la lógica de combate.  

### Interfaces gráficas:  
  • Crear GUI básica usando **Tkinter**:  
        - Botones para añadir personaje, iniciar combate y ver estadísticas.  
        - Panel de información de vida, nivel, habilidades y efectos activos.  
        - Notificaciones emergentes para críticos y habilidades especiales.  

### Uso de APIs externas  
  - Integración opcional con APIs reales para añadir dinamismo:  
  - Clima que afecta daño de habilidades o similar.  
  - Nombres o temáticas aleatorias.  
  - Descarga dinámica de armas o habilidades.  
  - La API debe estar realmente conectada e integrada en el funcionamiento del juego.  

### Ampliaciones funcionales:  

  - Efectos de estado avanzados  
  - Sistema de experiencia y niveles  
  - Ranking de personajes  
  - Equipos o torneo  
  - Estadísticas avanzadas  
  - Inclusión dinámica de nuevos tipos de personajes  
  - Bonus: Posible ampliación de interfaces gráficas: PyQt, Kivy o Dear PyGui para una apariencia más profesional.  

Como parte de la investigación, se deberá implementar Al menos **una ampliación a elegir: entre Interfaces gráficas y Uso de APIs externas y al menos una del bloque de Ampliaciones funcionales.**  


## Entrega del Proyecto  

- El alumno deberá entregar:  
  - Código fuente completo del proyecto  
  - Archivo JSON generado (si procede)  
  - Documento breve explicativo del funcionamiento y de las ampliaciones implementadas  

**Si el proyecto utiliza librerías externas, deberá incluir obligatoriamente:**  
  - Archivo requirements.txt con todas las dependencias necesarias.