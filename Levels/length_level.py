import tkinter as tk
from tkinter import ttk

#Funcion para mostrar el frame.
def open_frame_length(root):
  #Creo el frame que va a contener la elección de las unidades a convertir.
  frame_length = ttk.Frame(root, padding=10, relief="flat")
  frame_length.pack(fill="x", expand=True)

  #Mensaje de bienvenida de la ventana.
  label_main = ttk.Label(frame_length, text="Conversor de Longitud", font=("Arial", 16, "bold italic"), foreground="#f4fce2", background="#f15500")
  label_main.pack(pady=10, expand=True)
