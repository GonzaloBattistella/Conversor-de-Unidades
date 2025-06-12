import tkinter as tk
from tkinter import ttk
from pathlib import Path
from Levels import length_level

#Funcion para mostrar el frame correspondiente.
def show_frame(option):
  #Ocultar el frame principal.
  frame.pack_forget()

  #Cierro los demas frames
  for widget in root.winfo_children():
    if isinstance(widget, ttk.Frame):
      widget.pack_forget()

  match option:
    case "longitud":
      length_level.open_frame_length(root)

#Creo el Root
root = tk.Tk()
root.title("Units Conversor")

#Defino el alto y ancho de la ventana.
root.geometry("500x400")


frame = ttk.Frame(root, padding=10, relief="flat")
frame.pack(fill="x") 

ttk.Label(frame, text= "¿Que unidad quieres convertir?", font=("Arial", 16, "bold italic"), foreground="#00c16c").pack(pady=10)
ttk.Label(frame, text="Elige el tipo de Conversión", font=("Arial", 14, "bold italic"), foreground="#00c16c").pack(pady=10)

#Obtengo los nombres de los tipos de conversiones.
folder = Path("Conversiones")
names_types = [archivo.stem for archivo in folder.iterdir() if archivo.suffix == ".py" and archivo.name != "__init__.py"]

#Creo ttk.style para combobox


#Creo combobox (lista de opciones) con los nombres de los tipos de conversiones.
combobox = ttk.Combobox(frame, values = names_types, state= "readonly")
combobox.pack(pady= 20)
combobox.set("Seleccione una Opcion")

#Creo ttk.style para el boton "seleccionar".
button_style = ttk.Style()
button_style.configure("Selection.TButtton",
                font = ("Arial", 12, "bold"),
                padding = 10,
                borderwidth = 5,
                foreground = [("disabled", "#3a415a")])

button_style.map("selection.TButton", 
          background = [("pressed", "#fe5412")])


#Creo boton para obtener la opcion seleccionada.
boton = ttk.Button(frame, text="Seleccionar",style="selection.TButton",command= lambda: show_frame(combobox.get()))
boton.pack(pady=20)



root.mainloop()