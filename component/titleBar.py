import customtkinter as ctk
from PIL import Image

class TitleBar(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        companyColorBlack = "#1C1C1C"
        self.configure(fg_color=companyColorBlack, corner_radius=0)

        my_image = ctk.CTkImage(light_image=Image.open("images/TechResourcesBanner.webp"), size=(299.37, 51))

        label1 = ctk.CTkLabel(self, image=my_image, text="")
        label1.pack(fill="x", expand=True, ipady=15)