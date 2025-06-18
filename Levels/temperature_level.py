import tkinter as tk
from tkinter import ttk
from Conversiones import temperatura

def open_frame_temperature(root, frame, combobox):
  
  # Estilos personalizados
  style = ttk.Style()
  style.configure("Custom.TFrame", background="#6d7581")
  style.configure("Header.TLabel", background="#6d7581", foreground="#e5ebed", font=("Arial", 20, "bold italic"))
  style.configure("Custom.TLabel", background="#6d7581", font=("Arial", 12, "bold italic"))
  style.configure("Custom.TButton", font=("Arial", 12, "bold"), padding=6)

  # Frame Principal
  frame_temp = ttk.Frame(root, padding= 20, style="Custom.TFrame")
  frame_temp.pack(fill= "both", expand=True)

   # Configuración de columnas
  frame_temp.columnconfigure(0, weight=1)
  frame_temp.columnconfigure(1, weight=1)

  # Titulo 
  label_title = ttk.Label(frame_temp, text="Conversor de Temperatura", style="Header.TLabel")
  label_title.grid(row=0, column=0, columnspan=2, pady=(0, 20))

  # Lista de unidades
  units = ["°C (Celsius)", "°F (Fahrenheit)", "°K (Kelvin)", "°R (Rankine)", "°Ré (Réaumur)"]

  # Unidad inicial
  ttk.Label(frame_temp, text="Unidad Inicial", style="Custom.TLabel").grid(row=1, column=0, sticky="e", pady=5)
  cbb_input_unit = ttk.Combobox(frame_temp, values=units, state="readonly", width=30, font=("Arial", 12, "italic"), foreground="gray")
  cbb_input_unit.set("Seleccione una unidad")
  cbb_input_unit.grid(row=1, column=1, pady=5)

  # Unidad a convertir
  ttk.Label(frame_temp, text="Unidad a Convertir", style="Custom.TLabel").grid(row=2, column=0, sticky="e", pady=5)
  cbb_unit_convert = ttk.Combobox(frame_temp, values=units, state="readonly", width=30, font=("Arial", 12, "italic"), foreground="gray")
  cbb_unit_convert.set("Seleccione una unidad")
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
  ttk.Label(frame_temp, text="Valor a Convertir", style="Custom.TLabel").grid(row=3, column=0, sticky="e", pady=5)
  input_user = ttk.Entry(frame_temp, width=30, font=("Arial", 12, "italic"), foreground="gray")
  input_user.insert(0, "Ingrese el valor a convertir")
  input_user.bind("<FocusIn>", clear_placeholder)
  input_user.bind("<FocusOut>", add_placeholder)
  input_user.grid(row=3, column=1, pady=5)

  # Resultado
  label_resultado = ttk.Label(frame_temp, text="", font=("Arial", 12, "bold"), background="#6d7581")
  label_resultado.grid(row=5, column=0, columnspan=2, pady=15)

  # Funcion de Conversion
  def convertir(cbb_input_unit, cbb_unit_convert, input_user, label_resultado):
    unidad_inicial = cbb_input_unit.get()
    unidad_final = cbb_unit_convert.get()
    valor_str = input_user.get()

    if unidad_inicial == "Seleccione una Unidad" or unidad_final == "Seleccione una Unidad":
      label_resultado.config(text="Seleccione ambas Unidades")
      return
    
    if unidad_inicial == unidad_final:
      label_resultado.config(text= f"Resultado: {valor_str} {unidad_final}")
      return
    
    try:
      valor = float(valor_str)
    except ValueError:
      label_resultado.config(text="Por favor ingrese un número válido.")
      return
    
    #Diccionarios de posibles combinaciones de conversiones.
    conversions = {
      ("°C (Celsius)", "°F (Fahrenheit)"): temperatura.celsius_a_fahrenheit,
      ("°C (Celsius)", "°K (Kelvin)"): temperatura.celsius_a_kelvin,
      ("°C (Celsius)", "°R (Rankine)"): temperatura.celsius_a_rankine,
      ("°C (Celsius)", "°Ré (Réaumur)"): temperatura.celsius_a_reaumur,

      ("°F (Fahrenheit)", "°C (Celsius)"): temperatura.fahrenheit_a_celsius,
      ("°F (Fahrenheit)", "°K (Kelvin)"): temperatura.fahrenheit_a_kelvin,
      ("°F (Fahrenheit)", "°R (Rankine)"): temperatura.fahrenheit_a_rankine,
      ("°F (Fahrenheit)", "°Ré (Réaumur)"): temperatura.fahrenheit_a_reaumur,

      ("°K (Kelvin)", "°C (Celsius)"): temperatura.kelvin_a_celsius,
      ("°K (Kelvin)", "°F (Fahrenheit)"): temperatura.kelvin_a_fahrenheit,
      ("°K (Kelvin)", "°R (Rankine)"): temperatura.kelvin_a_rankine,
      ("°K (Kelvin)", "°Ré (Réaumur)"): temperatura.kelvin_a_reaumur,

      ("°R (Rankine)", "°C (Celsius)"): temperatura.rankine_a_celsius,
      ("°R (Rankine)", "°F (Fahrenheit)"): temperatura.rankine_a_fahrenheit,
      ("°R (Rankine)", "°K (Kelvin)"): temperatura.rankine_a_kelvin,
      ("°R (Rankine)", "°Ré (Réaumur)"): temperatura.rankine_a_reaumur,

      ("°Ré (Réaumur)", "°C (Celsius)"): temperatura.reaumur_a_celsius,
      ("°Ré (Réaumur)", "°F (Fahrenheit)"): temperatura.reaumur_a_fahrenheit,
      ("°Ré (Réaumur)", "°K (Kelvin)"): temperatura.reaumur_a_kelvin,
      ("°Ré (Réaumur)", "°R (Rankine)"): temperatura.reaumur_a_rankine
    }

    clave = (unidad_inicial, unidad_final)
    if clave in conversions:
      resultado = conversions[clave](valor)
      label_resultado.config(text=f"Resultado: {resultado} {unidad_final}")
    else:
      label_resultado.config(text="Conversión no disponible.")

  # Boton de conversion
  btn_convert = ttk.Button(frame_temp, text="CONVERTIR", style="Custom.TButton", command= lambda: convertir(cbb_input_unit, cbb_unit_convert, input_user, label_resultado))
  btn_convert.grid(row=4, column=0, columnspan=2, pady=15)

  # Boton Volver
  btn_back = ttk.Button(frame_temp, text="Volver", style="Custom.TButton", command= lambda: [frame_temp.destroy(), frame.pack(fill="x", expand=True), combobox.set("Seleccione una opcion")]) #Muestro el menu principal.
  btn_back.grid(row=6, column=0, sticky="w", padx=10, pady=(20, 0)) 