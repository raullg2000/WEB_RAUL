import sqlite3
from flask import Flask, render_template, request, redirect, url_for, session, flash
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = 'hollywood_secret_key'

# Diccionario con la información de las películas
PELICULAS_INFO = {
    'Kill Bill': {
        'titulo': 'Kill Bill: Vol. 1',
        'sinopsis': 'Una novia asesina es traicionada por su propia banda. Tras despertar de un coma, busca venganza contra todos los que la dieron por muerta.',
        'img': 'https://m.media-amazon.com/images/M/MV5BNzM3NDFhYTAtYmU5Mi00NGRmLTljYjgtMDkyODQ4MjNkMGY2XkEyXkFqcGdeQXVyNzkwMjQ5NzM@._V1_.jpg'
    },
    'Regreso al Futuro': {
        'titulo': 'Regreso al Futuro',
        'sinopsis': 'Marty McFly viaja accidentalmente a 1955 en un DeLorean inventado por Doc Brown y debe asegurar que sus padres se enamoren.',
        'img': 'https://m.media-amazon.com/images/M/MV5BZmU0M2Y1OGUtZjIxNi00ZjBkLTg1MjgtOWIyNThiZWIwYjRiXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_.jpg'
    },
    'Pulp Fiction': {
        'titulo': 'Pulp Fiction',
        'sinopsis': 'Vidas de criminales, boxeadores y gánsteres se entrelazan en una serie de incidentes violentos e inesperados en Los Ángeles.',
        'img': 'https://m.media-amazon.com/images/M/MV5BNGNhMDIzZTUtNTBlZi00MTRlLWFjM2ItYzViMjE3YzI5MjI4XkEyXkFqcGdeQXVyNzkwMjQ5NzM@._V1_.jpg'
    },
    'Karate Kid': {
        'titulo': 'The Karate Kid',
        'sinopsis': 'Un adolescente aprende artes marciales de la mano de un sabio maestro japonés para defenderse de unos acosadores.',
        'img': 'https://m.media-amazon.com/images/M/MV5BNTkzY2YzNmYtY2ViMS00MThiLWI5NDItY2NmNjZiNTY3YjVlXkEyXkFqcGdeQXVyNjE5MjUyOTM@._V1_.jpg'
    },
    'El Padrino': {
        'titulo': 'El Padrino',
        'sinopsis': 'La historia de la poderosa familia criminal Corleone y el ascenso de Michael Corleone dentro de la mafia de Nueva York.',
        'img': 'https://m.media-amazon.com/images/M/MV5BM2MyNjYxNmUtYTAwNi00MTYxLWJmNWYtYzZlODY3ZTk3OTFlXkEyXkFqcGdeQXVyNzkwMjQ5NzM@._V1_.jpg'
    },
    'Star Wars': {
        'titulo': 'Star Wars: Episodio IV',
        'sinopsis': 'Luke Skywalker se une a un caballero Jedi para salvar a la galaxia de la estación de combate del Imperio.',
        'img': 'https://m.media-amazon.com/images/I/81P3lDJbjCL._AC_UF1000,1000_QL80_.jpg'
    },
    'Jurassic Park': {
        'titulo': 'Jurassic Park',
        'sinopsis': 'Un multimillonario crea un parque temático con dinosaurios reales, pero un fallo en la seguridad desata el caos absoluto.',
        'img': 'https://m.media-amazon.com/images/M/MV5BMjM2MDgxMDg0Nl5BMl5BanBnXkFtZTgwNTM2OTM5NDE@._V1_.jpg'
    },
    'Terminator': {
        'titulo': 'The Terminator',
        'sinopsis': 'Un cyborg asesino viaja desde el futuro para matar a Sarah Connor, cuyo hijo no nacido será la clave de la resistencia.',
        'img': 'https://m.media-amazon.com/images/M/MV5BYTViYTE3ZGQtNDFmMS00MDZmLTlmY2ItN2RkYTA0OTM2NTcyXkEyXkFqcGdeQXVyNTAyODkwOQ@@._V1_.jpg'
    }
}

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    db = get_db_connection()
    resenas = db.execute('''
        SELECT posts.titulo, posts.contenido, usuarios.username 
        FROM posts JOIN usuarios ON posts.autor_id = usuarios.id 
        ORDER BY posts.id DESC LIMIT 5
    ''').fetchall()
    db.close()
    return render_template('index.html', resenas=resenas)

@app.route('/pelicula/<nombre>')
def detalle_pelicula(nombre):
    info = PELICULAS_INFO.get(nombre)
    if not info:
        return "Película no encontrada", 404
    db = get_db_connection()
    # Buscamos críticas que mencionen el nombre de la peli
    criticas = db.execute('''
        SELECT posts.contenido, usuarios.username 
        FROM posts JOIN usuarios ON posts.autor_id = usuarios.id 
        WHERE posts.titulo LIKE ?
    ''', ('%' + nombre + '%',)).fetchall()
    db.close()
    return render_template('detalle_pelicula.html', peli=info, criticas=criticas)

@app.route('/about-me')
def about_me():
    return render_template('about_me.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = generate_password_hash(request.form['password'])
        db = get_db_connection()
        try:
            db.execute('INSERT INTO usuarios (username, password) VALUES (?, ?)', (username, password))
            db.commit()
            return redirect(url_for('login'))
        except sqlite3.IntegrityError:
            flash('Usuario ya existe.')
        finally:
            db.close()
    return render_template('registro.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db = get_db_connection()
        user = db.execute('SELECT * FROM usuarios WHERE username = ?', (username,)).fetchone()
        db.close()
        if user and check_password_hash(user['password'], password):
            session['user_id'] = user['id']
            session['username'] = user['username']
            return redirect(url_for('dashboard'))
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session: return redirect(url_for('login'))
    db = get_db_connection()
    resenas = db.execute('SELECT * FROM posts WHERE autor_id = ?', (session['user_id'],)).fetchall()
    db.close()
    return render_template('dashboard.html', username=session['username'], posts=resenas)

@app.route('/nueva-resena', methods=['GET', 'POST'])
@app.route('/nueva-resena/<default_title>', methods=['GET', 'POST']) # Nueva ruta con título por defecto
def nuevo_post(default_title=None):
    if 'user_id' not in session:
        flash('Debes iniciar sesión para escribir una reseña.')
        return redirect(url_for('login'))
        
    if request.method == 'POST':
        titulo = request.form['titulo']
        contenido = request.form['contenido']
        db = get_db_connection()
        db.execute('INSERT INTO posts (titulo, contenido, autor_id) VALUES (?, ?, ?)', 
                   (titulo, contenido, session['user_id']))
        db.commit()
        db.close()
        return redirect(url_for('dashboard'))
    
    return render_template('nuevo_post.html', default_title=default_title)

@app.route('/borrar-post/<int:post_id>', methods=['POST'])
def borrar_post(post_id):
    db = get_db_connection()
    db.execute('DELETE FROM posts WHERE id = ?', (post_id,))
    db.commit()
    db.close()
    return redirect(url_for('dashboard'))

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)