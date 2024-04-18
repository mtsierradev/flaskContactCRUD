from flask import Flask, render_template, request, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_bcrypt import Bcrypt

# from flask_login import UserMixin

# Configuración

db = SQLAlchemy()
migrate = Migrate()


# Modelos


# Crear la aplicación

def create_app():
    app = Flask(__name__, static_folder='static', template_folder='templates')
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./testdb.db'


    app.secret_key = 'mysecretkey'

    db.init_app(app)

    loginManager = LoginManager()
    loginManager.init_app(app)

    from models import User

    @loginManager.user_loader
    def load_user(uid):
        return User.query.get(uid)

    bcrypt = Bcrypt(app)
   

    from routes import register_routes
    register_routes(app,db, bcrypt)


    migrate = Migrate(app, db)
    

    return app


 

# # Datos de usuarios (simulados)
# usuarios = {
#     'user1': 'pwd1',
#     'user2': 'pwd2'
# }

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

# if __name__ == '__main__':
#     app.run(debug=True)
