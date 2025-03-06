import tkinter as tk
from tkinter import ttk

# Función para cambiar de frame
def mostrar_frame(frame):
    frame.tkraise()

# Crear la ventana principal (root)
root = tk.Tk()
root.title("Conversor de Unidades")
root.geometry("500x300")

# Crear los frames
frame_inicio = ttk.Frame(root)
frame_inicio.grid(row=0, column=0, sticky="nsew")

frame_longitud = ttk.Frame(root)
frame_longitud.grid(row=0, column=0, sticky="nsew")

# Agregar widgets al frame de inicio
ttk.Label(frame_inicio, text="Selecciona una opción de conversión", font=("Arial", 14)).pack(pady=10)
boton_longitud = ttk.Button(frame_inicio, text="Conversión de Longitud", command=lambda: mostrar_frame(frame_longitud))
boton_longitud.pack()

# Agregar widgets al frame de longitud
ttk.Label(frame_longitud, text="Conversor de Longitud", font=("Arial", 16, "bold italic")).pack(pady=10)
boton_volver = ttk.Button(frame_longitud, text="Volver", command=lambda: mostrar_frame(frame_inicio))
boton_volver.pack(pady=10)

# Mostrar el frame de inicio por defecto
mostrar_frame(frame_inicio)

# Hacer que la ventana se ajuste al tamaño de los widgets
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

root.mainloop()
