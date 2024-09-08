import tkinter as tk

ventana = tk.Tk()

ventana.title("Mi primera ventana")
ventana.geometry("600x400") #Tamaño de la ventana.
ventana.minsize(400, 200) # Mínimo que se puede reducir la ventana.
ventana.maxsize(800, 600) # Máximo que se puede ampliar la ventana.
# ventana.iconbtmap("nombre_icono.ico") esto es para ponerle un icono a la ventana.
ventana.configure(bg="lightblue") # Color del fondo de la ventana.
# ventana.resizable(False, False) Esto es para bloquear la ventana. El primer atributo sería la coordenada X y el segundo la coordenada Y.
ventana.attributes("-alpha", 0.8) # Esta es la opacidad que le puedes dar a la ventana. Cero sería completamente transparente y 1 completamente opaca.





ventana.mainloop()
