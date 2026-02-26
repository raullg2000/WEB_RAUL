import sqlite3
from flask import Flask, render_template, request, redirect, url_for, session, flash
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = 'tu_clave_secreta_deportiva' # Puedes cambiar esto por cualquier frase

# --- CONFIGURACIÓN DE BASE DE DATOS ---
def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

# --- RUTAS PÚBLICAS ---
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about-me')
def about_me():
    return render_template('about_me.html')

# --- SISTEMA DE USUARIOS ---
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        hashed_pw = generate_password_hash(password)
        
        db = get_db_connection()
        try:
            db.execute('INSERT INTO usuarios (username, password) VALUES (?, ?)', 
                       (username, hashed_pw))
            db.commit()
            flash('¡Registro con éxito! Ya puedes iniciar sesión.')
            return redirect(url_for('login'))
        except sqlite3.IntegrityError:
            flash('Error: El nombre de usuario ya existe.')
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
        
        flash('Usuario o contraseña incorrectos.')
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear()
    flash('Has cerrado sesión.')
    return redirect(url_for('index'))

# --- PARTE PRIVADA (TERCER FORMULARIO Y CONTENIDO) ---

@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    
    db = get_db_connection()
    # Obtenemos los posts creados por este usuario específico
    mis_posts = db.execute('SELECT * FROM posts WHERE autor_id = ?', (session['user_id'],)).fetchall()
    db.close()
    
    return render_template('dashboard.html', username=session['username'], posts=mis_posts)

@app.route('/nuevo-post', methods=['GET', 'POST'])
def nuevo_post():
    # Seguridad: si no hay sesión, al login
    if 'user_id' not in session:
        return redirect(url_for('login'))
    
    if request.method == 'POST':
        titulo = request.form['titulo']
        contenido = request.form['contenido']
        autor_id = session['user_id']
        
        db = get_db_connection()
        db.execute('INSERT INTO posts (titulo, contenido, autor_id) VALUES (?, ?, ?)',
                   (titulo, contenido, autor_id))
        db.commit()
        db.close()
        
        flash('¡Contenido deportivo añadido correctamente!')
        return redirect(url_for('dashboard'))
        
    return render_template('nuevo_post.html')

if __name__ == '__main__':
    app.run(debug=True)
