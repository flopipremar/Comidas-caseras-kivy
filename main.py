from kivy.app import App
from kivy.uix.screenmanager import ScreenManager

from database import BaseDatos
from screens.menu_screen import MenuScreen
from screens.clientes_screen import ClientesScreen
from screens.productos_screen import ProductosScreen
from screens.gastos_screen import GastosScreen
from screens.ventas_screen import VentasScreen

class ComidaApp(App):
    def build(self):
        # Crear la base de datos
        db = BaseDatos()
        db.crear_base_de_datos()

        # Crear las pantallas
        menu_screen = MenuScreen(name='menu')
        ventas_screen = VentasScreen(name='ventas')
        clientes_screen = ClientesScreen(ventas_screen=ventas_screen, name='clientes')
        productos_screen = ProductosScreen(ventas_screen=ventas_screen, name='productos')
        gastos_screen = GastosScreen(name='gastos')

        # Crear el ScreenManager
        screen_manager = ScreenManager()
        screen_manager.add_widget(menu_screen)
        screen_manager.add_widget(clientes_screen)
        screen_manager.add_widget(productos_screen)
        screen_manager.add_widget(gastos_screen)

        ventas_screen.clientes = clientes_screen.clientes
        ventas_screen.productos = productos_screen.productos
        screen_manager.add_widget(ventas_screen)

        return screen_manager

if __name__ == '__main__':
    ComidaApp().run()
