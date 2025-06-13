import tkinter as tk
from tkinter import ttk
from Conversiones import longitud

def open_frame_length(root):
    #Acciones Asociadas a Teclas
    root.bind('<Return>', lambda event: convertir(cbb_input_unit, cbb_unit_convert, input_user, label_resultado))

    # Estilos personalizados
    style = ttk.Style()
    style.configure("Custom.TFrame", background="#6d7581")
    style.configure("Header.TLabel", background="#6d7581", foreground="#e5ebed", font=("Arial", 20, "bold italic"))
    style.configure("Custom.TLabel", background="#6d7581", font=("Arial", 12, "bold italic"))
    style.configure("Custom.TButton", font=("Arial", 12, "bold"), padding=6)

    # Frame principal
    frame_length = ttk.Frame(root, padding=20, style="Custom.TFrame")
    frame_length.pack(fill="both", expand=True)

    # Configuración de columnas
    frame_length.columnconfigure(0, weight=1)
    frame_length.columnconfigure(1, weight=1)

    # Título
    label_main = ttk.Label(frame_length, text="Conversor de Longitud", style="Header.TLabel")
    label_main.grid(row=0, column=0, columnspan=2, pady=(0, 20))

    # Lista de unidades
    units = ["ft", "pulgadas", "milimetros", "centimetros", "metros", "kilometros"]

    # Unidad inicial
    ttk.Label(frame_length, text="Unidad Inicial", style="Custom.TLabel").grid(row=1, column=0, sticky="e", pady=5)
    cbb_input_unit = ttk.Combobox(frame_length, values=units, state="readonly", width=30, font=("Arial", 12, "italic"), foreground="gray")
    cbb_input_unit.set("Seleccione una unidad")
    cbb_input_unit.grid(row=1, column=1, pady=5)

    # Unidad a convertir
    ttk.Label(frame_length, text="Unidad a Convertir", style="Custom.TLabel").grid(row=2, column=0, sticky="e", pady=5)
    cbb_unit_convert = ttk.Combobox(frame_length, values=units, state="readonly", width=30, font=("Arial", 12, "italic"), foreground="gray")
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
    ttk.Label(frame_length, text="Valor a Convertir", style="Custom.TLabel").grid(row=3, column=0, sticky="e", pady=5)
    input_user = ttk.Entry(frame_length, width=30, font=("Arial", 12, "italic"), foreground="gray")
    input_user.insert(0, "Ingrese el valor a convertir")
    input_user.bind("<FocusIn>", clear_placeholder)
    input_user.bind("<FocusOut>", add_placeholder)
    input_user.grid(row=3, column=1, pady=5)

    # Resultado
    label_resultado = ttk.Label(frame_length, text="", font=("Arial", 12, "bold"), background="#6d7581")
    label_resultado.grid(row=5, column=0, columnspan=2, pady=15)

    # Función de conversión
    def convertir(cbb_input_unit, cbb_unit_convert, input_user, label_resultado):
        unidad_inicial = cbb_input_unit.get()
        unidad_final = cbb_unit_convert.get()
        valor_str = input_user.get()

        if unidad_inicial == "Seleccione una unidad" or unidad_final == "Seleccione una unidad":
            label_resultado.config(text="Selecciona ambas Unidades.")
            return

        if unidad_inicial == unidad_final:
            label_resultado.config(text=f"Resultado: {valor_str} {unidad_final}")
            return

        try:
            valor = float(valor_str)
        except ValueError:
            label_resultado.config(text="Por favor ingrese un número válido.")
            return

        convertions = {
            ("ft", "pulgadas"): longitud.ft_a_pulgadas,
            ("ft", "milimetros"): longitud.ft_a_milimetros,
            ("ft", "centimetros"): longitud.ft_a_centimetros,
            ("ft", "metros"): longitud.ft_a_metros,
            ("ft", "kilometros"): longitud.ft_a_kilometros,

            ("pulgadas", "ft"): longitud.pulgadas_a_ft,
            ("pulgadas", "milimetros"): longitud.pulgadas_a_milimetros,
            ("pulgadas", "centimetros"): longitud.pulgadas_a_centimetros,
            ("pulgadas", "metros"): longitud.pulgadas_a_metros,
            ("pulgadas", "kilometros"): longitud.pulgadas_a_kilometros,

            ("milimetros", "ft"): longitud.milimetros_a_ft,
            ("milimetros", "pulgadas"): longitud.milimetros_a_pulgadas,
            ("milimetros", "centimetros"): longitud.milimetros_a_centimetros,
            ("milimetros", "metros"): longitud.milimetros_a_metros,
            ("milimetros", "kilometros"): longitud.milimetros_a_kilometros,

            ("centimetros", "ft"): longitud.centimetros_a_ft,
            ("centimetros", "pulgadas"): longitud.centimetros_a_pulgadas,
            ("centimetros", "milimetros"): longitud.centimetros_a_milimetros,
            ("centimetros", "metros"): longitud.centimetros_a_metros,
            ("centimetros", "kilometros"): longitud.centimetros_a_kilometros,

            ("metros", "ft"): longitud.metros_a_ft,
            ("metros", "pulgadas"): longitud.metros_a_pulgadas,
            ("metros", "milimetros"): longitud.metros_a_milimetros,
            ("metros", "centimetros"): longitud.metros_a_centimetros,
            ("metros", "kilometros"): longitud.metros_a_kilometros,

            ("kilometros", "ft"): longitud.kilometros_a_ft,
            ("kilometros", "pulgadas"): longitud.kilometros_a_pulgadas,
            ("kilometros", "milimetros"): longitud.kilometros_a_milimetros,
            ("kilometros", "centimetros"): longitud.kilometros_a_centimetros,
            ("kilometros", "metros"): longitud.kilometros_a_metros,
        }

        clave = (unidad_inicial, unidad_final)
        if clave in convertions:
            resultado = convertions[clave](valor)
            label_resultado.config(text=f"Resultado: {resultado} {unidad_final}")
        else:
            label_resultado.config(text="Conversión no disponible.")

    # Botón de conversión
    button_convert = ttk.Button(frame_length, text="CONVERTIR", style="Custom.TButton", command=lambda: convertir(cbb_input_unit, cbb_unit_convert, input_user, label_resultado))
    button_convert.grid(row=4, column=0, columnspan=2, pady=15)

