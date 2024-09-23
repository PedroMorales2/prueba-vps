from flask import Flask, render_template, session, redirect, url_for, request, flash
import controladores.controlador_usuario as cu

app = Flask(__name__)

@app.route('/')
def hello_world():
    # Si el usuario está en sesión, pasa el username a la plantilla
    username = session.get('username')
    return render_template('index.html', name=username)

@app.route('/home')
def home():
    if 'username' in session:
        return render_template('home.html', name=session['username'])
    return redirect(url_for('hello_world'))  # Redirige a la página de inicio si no está logueado

@app.route('/login', methods=['POST'])
def login():
    nombre = request.form['nombre']
    contrasena = request.form['contrasena']
    usuario = cu.login(nombre, contrasena)
    if usuario:
        session['username'] = usuario['nombre']  # Guarda el nombre de usuario en la sesión
        return redirect(url_for('home'))
    else:
        flash('Credenciales incorrectas. Inténtalo de nuevo.')
        return render_template('index.html')
    
@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('hello_world'))

if __name__ == '__main__':
    app.secret_key = 'super'  # Asegúrate de cambiar esta clave en producción
    app.run(debug=True)
