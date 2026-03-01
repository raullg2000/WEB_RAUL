# Proyecto Final: Críticas de Cine - Raúl L.G.

Aplicación web desarrollada con Python (Flask) y MySQL para la gestión de reseñas de cine. Permite a los usuarios interactuar con un catálogo de películas y gestionar sus propias opiniones de forma privada.

## Requisitos del Sistema
* Python 3.12 (WSL2 - Ubuntu).
* XAMPP (Servidor MySQL en Windows).
* Librerías: flask, mysql-connector-python, werkzeug.

## Configuración de la Base de Datos
1. Crear base de datos "web_raul" en phpMyAdmin.
2. Importar el archivo "web_raul.sql" incluido.
3. El archivo app.py conecta con MySQL mediante la IP 172.27.192.1 para comunicar WSL con Windows.

## Funcionalidades
* Registro e Inicio de sesión seguro.
* Parte pública con cartelera y últimas reseñas.
* Dashboard privado para crear y borrar reseñas propias.
* Sección "About Me" con portafolio de proyectos anteriores.

## Estructura
* app.py: Lógica y conexión a BD.
* templates/: HTML con herencia de plantillas.
* static/: Estilos CSS.
* web_raul.sql: Base de datos con usuarios y reseñas de prueba.

Autor: Raúl L.G. - Aplicacions Web 2026