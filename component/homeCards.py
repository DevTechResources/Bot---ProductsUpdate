import customtkinter as ctk
from component.card import Card

class HomeCards(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.configure(fg_color="transparent")

        # Añadir frames al grid 
        ctk.CTkFrame(self, fg_color="purple", corner_radius=0).grid(row=0, column=0, sticky='w'+'e'+'n'+'s')
        #Right margin with padx using comma
        Card(self).grid(row=0, column=1, sticky='w'+'e'+'n'+'s', padx=(0,22))
        ctk.CTkFrame(self, fg_color="purple", corner_radius=0).grid(row=0, column=2, sticky='w'+'e'+'n'+'s')
        ctk.CTkFrame(self, fg_color="purple", corner_radius=0).grid(row=0, column=3, sticky='w'+'e'+'n'+'s')
        

        # Configurar las columnas para que crezcan proporcionalmente 
        self.grid_columnconfigure(list(range(4)), weight = 1, uniform="Silent_Creme")

        # Configurar las filas para que crezcan proporcionalmente 
        self.grid_rowconfigure(0, weight=1)

        