import tkinter as tk

ventana = tk.Tk()

ventana.title("Mi primera ventana")
ventana.geometry("600x400")
ventana.configure(bg="lightblue")

labelframe = tk.LabelFrame(ventana, text="Grupo de Widgets", bg="yellow", padx=10, pady=10)
labelframe.configure(width=300, height=200)
labelframe.pack()

ventana.mainloop()