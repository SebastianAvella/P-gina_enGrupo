import ttkbootstrap as ttk

def view_dashboard(container, manage_views):
    #Bucle widget
    for widget in container.winfo_children():
        widget.destroy()
    #selfs
    container_dashboard = ttk.Frame(container, padding=20, relief="solid",borderwidth=2)
    container_dashboard.pack(fill="both", expand=True)
    ttk.Label(container_dashboard, text="Bienvenido al Dashboard").pack(pady=20)
    ttk.Button(container_dashboard, text="Adivinar el número", command=lambda: manage_views("adivinar")).pack(pady=10)