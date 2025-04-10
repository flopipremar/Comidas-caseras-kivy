from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.uix.spinner import Spinner
from database import BaseDatos

class VentasScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.db = BaseDatos()
        self.clientes = []
        self.productos = []
        self.ventas = []

        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)

        self.cliente_spinner = Spinner(
            text="Seleccionar Cliente",
            values=[],
            size_hint=(1, None),
            height=40
        )
        layout.add_widget(self.cliente_spinner)

        self.producto_spinner = Spinner(
            text="Seleccionar Producto",
            values=[],
            size_hint=(1, None),
            height=40
        )
        layout.add_widget(self.producto_spinner)

        self.cantidad_input = TextInput(
            hint_text="Cantidad vendida",
            multiline=False,
            size_hint=(1, None),
            height=40
        )
        layout.add_widget(self.cantidad_input)

        self.ventas_label = Label(text="Ventas Guardadas:", size_hint=(1, None), height=30)
        layout.add_widget(self.ventas_label)

        self.lista_ventas = Label(text="", size_hint_y=None, height=300)
        scroll_view = ScrollView(do_scroll_x=False, do_scroll_y=True)
        scroll_view.add_widget(self.lista_ventas)
        layout.add_widget(scroll_view)

        save_button = Button(
            text="Guardar Venta",
            size_hint=(1, None),
            height=50,
            background_color=(0.643, 0.518, 0.357, 1)
        )
        save_button.bind(on_press=self.guardar_venta)
        layout.add_widget(save_button)

        back_button = Button(
            text="Volver al Menú",
            size_hint=(1, None),
            height=50,
            background_color=(0.643, 0.518, 0.357, 1)
        )
        back_button.bind(on_press=self.volver_menu)
        layout.add_widget(back_button)

        self.add_widget(layout)

    def actualizar_spinners(self):
        clientes = self.db.obtener_clientes()
        productos = self.db.obtener_productos()

        self.cliente_spinner.values = [c[1] for c in clientes if len(c) > 1]
        self.producto_spinner.values = [p[1] for p in productos if len(p) > 1]

    def guardar_venta(self, instance):
        cliente = self.cliente_spinner.text
        producto = self.producto_spinner.text
        cantidad = self.cantidad_input.text

        if cliente == "Seleccionar Cliente" or producto == "Seleccionar Producto" or not cantidad.isdigit():
            print("Seleccioná cliente, producto y asegurate que la cantidad sea válida")
            return

        cantidad = int(cantidad)
        self.ventas.append((cliente, producto, cantidad))
        self.db.insertar_venta(cliente, producto, cantidad)
        self.actualizar_lista_ventas()

    def actualizar_lista_ventas(self):
        texto = "\n".join([f"{v[0]} - {v[1]}: {v[2]}" for v in self.ventas])
        self.lista_ventas.text = texto

    def volver_menu(self, instance):
        self.manager.current = "menu"