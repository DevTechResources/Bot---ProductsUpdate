import customtkinter as ctk
import style.colors as colors
from component.pageChangerButtons import PageChangerButtons

class UploadPage(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.configure(fg_color=colors.CompanyColor3, corner_radius=0)

        #Frame del título
        frameTitle = ctk.CTkFrame(self, fg_color="pink")
        ctk.CTkLabel(
            frameTitle,
            text = "Actualizar categorías",
            font = ("Roboto", 32, "bold"),
            text_color = "black"
            ).pack()
        frameTitle.pack(side="top", fill="x", pady=(30,22))

        #Frame de la parte de botones
        PageChangerButtons(self,"Atrás", "Confirmar","HomePage","HomePage").pack(side="bottom", fill="x", pady=(22,20), padx=(30,20))

        #Frame de las tarjetas
        frameCards = ctk.CTkFrame(self, fg_color="green")
        frameCards.pack(fill="both", expand=True, padx=(30,30))

        frameFileUpload = ctk.CTkFrame(frameCards, fg_color = "red", corner_radius = 28).pack(side = "top", fill="both", expand = True)
        frameTitle = ctk.CTkFrame(frameFileUpload, fg_color = "purple").pack(side = "top")
        ctk.CTk

        ctk.CTkFrame(frameCards, fg_color = "green", corner_radius = 28).pack(side = "bottom", fill="both", expand = True)

        

        