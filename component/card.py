import customtkinter as ctk

class Card(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.configure(fg_color="transparent")

        # Añadir elementos a la card
        ctk.CTkLabel(self, corner_radius=1.5, text="hola", text_color="black").grid(row=0, column=0, sticky='w'+'e'+'n'+'s') 
        ctk.CTkLabel(self, corner_radius=1.5, text="bye", text_color="black").grid(row=1, column=0, sticky='w'+'e'+'n'+'s') 
        ctk.CTkLabel(self, corner_radius=1.5, text="asdgbefcyhuwbeuycfweybcfweyfyvsevfr", text_color="black").grid(row=2, column=0, sticky='w'+'e'+'n'+'s') 
        ctk.CTkButton(self, corner_radius=1.5).grid(row=3, column=0, sticky='w'+'e'+'n'+'s') 
        
        # Configurar las filas para que crezcan proporcionalmente 
        self.grid_rowconfigure(list(range(4)), weight = 1, uniform="Silent_Creme")

        # Configurar las columnas para que crezcan proporcionalmente 
        self.grid_columnconfigure(0, weight=1)