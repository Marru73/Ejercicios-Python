import tkinter as tk

# Código para crear un evento al hacer click con el mouse.

def on_click(evento):
    print("Botón presionado")

ventana = tk.Tk()

button = tk.Button(ventana, text="Haz click aquí")
button.pack()

button.bind("<Button-1>", on_click)



# Código para crear un evento al usar una tecla del teclado.

def on_key_press(event):
    if event.char == "a":
        print("Tecla 'a' pulsada.")

ventana.bind("<KeyPress>", on_key_press)



# Código para redimensionar la ventana.

def on_resize(event):
    print(f"La ventana ha sido redimensionada a {event.width} x {event.height}")

ventana.bind("<Configure>", on_resize)



# Código para obtener las coordenadas del mouse.

def on_mouse_move(event):
    print(f"Ratón movido a {event.x}, {event.y}")

ventana.bind("<Motion>", on_mouse_move)



ventana.mainloop()
