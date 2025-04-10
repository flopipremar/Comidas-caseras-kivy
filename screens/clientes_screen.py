from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from database import BaseDatos

class ClientesScreen(Screen):
    def __init__(self, ventas_screen, **kwargs):
        super().__init__(**kwargs)
        self.db = BaseDatos()
        self.clientes = []
        self.ventas_screen = ventas_screen

        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)

        self.nombre_input = TextInput(hint_text="Escribe el nombre del cliente", multiline=False, size_hint=(1, None), height=40)
        layout.add_widget(self.nombre_input)

        self.telefono_input = TextInput(hint_text="Escribe el teléfono del cliente", multiline=False, size_hint=(1, None), height=40)
        layout.add_widget(self.telefono_input)

        self.direccion_input = TextInput(hint_text="Escribe la dirección del cliente", multiline=False, size_hint=(1, None), height=40)
        layout.add_widget(self.direccion_input)

        save_button = Button(text="Guardar Cliente", size_hint=(1, None), height=50, background_color=(0.643, 0.518, 0.357, 1))
        save_button.bind(on_press=self.guardar_cliente)
        layout.add_widget(save_button)

        self.clientes_label = Label(text="Clientes Guardados:", size_hint=(1, None), height=30)
        layout.add_widget(self.clientes_label)

        self.lista_clientes = Label(text="", size_hint_y=None, height=300)
        scroll_view = ScrollView(do_scroll_x=False, do_scroll_y=True)
        scroll_view.add_widget(self.lista_clientes)
        layout.add_widget(scroll_view)

        back_button = Button(text='Volver al Menú', size_hint=(1, None), height=50, background_color=(0.643, 0.518, 0.357, 1))
        back_button.bind(on_press=self.volver_menu)
        layout.add_widget(back_button)

        self.add_widget(layout)

    def volver_menu(self, instance):
        self.manager.current = 'menu'

    def guardar_cliente(self, instance):
        nombre = self.nombre_input.text.strip()
        telefono = self.telefono_input.text.strip()
        direccion = self.direccion_input.text.strip()

        if nombre and telefono and direccion:
            cliente = {'nombre': nombre, 'telefono': telefono, 'direccion': direccion}
            self.db.guardar_cliente(cliente)
            self.clientes.append(cliente)

            self.nombre_input.text = ""
            self.telefono_input.text = ""
            self.direccion_input.text = ""

            self.actualizar_lista_clientes()
            self.ventas_screen.actualizar_spinners()
        else:
            print("Por favor, completa todos los campos.")

    def actualizar_lista_clientes(self):
        cliente_text = "\n".join([f"Nombre: {c['nombre']}\nTeléfono: {c['telefono']}\nDirección: {c['direccion']}\n" for c in self.clientes])
        self.lista_clientes.text = cliente_text