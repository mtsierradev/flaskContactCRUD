from app import create_app

# haciendo uso del patron factory Method realizamos la creacion de la app desde 
# una fabrica en este caso otro archivo y no desde app.py

flask_app = create_app()

if __name__ == '__main__':
     flask_app.run(debug=True)