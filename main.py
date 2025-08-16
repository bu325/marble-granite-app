from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager
from core.theme import setup_theme
from core.screens.main_screen import MainScreen
from core.screens.inventory_screen import InventoryScreen
from core.screens.clients_screen import ClientsScreen
from core.screens.invoices_screen import InvoicesScreen
from core.services.db import initialize_db

class MarbleGraniteApp(MDApp):
    def build(self):
        # Setup theme
        setup_theme(self)
        
        # Initialize database
        initialize_db()
        
        # Create screen manager
        sm = ScreenManager()
        
        # Add screens
        sm.add_widget(MainScreen())
        sm.add_widget(InventoryScreen())
        sm.add_widget(ClientsScreen())
        sm.add_widget(InvoicesScreen())
        
        return sm

if __name__ == '__main__':
    MarbleGraniteApp().run()


