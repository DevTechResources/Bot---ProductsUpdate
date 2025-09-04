import customtkinter as ctk
from component.card import Card
from PIL import Image

class HomeCards(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master, fg_color="transparent")

        # Añadir frames al grid 
        ctk.CTkFrame(self, fg_color="transparent", corner_radius=0).grid(row=0, column=0, sticky='w'+'e'+'n'+'s')

        Card(
            self,
            "images/modificarCategoria.png",
            "Actualizar categoría",
            "Modificar las categorías de"
            "\n“Nuevo Stock”, “Liquidacion” y"
            "\n“OpenBox” de productos en\ntienda.",
            "compras"
            ).grid(row=0, column=1, sticky='w'+'e'+'n'+'s', padx=(0,17))

        Card(
            self,
            "images/cambiarNombre.png",
            "Cambiar nombre",
            "Modificar los nombres de los"
            "\nproductos en tienda para"
            "\nincluir la marca.",
            "compras"
            ).grid(row=0, column=2, sticky='w'+'e'+'n'+'s', padx=(22,0))

        ctk.CTkFrame(self, fg_color="transparent", corner_radius=0).grid(row=0, column=3, sticky='w'+'e'+'n'+'s')
        

        # Configurar las columnas para que crezcan proporcionalmente 
        self.grid_columnconfigure(list(range(4)), weight = 1, uniform="Silent_Creme")

        # Configurar las filas para que crezcan proporcionalmente 
        self.grid_rowconfigure(0, weight=1)