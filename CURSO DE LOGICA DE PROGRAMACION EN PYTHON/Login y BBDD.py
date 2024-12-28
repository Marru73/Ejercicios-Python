import tkinter as tk
from tkinter import messagebox, ttk
from datetime import datetime
from tkinter.constants import *
import sqlite3  # Añadimos import para SQLite

# Función para crear la base de datos y la tabla
def crear_base_datos():
    try:
        conn = sqlite3.connect('admisiones.db')
        cursor = conn.cursor()
        
        # Crear tabla si no existe
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS admisiones (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                fecha_hora TEXT,
                nombre TEXT,
                apellidos TEXT,
                direccion TEXT,
                email TEXT,
                genero TEXT
            )
        ''')
        
        conn.commit()
        conn.close()
    except Exception as e:
        messagebox.showerror("Error", f"Error al crear la base de datos: {str(e)}")

# Llamar a la función para crear la base de datos al inicio
crear_base_datos()

# Crear ventana principal
root = tk.Tk()
root.title("Sistema de Admisión")
root.geometry("900x650")
root.configure(bg="#f0f0f0")

# Frame principal
main_frame = ttk.Frame(root, padding=20)
main_frame.pack(fill=BOTH, expand=True, padx=20, pady=20)

# Título
title_frame = ttk.Frame(main_frame)
title_frame.pack(fill=X, pady=(0, 20))

title_label = ttk.Label(
    title_frame, 
    text="Formulario de Admisión", 
    font=("Arial", 24, "bold")
)
title_label.pack()

subtitle = ttk.Label(
    title_frame,
    text="Complete todos los campos para registrar su solicitud",
    font=("Arial", 12)
)
subtitle.pack()

# Frame para el formulario
form_frame = ttk.Frame(main_frame)
form_frame.pack(fill=BOTH, expand=True)

# Contenedor para campos personales
personal_frame = ttk.LabelFrame(form_frame, text="Datos Personales", padding=15)
personal_frame.pack(fill=X, pady=10)

# Grid para mejor organización
personal_frame.columnconfigure(1, weight=1)

# Función para crear campos de entrada con estilo
def create_entry_field(parent, label_text, row):
    label = ttk.Label(parent, text=label_text)
    label.grid(row=row, column=0, padx=(0,10), pady=8, sticky=W)
    
    entry = ttk.Entry(parent)
    entry.grid(row=row, column=1, sticky=EW)
    return label, entry

# Crear campos
labels_entries = {
    "nombre": create_entry_field(personal_frame, "Nombre:", 0),
    "apellidos": create_entry_field(personal_frame, "Apellidos:", 1),
    "direccion": create_entry_field(personal_frame, "Dirección:", 2),
    "email": create_entry_field(personal_frame, "E-mail:", 3)
}

# Frame para género
gender_frame = ttk.LabelFrame(form_frame, text="Género", padding=15)
gender_frame.pack(fill=X, pady=10)

variable_control = tk.IntVar()
genders = ["Masculino", "Femenino", "Otro"]

for i, gender in enumerate(genders, 1):
    ttk.Radiobutton(
        gender_frame,
        text=gender,
        variable=variable_control,
        value=i
    ).pack(side=LEFT, padx=20)

def mostrar_seleccion():
    campos_vacios = []
    
    # Validar campos
    for field_name, (label, entry) in labels_entries.items():
        if not entry.get().strip():
            campos_vacios.append(field_name.capitalize())
            label.configure(text=f"{label.cget('text').rstrip(':')} *:")
        else:
            label.configure(text=f"{label.cget('text').rstrip('*:')}")
    
    if variable_control.get() == 0:
        campos_vacios.append("Género")
        gender_frame.configure(text="Género *")
    else:
        gender_frame.configure(text="Género")

    if campos_vacios:
        messagebox.showerror(
            "Campos Requeridos",
            "Por favor complete los siguientes campos:\n\n" + "\n".join(campos_vacios)
        )
        return

    try:
        # Procesar datos
        genero = genders[variable_control.get() - 1]
        fecha_hora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        
        # Preparar datos en mayúsculas
        datos = {
            "fecha_hora": fecha_hora,
            "nombre": labels_entries["nombre"][1].get().upper(),
            "apellidos": labels_entries["apellidos"][1].get().upper(),
            "direccion": labels_entries["direccion"][1].get().upper(),
            "email": labels_entries["email"][1].get().upper(),
            "genero": genero.upper()
        }
        
        # Guardar en la base de datos
        conn = sqlite3.connect('admisiones.db')
        cursor = conn.cursor()
        
        cursor.execute('''
            INSERT INTO admisiones (fecha_hora, nombre, apellidos, direccion, email, genero)
            VALUES (:fecha_hora, :nombre, :apellidos, :direccion, :email, :genero)
        ''', datos)
        
        conn.commit()
        conn.close()
        
        messagebox.showinfo(
            "Registro Exitoso",
            "Los datos se han guardado correctamente en la base de datos"
        )
        
        # Limpiar campos
        for _, entry in labels_entries.values():
            entry.delete(0, END)
        variable_control.set(0)
        
    except Exception as e:
        messagebox.showerror("Error", f"Error al guardar en la base de datos: {str(e)}")

# Función para consultar registros (nueva)
def consultar_registros():
    try:
        conn = sqlite3.connect('admisiones.db')
        cursor = conn.cursor()
        
        cursor.execute('SELECT * FROM admisiones')
        registros = cursor.fetchall()
        
        # Crear nueva ventana para mostrar registros
        ventana_registros = tk.Toplevel(root)
        ventana_registros.title("Registros de Admisión")
        ventana_registros.geometry("800x400")
        
        # Crear Treeview
        tree = ttk.Treeview(ventana_registros)
        tree['columns'] = ('ID', 'Fecha', 'Nombre', 'Apellidos', 'Dirección', 'Email', 'Género')
        
        # Formato de columnas
        tree.column('#0', width=0, stretch=NO)
        tree.column('ID', width=50)
        tree.column('Fecha', width=120)
        tree.column('Nombre', width=100)
        tree.column('Apellidos', width=120)
        tree.column('Dirección', width=150)
        tree.column('Email', width=150)
        tree.column('Género', width=80)
        
        # Encabezados
        tree.heading('ID', text='ID')
        tree.heading('Fecha', text='Fecha y Hora')
        tree.heading('Nombre', text='Nombre')
        tree.heading('Apellidos', text='Apellidos')
        tree.heading('Dirección', text='Dirección')
        tree.heading('Email', text='Email')
        tree.heading('Género', text='Género')
        
        # Insertar datos
        for registro in registros:
            tree.insert('', END, values=registro)
        
        # Agregar scrollbar
        scrollbar = ttk.Scrollbar(ventana_registros, orient=VERTICAL, command=tree.yview)
        tree.configure(yscrollcommand=scrollbar.set)
        
        # Empaquetar elementos
        tree.pack(side=LEFT, fill=BOTH, expand=True)
        scrollbar.pack(side=RIGHT, fill=Y)
        
        conn.close()
        
    except Exception as e:
        messagebox.showerror("Error", f"Error al consultar la base de datos: {str(e)}")

# Botón de guardar
save_button = ttk.Button(
    form_frame,
    text="Guardar Datos",
    command=mostrar_seleccion,
    width=20
)
save_button.pack(pady=20)

# Añadir botón para consultar registros
query_button = ttk.Button(
    form_frame,
    text="Consultar Registros",
    command=consultar_registros,
    width=20
)
query_button.pack(pady=10)

root.mainloop()
