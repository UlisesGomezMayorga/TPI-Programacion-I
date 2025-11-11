# TPI-Programacion-I   

Descripción
Este proyecto implementa un sistema en python para gestionar información sobre países. Permite leer y escribir datos en un archivo CSV, aplicar filtros, ordenamientos y generar estadísticas


Funcionalidades:

Agregar un país con validación de datos.
Actualizar población y superficie.
Buscar países por nombre (coincidencia parcial).
Filtrar por:Continente
Rango de población
Rango de superficie
Ordenar por:Nombre
Población
Superficie (ascendente/descendente)
Mostrar estadísticas:País con mayor y menor población
Promedio de población y superficie
Cantidad de países por continente
Lectura y escritura en archivo CSV.


Estructura del proyecto
-tpi_paises.py        Código principal
- paises.csv            Dataset base
- README.md             Documentación
- capturas/             Imágenes del programa en ejecución




 Cómo ejecutar

Clonar el repositorio:
git clone https://github.com/UlisesGomezMayorga/TPI-Programacion-I.git
   cd tpi_paises



Ejecutar el programa:
python tpi_paises.py




 Formato del CSV
nombre,poblacion,superficie,continente
Argentina,45376763,2780400,América
Japón,125800000,377975,Asia
Brasil,213993437,8515767,América
Alemania,83149300,357022,Europa




 Ejemplo de uso
---Menú de Gestión de Países
1. Agregar un país
2. Actualizar población/superficie
3. Buscar país por nombre
4. Filtrar países
5. Ordenar países
6. Mostrar estadísticas
7. Mostrar todos los países
8. Guardar y salir
0. Salir sin guardar


 Capturas
Hay capturas de pantalla en la carpeta imagenes/ mostrando el menu principal y las diferentes opciones.


 Ejemplo de entrada y salida
Entrada:
Agregar país:
Nombre: Chile
Población: 19116209
Superficie: 756102
Continente: América


Salida:
País 'Chile' agregado correctamente.




 Instalación de dependencias
Este proyecto no requiere librerías externas. Solo necesitas python


 Mejoras futuras

Implementar opción para eliminar países.
Exportar estadísticas a archivo CSV.
Añadir interfaz gráfica (GUI).


 Integrantes

GOMEZ MAYORGA ULISES
GARAY ROCIO
