🎬 Proyecto Final: Críticas de Cine - Raúl L.G.
Aplicación web desarrollada con Python (Flask) y MySQL para la gestión de reseñas cinematográficas. Este proyecto permite a los usuarios interactuar con un catálogo de películas y gestionar sus propias opiniones de forma privada.

🚀 Requisitos del Sistema
Para ejecutar esta aplicación, se han utilizado las siguientes herramientas:

Python 3.12 (Entorno WSL2 - Ubuntu).

XAMPP v3.3.0 (Servidor MySQL en Windows).

Librerías necesarias: flask, mysql-connector-python, werkzeug.

🛠️ Configuración de la Base de Datos
La base de datos se gestiona a través de phpMyAdmin en XAMPP.

Crear una base de datos llamada web_raul.

Importar el archivo web_raul.sql (incluido en la entrega).

Conectividad: Se ha configurado el archivo app.py para conectar con el host de Windows desde WSL usando la IP 172.27.192.1.

📋 Cumplimiento de Requisitos
Parte Pública: Visualización de reseñas en el Index, detalle de películas y sección "About Me".

Parte Privada: Acceso restringido al Dashboard mediante Login.

Registro de Usuarios: Sistema de registro con almacenamiento en BD y cifrado de contraseñas.

Base de Datos: Integración total con MySQL para usuarios y reseñas.

Formularios: Registro, Login y "Nueva Reseña".

Herencia de Plantillas: Uso de base.html como plantilla maestra.

About Me: Portafolio con enlaces directos a los ejercicios de clase.

📁 Estructura del Proyecto
app.py: Lógica del servidor y conexión MySQL.

templates/: Plantillas HTML con herencia.

static/: Estilos CSS.

web_raul.sql: Script de base de datos con datos de prueba.

👤 Autor
Raúl L.G. - Curso de Aplicacions Web 2026