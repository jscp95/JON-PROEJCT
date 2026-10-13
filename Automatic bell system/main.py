import customtkinter as ctk
from frontend.schedule_page import SchedulePage

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


class BellApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Automatic School Bell System")
        self.geometry("1150x650")
        self.minsize(1000, 600)

        self.schedule_page = SchedulePage(self)
        self.schedule_page.pack(fill="both", expand=True)


if __name__ == "__main__":
    app = BellApp()
    app.mainloop()
