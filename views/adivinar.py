import ttkbootstrap as ttk

def view_adivinar(container, manage_views):
    #Bucle widget
    for widget in container.winfo_children():
        widget.destroy()
    #selfs
    container_adivinar = ttk.Frame(container, padding=20)
    container_adivinar.pack(fill="both", expand=True)
    ttk.Label(container_adivinar, text="Adivina el número").pack(pady=20)
    ttk.Button(container_adivinar, text="Volver al menú", command=lambda: manage_views("inicio")).pack(pady=10)