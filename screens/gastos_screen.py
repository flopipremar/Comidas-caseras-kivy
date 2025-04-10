from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.uix.spinner import Spinner

class GastosScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.gastos_personales = []
        self.gastos_produccion = []

        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)

        self.tipo_spinner = Spinner(
            text="Seleccione tipo",
            values=["Personal", "Producción"],
            size_hint=(1, 0.1),
        )
        layout.add_widget(self.tipo_spinner)

        self.descripcion_input = TextInput(hint_text="Descripción del gasto", multiline=False, size_hint=(1, None), height=40)
        layout.add_widget(self.descripcion_input)

        self.monto_input = TextInput(hint_text="Monto del gasto", multiline=False, size_hint=(1, None), height=40)
        layout.add_widget(self.monto_input)

        save_button = Button(text="Guardar Gasto", size_hint=(1, None), height=50, background_color=(0.643, 0.518, 0.357, 1))
        save_button.bind(on_press=self.guardar_gasto)
        layout.add_widget(save_button)

        self.gastos_label = Label(text="Gastos Guardados:", size_hint=(1, None), height=30)
        layout.add_widget(self.gastos_label)

        self.lista_gastos = Label(text="", size_hint_y=None, height=300)
        scroll_view = ScrollView(do_scroll_x=False, do_scroll_y=True)
        scroll_view.add_widget(self.lista_gastos)
        layout.add_widget(scroll_view)

        back_button = Button(text="Volver al Menú", size_hint=(1, None), height=50, background_color=(0.643, 0.518, 0.357, 1))
        back_button.bind(on_press=self.volver_menu)
        layout.add_widget(back_button)

        self.add_widget(layout)

    def guardar_gasto(self, instance):
        descripcion = self.descripcion_input.text.strip()
        monto = self.monto_input.text.strip()
        tipo = self.tipo_spinner.text

        if descripcion and monto and tipo != "Seleccione tipo":
            try:
                monto = float(monto)
                gasto = (descripcion, monto)

                if tipo == "Personal":
                    self.gastos_personales.append(gasto)
                else:
                    self.gastos_produccion.append(gasto)

                self.descripcion_input.text = ""
                self.monto_input.text = ""
                self.tipo_spinner.text = "Seleccione tipo"

                self.actualizar_listas_gastos()
            except ValueError:
                print("Error: El monto debe ser un número válido.")
        else:
            print("Por favor, completa todos los campos correctamente.")

    def actualizar_listas_gastos(self):
        texto = "[PERSONAL]\n" + "\n".join([f"{d}: ${m:.2f}" for d, m in self.gastos_personales])
        texto += "\n\n[PRODUCCIÓN]\n" + "\n".join([f"{d}: ${m:.2f}" for d, m in self.gastos_produccion])
        self.lista_gastos.text = texto

    def volver_menu(self, instance):
        self.manager.current = 'menu'