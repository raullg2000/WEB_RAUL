# Proyecto Final: Críticas de Cine - Raúl L.G.

Aplicación web desarrollada con Python (Flask) y MySQL para la gestión de reseñas cinematográficas. Permite a los usuarios registrarse, iniciar sesión y compartir opiniones sobre una selección de películas clásicas.

## 🚀 Requisitos del Sistema
* Python 3.12 (Entorno WSL2 - Ubuntu).
* XAMPP (Servidor MySQL en Windows).
* Librerías necesarias: flask, mysql-connector-python, werkzeug.

## 🛠️ Configuración de la Base de Datos
1. Crear una base de datos llamada "web_raul" en phpMyAdmin.
2. Importar el archivo "web_raul.sql" adjunto en este repositorio.
3. Conectividad: El archivo app.py está configurado para conectar con el host de Windows desde WSL2 mediante la IP 172.27.192.1.

## 📋 Funcionalidades
- Parte Pública: Catálogo de películas, detalles y visualización de las últimas reseñas.
- Parte Privada: Dashboard personal para usuarios registrados donde pueden crear y borrar sus propias críticas.
- Seguridad: Cifrado de contraseñas y manejo de sesiones.
- About Me: Portafolio con enlaces a los ejercicios realizados durante el curso.

## 📁 Estructura
- app.py: Servidor Flask y lógica de conexión.
- templates/: Vistas HTML con herencia de plantillas.
- static/: Estilos CSS y diseño.
- web_raul.sql: Script de base de datos con estructura y datos de prueba.

Autor: Raúl L.G. - Aplicacions Web 2026