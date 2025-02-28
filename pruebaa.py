import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Ejemplo con múltiples Frames")
root.geometry("300x200")

# Frame superior
frame_superior = ttk.Frame(root, padding=10, relief="ridge", borderwidth=2)
frame_superior.pack(fill="x", padx=10, pady=5)

ttk.Label(frame_superior, text="Frame Superior").pack()

# Frame central
frame_central = ttk.Frame(root, padding=10, relief="solid", borderwidth=2)
frame_central.pack(expand=True, fill="both", padx=10, pady=5)

ttk.Label(frame_central, text="Frame Central").pack()

# Frame inferior
frame_inferior = ttk.Frame(root, padding=10, relief="groove", borderwidth=2)
frame_inferior.pack(fill="x", padx=10, pady=5)

ttk.Label(frame_inferior, text="Frame Inferior").pack()

root.mainloop()
