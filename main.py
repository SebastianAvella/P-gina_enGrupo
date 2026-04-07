import ttkbootstrap as ttk
from views.dashboar import view_dashboard
from views.adivinar import view_adivinar


VISTAS = {
        "inicio":view_dashboard,
        "adivinar":view_adivinar
    }

class App(ttk.Window):
    

    def __init__(self):
        super().__init__(themename="superhero")

        self.title("prueba")
        self.geometry("800x600")
        self.container = ttk.Frame(self)
        self.container.pack(fill="both", expand=True)
        self.manage_views("inicio")
        self.mainloop()

    def manage_views(self, view_name):
        view_func = VISTAS[view_name]
        view_func(self.container, self.manage_views)
            
if __name__ == "__main__":
    app = App()
        