import tkinter as tk
from tkinter import ttk
from Conversiones import tamaño_archivos as ta

def open_frame_file_size(root, frame_menu, combobox, tamaño_original):
  #Acciones Asociadas a Teclas
  root.bind('<Return>', lambda event: convertir(cbb_input_unit, cbb_unit_convert, input_user, label_resultado))

  # Estilos personalizados
  style = ttk.Style()
  style.configure("Custom.TFrame", background="#6d7581")
  style.configure("Header.TLabel", background="#6d7581", foreground="#e5ebed", font=("Arial", 20, "bold italic"))
  style.configure("Custom.TLabel", background="#6d7581", font=("Arial", 12, "bold italic"))
  style.configure("Custom.TButton", font=("Arial", 12, "bold"), padding=6)

  #Configuro el tamaño del root
  root.geometry("600x450")

  # Frame Principal
  frame_size = ttk.Frame(root, padding= 20, style="Custom.TFrame")
  frame_size.pack(fill= "both", expand=True)

   # Configuración de columnas
  frame_size.columnconfigure(0, weight=1)
  frame_size.columnconfigure(1, weight=1)

  # Titulo 
  label_title = ttk.Label(frame_size, text="Conversor de Tamaño de Archivos", style="Header.TLabel")
  label_title.grid(row=0, column=0, columnspan=2, pady=(0, 20))

  #Lista de Unidades
  units = ["Bytes", "KB", "MB", "GB", "TB", "KiB", "MiB", "GiB", "TiB"]

  #Label aclaracion con diferencia entre base10 y base2
  label_aclaracion = ttk.Label(frame_size, 
    text="Aclaración: KB, MB, GB, TB usan base 10 (1 KB = 1000 B).\nKiB, MiB, GiB, TiB usan base 2 (1 KiB = 1024 B).", 
    font=("Arial", 9, "italic"),
    background="#6d7581",  # o el color de fondo que estés usando
    foreground="#e5ebed"   # o un gris claro que combine
  )

  label_aclaracion.grid(row=1, column=0, columnspan=2, pady=(5, 10))

  # Unidad inicial
  ttk.Label(frame_size, text="Unidad Inicial", style="Custom.TLabel").grid(row=2, column=0, sticky="e", pady=5)
  cbb_input_unit = ttk.Combobox(frame_size, values=units, state="readonly", width=30, font=("Arial", 12, "italic"), foreground="gray")
  cbb_input_unit.set("Seleccione una unidad")
  cbb_input_unit.grid(row=2, column=1, pady=5)

  # Unidad a convertir
  ttk.Label(frame_size, text="Unidad a Convertir", style="Custom.TLabel").grid(row=3, column=0, sticky="e", pady=5)
  cbb_unit_convert = ttk.Combobox(frame_size, values=units, state="readonly", width=30, font=("Arial", 12, "italic"), foreground="gray")
  cbb_unit_convert.set("Seleccione una unidad")
  cbb_unit_convert.grid(row=3, column=1, pady=5)

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
  ttk.Label(frame_size, text="Valor a Convertir", style="Custom.TLabel").grid(row=4, column=0, sticky="e", pady=5)
  input_user = ttk.Entry(frame_size, width=30, font=("Arial", 12, "italic"), foreground="gray")
  input_user.insert(0, "Ingrese el valor a convertir")
  input_user.bind("<FocusIn>", clear_placeholder)
  input_user.bind("<FocusOut>", add_placeholder)
  input_user.grid(row=4, column=1, pady=5)

  # Resultado
  label_resultado = ttk.Label(frame_size, text="", font=("Arial", 12, "bold"), background="#6d7581")
  label_resultado.grid(row=6, column=0, columnspan=2, pady=15)

  #Funcion de Conversion
  def convertir(cbb_input_unit, cbb_unit_convert, input_user, label_resultado):
    unidad_inicial = cbb_input_unit.get()
    unidad_final = cbb_unit_convert.get()
    valor_str = input_user.get()

    if unidad_inicial == "Seleccione una Opcion" or unidad_final == "Seleccione una Opcion":
      label_resultado.config(text="Seleccione Ambas Unidades.")
      return
    
    if unidad_inicial == unidad_final:
      label_resultado.config(text=f"Resultado: {valor_str} {unidad_final}")
      return
    
    try:
      valor = float(valor_str)
    except ValueError:
      label_resultado.config(text="Por favor Ingrese un número válido.")

    #Diccionario de posibles combinaciones de conversiones
    conversions = {
    # Base 10: Bytes, KB, MB, GB, TB
    ("Bytes", "KB"): ta.bytes_a_kb,
    ("KB", "Bytes"): ta.kb_a_bytes,
    ("KB", "MB"): ta.kb_a_mb,
    ("MB", "KB"): ta.mb_a_kb,
    ("MB", "GB"): ta.mb_a_gb,
    ("GB", "MB"): ta.gb_a_mb,
    ("GB", "TB"): ta.gb_a_tb,
    ("TB", "GB"): ta.tb_a_gb,
    ("KB", "GB"): ta.kb_a_gb,
    ("GB", "KB"): ta.gb_a_kb,
    ("MB", "TB"): ta.mb_a_tb,
    ("TB", "MB"): ta.tb_a_mb,
    ("KB", "TB"): ta.kb_a_tb,
    ("TB", "KB"): ta.tb_a_kb,
    ("Bytes", "MB"): ta.bytes_a_mb,
    ("MB", "Bytes"): ta.mb_a_bytes,
    ("Bytes", "GB"): ta.bytes_a_gb,
    ("GB", "Bytes"): ta.gb_a_bytes,
    ("Bytes", "TB"): ta.bytes_a_tb,
    ("TB", "Bytes"): ta.tb_a_bytes,

    # Base 2: Bytes, KiB, MiB, GiB, TiB
    ("Bytes", "KiB"): ta.bytes_a_kib,
    ("KiB", "Bytes"): ta.kib_a_bytes,
    ("KiB", "MiB"): ta.kib_a_mib,
    ("MiB", "KiB"): ta.mib_a_kib,
    ("MiB", "GiB"): ta.mib_a_gib,
    ("GiB", "MiB"): ta.gib_a_mib,
    ("GiB", "TiB"): ta.gib_a_tib,
    ("TiB", "GiB"): ta.tib_a_gib,
    ("KiB", "GiB"): ta.kib_a_gib,
    ("GiB", "KiB"): ta.gib_a_kib,
    ("MiB", "TiB"): ta.mib_a_tib,
    ("TiB", "MiB"): ta.tib_a_mib,
    ("KiB", "TiB"): ta.kib_a_tib,
    ("TiB", "KiB"): ta.tib_a_kib,
    ("Bytes", "MiB"): ta.bytes_a_mib,
    ("MiB", "Bytes"): ta.mib_a_bytes,
    ("Bytes", "GiB"): ta.bytes_a_gib,
    ("GiB", "Bytes"): ta.gib_a_bytes,
    ("Bytes", "TiB"): ta.bytes_a_tib,
    ("TiB", "Bytes"): ta.tib_a_bytes,

    # Cruzadas entre decimal y binario
    ("KB", "KiB"): ta.kb_a_kib,
    ("KiB", "KB"): ta.kib_a_kb,
    ("MB", "MiB"): ta.mb_a_mib,
    ("MiB", "MB"): ta.mib_a_mb,
    ("GB", "GiB"): ta.gb_a_gib,
    ("GiB", "GB"): ta.gib_a_gb,
    ("TB", "TiB"): ta.tb_a_tib,
    ("TiB", "TB"): ta.tib_a_tb,
    }

    clave = (unidad_inicial, unidad_final)
    if clave in conversions:
      resultado = conversions[clave](valor)
      
      # Formatear para evitar notación científica y ajustar decimales
      resultado_formateado = f"{resultado:.8f}".rstrip('0').rstrip('.')  # Esto quita ceros y punto si sobran
      label_resultado.config(text=f"Resultado: {resultado_formateado} {unidad_final}")
    else:
      label_resultado.config(text="Conversion No Disponible.")

  # Boton de conversion
  btn_convert = ttk.Button(frame_size, text="CONVERTIR", style="Custom.TButton", command= lambda: convertir(cbb_input_unit, cbb_unit_convert, input_user, label_resultado))
  btn_convert.grid(row=5, column=0, columnspan=2, pady=15)

  # Boton Volver
  btn_back = ttk.Button(frame_size, text="Volver", style="Custom.TButton",
  command=lambda: [
      frame_size.destroy(),
      frame_menu.pack(fill="x", expand=True),
      combobox.set("Seleccione una opcion"),
      root.geometry(tamaño_original)  # Restaurar tamaño original
  ]
  )

  btn_back.grid(row=7, column=0, sticky="w", padx=10, pady=(20, 0))
