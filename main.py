import tkinter as tk
from tkinter import ttk
from pathlib import Path
from Levels import length_level

# ==== Funcion de confirmacion personalizada ====
def confirmar_salida():
  win_confirmation = tk.Toplevel(root)
  win_confirmation.title("Confirmar Salida")
  win_confirmation.geometry("200x100")
  win_confirmation.configure(bg="#6d7581")
  win_confirmation.transient(root) #Para que la ventana este asociada al root
  win_confirmation.grab_set() #Bloquea Interaccion con el root

  #Centrar sobre el root
  win_confirmation.update_idletasks()  # Necesario para calcular tamaño real
  x = root.winfo_x() + (root.winfo_width() // 2) - (win_confirmation.winfo_width() // 2)
  y = root.winfo_y() + (root.winfo_height() // 2) - (win_confirmation.winfo_height() // 2)
  win_confirmation.geometry(f"+{x}+{y}")

  label  = tk.Label(win_confirmation, text="¿Seguro que quieres Salir?", font=("Arial", 8, "bold italic"), bg="#6d7581")
  label.pack(pady=20)

  frame_buttons = tk.Frame(win_confirmation, bg="#6d7581")
  frame_buttons.pack()

  btn_yes = ttk.Button(frame_buttons, text="YES", command=root.destroy)
  btn_yes.pack(side="right", padx=10)

  btn_no = ttk.Button(frame_buttons, text="NO", command=win_confirmation.destroy)
  btn_no.pack(side="left", padx=10)


# ==== Funcion para mostrar el frame correspondiente ====
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

# ==== Creo el Root ====
root = tk.Tk()
root.title("Units Conversor")
root.configure(bg="#6d7581")

#Defino el alto y ancho de la ventana.
root.geometry("500x400")

# Estilos personalizados
style = ttk.Style()
style.configure("Custom.TFrame", background="#6d7581")
style.configure("Header.TLabel", background="#6d7581", foreground="#f2f2f2", font=("Arial", 40, "bold italic"))
style.configure("Custom.TLabel", background="#6d7581", font=("Arial", 12, "italic"))
style.configure("Custom.TButton", font=("Arial", 12, "bold"), padding=6, background="#6d7581")

# ==== Frame Principal con botones y combobox ====
frame = ttk.Frame(root, padding=10, relief="flat", style= "Custom.TFrame")
frame.pack(fill="both", expand= True) 

ttk.Label(frame, text= "¿Que unidad quieres convertir?", font=("Arial", 16, "bold italic"), style="Header.TLabel").pack(pady=10)
ttk.Label(frame, text="Elige el tipo de Conversión", font=("Arial", 14, "bold italic"), style="Header.TLabel").pack(pady=10)

#Obtengo los nombres de los tipos de conversiones.
folder = Path("Conversiones")
names_types = [archivo.stem for archivo in folder.iterdir() if archivo.suffix == ".py" and archivo.name != "__init__.py"]

#Creo ttk.style para combobox

#Creo combobox (lista de opciones) con los nombres de los tipos de conversiones.
combobox = ttk.Combobox(frame, values = names_types, state= "readonly")
combobox.pack(pady= 20)
combobox.set("Seleccione una Opcion")

#Creo boton para obtener la opcion seleccionada.
def on_select():
  if combobox.get() != "Seleccione una Opcion": 
    show_frame(combobox.get())

boton = ttk.Button(frame, text="Seleccionar", style="Custom.TButton", command=on_select)
boton.pack(pady=20)

# ==== Boton de Salida del programa ====
btn_salir = ttk.Button(frame, text="Salir", style="Custom.TButton", width=6, command=confirmar_salida)
btn_salir.pack(side="left", anchor="sw", padx=10, pady=10)

root.mainloop()