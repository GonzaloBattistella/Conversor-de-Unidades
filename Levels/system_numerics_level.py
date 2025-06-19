import tkinter as tk
from tkinter import ttk

def open_frame_numerics_systems(root, frame_menu, combobox):
  #Acciones Asociadas a Teclas
  #root.bind('<Return>', lambda event: convertir(cbb_input_unit, cbb_unit_convert, input_user, label_resultado))

  # Estilos personalizados
  style = ttk.Style()
  style.configure("Custom.TFrame", background="#6d7581")
  style.configure("Header.TLabel", background="#6d7581", foreground="#e5ebed", font=("Arial", 20, "bold italic"))
  style.configure("Custom.TLabel", background="#6d7581", font=("Arial", 12, "bold italic"))
  style.configure("Custom.TButton", font=("Arial", 12, "bold"), padding=6)

  #Frame Principal
  frame_sysnum = ttk.Frame(root, padding=20, style="Custom.TFrame")
  frame_sysnum.pack(fill="both", expand=True)

  #Configuracion de Columnas
  frame_sysnum.columnconfigure(0, weight=1)
  frame_sysnum.columnconfigure(1, weight=1)

  #Titulo
  label_main = ttk.Label(frame_sysnum, text="Conversor de Sistemas Numericos", style="Header.TLabel")
  label_main.grid(row=0, column=0, columnspan=2, pady=(0, 20))

  #Lista de Unidades
  units = ["binario", "octal", "decimal", "hexadecimal"]

  #Unidad Inicial
  ttk.Label(frame_sysnum, text="Unidad Inicial", style="Custom.TLabel").grid(row=1, column=0, sticky="e", pady=5)
  cbb_input_unit = ttk.Combobox(frame_sysnum, values=units, state="readonly", width=30, font=("Arial", 12, "italic"), foreground="gray")
  cbb_input_unit.set("Seleccione una Unidad")
  cbb_input_unit.grid(row=1, column=1, pady=5)

  #Unidad a Convertir
  ttk.Label(frame_sysnum, text="Unidad a Convertir", style="Custom.TLabel").grid(row=2, column=0, sticky="e", pady=5)
  cbb_unit_convert = ttk.Combobox(frame_sysnum, values=units, state="readonly", width=30, font=("Arial", 12, "italic"), foreground="gray")
  cbb_unit_convert.set("Seleccione una Unidad")
  cbb_unit_convert.grid(row=2, column=1, pady=5)

  # Placeholder en el Entry
  def clear_placeholder(event):
    if input_user.get() == "Ingrese el valor a convertir":
      input_user.delete(0, tk.END)
      input_user.config(foreground="black")

  def add_placeholder(event):
    if not input_user.get():
      input_user.insert(0, "Ingrese el valor a convertir")
      input_user.config(foreground="gray")

  # Campo de entrada
  ttk.Label(frame_sysnum, text="Valor a Convertir", style="Custom.TLabel").grid(row=3, column=0, sticky="e", pady=5)
  input_user = ttk.Entry(frame_sysnum, width=30, font=("Arial", 12, "italic"), foreground="gray")
  input_user.insert(0, "Ingrese el valor a convertir")
  input_user.bind("<FocusIn>", clear_placeholder)
  input_user.bind("<FocusOut>", add_placeholder)
  input_user.grid(row=3, column=1, pady=5)

  #Resultado
  label_resultado = ttk.Label(frame_sysnum, text="", font=("Arial", 12, "bold"), background="#6d7581")
  label_resultado.grid(row=5, column=0, columnspan=2, pady=15)

  #Funcion de Conversion
  def convertir (cbb_input_unit, cbb_unit_convert, input_user, label_resultado):
    pass

  #Boton Convertir
  btn_convert = ttk.Button(frame_sysnum, text="CONVERTIR", style="Custom.TButton", command=lambda: convertir(cbb_input_unit, cbb_unit_convert, input_user, label_resultado))
  btn_convert.grid(row=4, column=0, columnspan=2, pady=15)

  #Boton Volver
  btn_back = ttk.Button(frame_sysnum, text="Volver", style="Custom.TButton", command=lambda: [frame_sysnum.destroy(), frame_menu.pack(fill="x", expand=True), combobox.set("Seleccione una Opción")])
  btn_back.grid(row=6, column=0, sticky="w", padx=10, pady=(20, 0)) #Se posiciona el boton en la esquina inferior izquierda.
