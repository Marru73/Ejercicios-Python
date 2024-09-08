import tkinter as tk

ventana = tk.Tk()
ventana.title("Ejemplo de Place")
ventana.geometry("600x400")



label1 = tk.Label(ventana, text="Label 1")
label1.place(x=50, y=50)

label2 = tk.Label(ventana, text="Label 2")
label2.place(x=100, y=100)

"""
También se pueden poner con porcentajes:

label1 = tk.Label(ventana, text="Label 1")
label1.place(relx=0.25, rely=0.25)

label2 = tk.Label(ventana, text="Label 2")
label2.place(relx=0.75, rely=0.75)

    """

ventana.mainloop()