import customtkinter as ctk
import pywinstyles

class CustomCTkButton(ctk.CTkFrame):
    def __init__(self, parent, shadow_color='#d1cfcf', **kwargs):
        super().__init__(parent, fg_color='transparent')
        self.shadow = ctk.CTkFrame(self, fg_color=shadow_color)
        self.button = ctk.CTkButton(self, **kwargs)
        self.button.grid(column=0, row=0, pady=(0,10), padx=(0,10))
        h = self.button.cget('height')
        w = self.button.cget('width')
        cr = self.button.cget('corner_radius')
        self.shadow.configure(height = h, width = w, corner_radius = cr)
        self.shadow.grid(column=0, row=0)
        self.button.lift()
        pywinstyles.set_opacity(self.button, color=self.button.cget("bg_color"))