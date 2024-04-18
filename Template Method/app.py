from flask import Flask, render_template
from abc import ABC, abstractmethod

app = Flask(__name__)

# Clase abstracta que define el esqueleto de una página web
class WebPage(ABC):
    def __init__(self, title):
        self.title = title

    # Método plantilla que define la estructura común de la página
    def render(self):
        return render_template('base.html', title=self.title, content=self.get_content())

    # Método abstracto que debe ser implementado por las subclases
    @abstractmethod
    def get_content(self):
        pass

# Subclase concreta que define una página de inicio
class HomePage(WebPage):
    def __init__(self):
        super().__init__("Página de Inicio")

    # Implementación específica para la página de inicio
    def get_content(self):
        return "¡Bienvenido a nuestra página de inicio!"

# Subclase concreta que define una página de contacto
class ContactPage(WebPage):
    def __init__(self):
        super().__init__("Página de Contacto")

    # Implementación específica para la página de contacto
    def get_content(self):
        return "Póngase en contacto con nosotros a través de support@example.com"

# Subclase concreta que define una página de productos
class ProductsPage(WebPage):
    def __init__(self):
        super().__init__("Página de Productos")

    # Implementación específica para la página de productos
    def get_content(self):
        return "Aquí están nuestros últimos productos: Producto A, Producto B, Producto C"

# Rutas para las diferentes páginas
@app.route('/')
def home():
    home_page = HomePage()
    return home_page.render()

@app.route('/contact')
def contact():
    contact_page = ContactPage()
    return contact_page.render()

@app.route('/products')
def products():
    products_page = ProductsPage()
    return products_page.render()

if __name__ == '__main__':
    app.run(debug=True)
