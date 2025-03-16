import tkinter as tk
from tkinter import ttk

#Funcion que evalua y llama a la funcion necesaria para realizar la conversion de las unidades.
def convertir():
  pass

#Funcion para mostrar el frame.
def open_frame_length(root):
  #Creo el frame que va a contener la elección de las unidades a convertir.
  frame_length = ttk.Frame(root, padding=10, relief="flat")
  frame_length.pack(fill="x", expand=True)

  #Mensaje de bienvenida de la ventana.
  label_main = ttk.Label(frame_length, text="Conversor de Longitud", font=("Arial", 20, "bold italic"), foreground="#f4fce2", background="#f15500")
  label_main.pack(pady=10, expand=True)

  #Lista con los nombres de las unidades a elegir dentro de los combobox
  units = ["ft", "pulgadas", "milimetros", "centimetros", "metros", "kilometros"]

  #Creo combobox para la eleccion de la unidad inicial.
  ttk.Label(frame_length, text="Unidad Inicial", font=("Arial", 12,"italic")).pack(padx=20)
  cbb_input_unit = ttk.Combobox(frame_length, values= units, state= "readonly", width= 30, foreground= "gray")
  cbb_input_unit.pack(pady= 20, padx=20)
  cbb_input_unit.config(font=("Arial", 12, "italic"))
  cbb_input_unit.set("Seleccione una unidad")

  #Creo combobox para la eleccion de la unidad a convertir.
  ttk.Label(frame_length, text="Unidad a Convertir", font=("Arial", 12, "italic")).pack(padx=20)
  cbb_unit_convert = ttk.Combobox(frame_length, values= units, state= "readonly", width= 30, foreground="grey")
  cbb_unit_convert.pack(padx=20, pady=20)
  cbb_unit_convert.config(font= ("Arial", 12, "italic"))
  cbb_unit_convert.set("Seleccione una unidad")

  
  ##Funcion que borra el texto dentro del Entry.
  def clear_placeholder(event):
    if input_user.get() == "Ingrese el valor a convertir":
      input_user.delete(0, tk.END)
      input_user.config(foreground= "black")

  
  ##Funcion que muestra el texto dentro del Entry
  def add_placeholder(event):
    if not input_user.get():
      input_user.insert(0, "Ingrese el valor a convertir")
      input_user.config(foreground= "gray")

  #Creo un Entry para que el usuario ingrese el valor a convertir.
  input_user = ttk.Entry(frame_length, width=30, font= ("Arial", 12, "italic"), foreground= "gray")
  input_user.insert(0, "Ingrese el valor a convertir")
  input_user.bind("<FocusIn>", clear_placeholder)
  input_user.bind("<FocusOut>", add_placeholder)
  input_user.pack(pady= 20)

  #Creo boton para llamar a la funcion que realiza la conversion.
  button_convert = ttk.Button(frame_length, text="CONVERTIR", command= convertir())
  button_convert.pack(padx=20, pady=20)

  #Label que muestra el resultado de la conversion.