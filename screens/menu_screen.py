from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.graphics import Color, Rectangle

class MenuScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', spacing=10, padding=10)

        with self.canvas.before:
            Color(0.784, 0.710, 0.584, 1)
            self.rect = Rectangle(size=self.size, pos=self.pos)
        self.bind(size=self._update_rect, pos=self._update_rect)

        imagen = Image(source='logo_desde_casa.jpeg', size_hint=(1, 0.3))
        layout.add_widget(imagen)

        layout.add_widget(Button(text='Clientes', background_color=(0.643, 0.518, 0.357, 1), size_hint=(1, None), height=50, on_press=self.cambiar_pantalla_clientes))
        layout.add_widget(Button(text='Productos', background_color=(0.643, 0.518, 0.357, 1), size_hint=(1, None), height=50, on_press=self.cambiar_pantalla_productos))
        layout.add_widget(Button(text='Gastos', background_color=(0.643, 0.518, 0.357, 1), size_hint=(1, None), height=50, on_press=self.cambiar_pantalla_gastos))
        layout.add_widget(Button(text='Ventas', background_color=(0.643, 0.518, 0.357, 1), size_hint=(1, None), height=50, on_press=self.cambiar_pantalla_ventas))

        self.add_widget(layout)

    def _update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size

    def cambiar_pantalla_clientes(self, instance):
        self.manager.current = 'clientes'

    def cambiar_pantalla_productos(self, instance):
        self.manager.current = 'productos'

    def cambiar_pantalla_gastos(self, instance):
        self.manager.current = 'gastos'

    def cambiar_pantalla_ventas(self, instance):
        self.manager.current = 'ventas'