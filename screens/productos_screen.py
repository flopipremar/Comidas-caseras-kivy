from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from database import BaseDatos

class ProductosScreen(Screen):
    def __init__(self, ventas_screen, **kwargs):
        super().__init__(**kwargs)
        self.db = BaseDatos()
        self.productos = []
        self.ventas_screen = ventas_screen

        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)

        self.nombre_input = TextInput(hint_text="Escribe el nombre del producto", multiline=False, size_hint=(1, None), height=40)
        layout.add_widget(self.nombre_input)

        self.precio_input = TextInput(hint_text="Escribe el precio del producto", multiline=False, size_hint=(1, None), height=40)
        layout.add_widget(self.precio_input)

        save_button = Button(text="Guardar Producto", size_hint=(1, None), height=50, background_color=(0.643, 0.518, 0.357, 1))
        save_button.bind(on_press=self.guardar_producto)
        layout.add_widget(save_button)

        self.productos_label = Label(text="Productos Guardados:", size_hint=(1, None), height=30)
        layout.add_widget(self.productos_label)

        self.lista_productos = Label(text="", size_hint_y=None, height=300)
        scroll_view = ScrollView(do_scroll_x=False, do_scroll_y=True)
        scroll_view.add_widget(self.lista_productos)
        layout.add_widget(scroll_view)

        back_button = Button(text='Volver al Menú', size_hint=(1, None), height=50, background_color=(0.643, 0.518, 0.357, 1))
        back_button.bind(on_press=self.volver_menu)
        layout.add_widget(back_button)

        self.add_widget(layout)

    def guardar_producto(self, instance):
        nombre = self.nombre_input.text.strip()
        precio = self.precio_input.text.strip()

        if nombre and precio:
            try:
                precio = float(precio)
                producto = {'nombre': nombre, 'precio': precio}
                self.db.guardar_producto(producto)
                self.productos.append(producto)

                self.nombre_input.text = ""
                self.precio_input.text = ""
                self.actualizar_lista_productos()
                self.ventas_screen.actualizar_spinners()
            except ValueError:
                self.lista_productos.text = "Error: El precio debe ser un número válido."

    def actualizar_lista_productos(self):
        producto_text = "\n".join([f"Nombre: {p['nombre']}\nPrecio: ${p['precio']:.2f}\n" for p in self.productos])
        self.lista_productos.text = producto_text

    def volver_menu(self, instance):
        self.manager.current = 'menu'