import customtkinter as ckt
from PIL import Image

class App(ckt.CTk):
    def __init__(self):
        super().__init__()
        screenWidth = self.winfo_screenwidth()
        screenHeight = self.winfo_screenheight()
        self.geometry(f"{screenWidth}x{screenHeight}+0+0")
        self.title("CTk example")

    
        # add widgets to app
        frame = ckt.CTkFrame(self, fg_color="blue")
        frame.pack(side="top",fill="x")

        my_image = ckt.CTkImage(light_image=Image.open("images\TechResourcesBanner.webp"), size=(70,70))

        label1 = ckt.CTkLabel(frame, image=my_image, text="")
        label1.grid(row=0, column=0)
        
        
        frame2 = ckt.CTkFrame(self, fg_color="red",corner_radius=0)
        frame2.pack(expand=True, fill = "both")


app = App()
app.mainloop()