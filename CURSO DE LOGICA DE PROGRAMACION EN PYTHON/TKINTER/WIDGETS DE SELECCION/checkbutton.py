import tkinter as tk

ventana = tk.Tk()
ventana.title("Ejemplo Checkbutton")

variable_check1 = tk.BooleanVar()
variable_check2 = tk.BooleanVar()

check1 = tk.Checkbutton(ventana, text="Opción 1", variable=variable_check1)
check2 = tk.Checkbutton(ventana, text="Opción 2", variable=variable_check2)


check1.pack()
check2.pack()

ventana.mainloop()