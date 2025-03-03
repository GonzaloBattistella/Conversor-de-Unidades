import tkinter as tk
from tkinter import ttk
from pathlib import Path

#Funciones en las que llamo a su level correspondiente.
def choosen_length():
  pass

def choosen_system_numerics():
  pass

def choosen_file_size():
  pass

def choosen_temperature():
  pass

#Opcion para obtener la opcion seleccionada por el usuario.
def obtenerOpcionUser():
  opcion = combobox.get()

  match opcion:
    case "longitud":
      choosen_length()
    case "sistemas_numericos":
      choosen_system_numerics()
    case "tamaño_archivos":
      choosen_file_size()
    case "temperatura":
      choosen_temperature()

#Creo el Root
root = tk.Tk()
root.title("Units Conversor")

#Defino el alto y ancho de la ventana.
root.geometry("500x300")


ttk.Label(root, text= "¿Que unidad quieres convertir?", font=("Arial", 16, "bold italic"), foreground="#00c16c").pack(pady=10)

frame = ttk.Frame(root, padding=10, relief="flat").pack(fill="x")

ttk.Label(frame, text="Elige el tipo de Coversión", font=("Arial", 14, "bold italic"), foreground="#00c16c").pack(pady=10)

#Obtengo los nombres de los tipos de conversiones.
folder = Path("Conversiones")
names_types = [archivo.stem for archivo in folder.iterdir() if archivo.suffix == ".py" and archivo.name != "__init__.py"]

#Creo combobox (lista de opciones) con los nombres de los tipos de conversiones.
combobox = ttk.Combobox(frame, values = names_types, state= "readonly")
combobox.pack(pady= 20)
combobox.set("Seleccione una Opcion")

#Creo boton para obtener la opcion seleccionada.
boton = ttk.Button(frame, text="Seleccionar", command=obtenerOpcionUser())

root.mainloop()