from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__, static_folder='static')
app.secret_key = 'mysecretkey'

# Datos de usuarios (simulados)
usuarios = {
    'user1': 'pwd1',
    'user2': 'pwd2'
}

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/dashboard/')
def dashboard():
    return render_template('dashboard.html')

# @app.route('/')
# def index():
#     if 'username' in session:
#         return 'Estás logueado como ' + session['username'] + '<br><a href="/logout">Cerrar sesión</a>'
#     return 'No estas logueado <br><a href="/login">Iniciar sesión</a>'

# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         username = request.form['username']
#         password = request.form['password']
#         if username in usuarios and usuarios[username] == password:
#             session['username'] = username
#             return redirect(url_for('index'))
#         else:
#             return 'Credenciales incorrectas. <a href="/login">Intenta de nuevo</a>'
#     return render_template('login.html')

# @app.route('/logout')
# def logout():
#     session.pop('username', None)
#     return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
