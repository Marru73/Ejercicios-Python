""" 
Esto sería un ejemplo de pack: 

import tkinter as tk

ventana = tk.Tk()
ventana.title("Ejemplo de Pack")
ventana.geometry("600x400")



label1 = tk.Label(ventana, text="Label 1")
label1.pack()

label2 = tk.Label(ventana, text="Label 2")
label2.pack()

ventana.mainloop()  

    """

# Este es otro ejemplo más avanzado:

import tkinter as tk

ventana = tk.Tk()
ventana.title("Ejemplo de Pack")
ventana.geometry("600x400")

frame_botones = tk.Frame(ventana)
frame_botones.pack(pady=10)

boton1 = tk.Button(frame_botones,text="Botón 1" )
boton1.pack(side="left", padx=5)

boton2 = tk.Button(frame_botones,text="Botón 2" )
boton2.pack(side="left", padx=5)

boton3 = tk.Button(frame_botones,text="Botón 3" )
boton3.pack(side="left", padx=5)

ventana.mainloop()

