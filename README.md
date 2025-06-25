# Conversor de Unidades

Aplicación de escritorio desarrollada en Python con interfaz gráfica usando Tkinter. Permite convertir entre distintas unidades de longitud, temperatura, sistemas numéricos y tamaño de archivos.

Es un proyecto práctico que demuestra habilidades en programación Python, diseño de interfaces con Tkinter, validación de entradas del usuario y empaquetado de aplicaciones para su distribución.

## 🚀 Funcionalidades

- Conversión de **longitudes**: metros, kilómetros, pies, pulgadas, etc.
- Conversión de **temperatura**: Celsius, Fahrenheit, Kelvin, Rankine, Réaumur.
- Conversión de **sistemas numéricos**: binario, decimal, hexadecimal, octal.
- Conversión de **tamaño de archivos**: Bytes, KB/MB/GB/TB (base 10) y KiB/MiB/GiB/TiB (base 2).
- Interfaz gráfica intuitiva y adaptativa.
- Soporte para tecla Enter como atajo para convertir.
- Estilos personalizados y diseño adaptable.
- Validación de entradas y manejo de errores.

## 🖼️ Capturas de pantalla

_Espacio reservado para agregar capturas o videos del programa funcionando._

## 🛠️ Tecnologías usadas

- [Python 3](https://www.python.org/)
- [Tkinter](https://docs.python.org/3/library/tkinter.html)
- [PyInstaller](https://pyinstaller.org/en/stable/)(Para generar el ejecutable del programa)

## 📦 Ejecutar el programa

- Si descargaste la versión compilada, seguí estos pasos:
  1. Abrí la carpeta `dist/`.
  2. Hacé doble clic en el archivo `ConversorDeUnidades.exe`.
  3. ¡Listo! El conversor se ejecutará sin necesidad de tener Python instalado.

⚠️ Si Windows muestra una advertencia de seguridad, podés confirmar que querés ejecutar el archivo.  
🧠 Asegurate de no mover el `.exe` fuera de la carpeta `dist/`, ya que puede necesitar archivos que están allí.

## 📁 Estructura del proyecto

```bash
ConversorUnidades/
├── Assets/
│   └── conversor_icon.ico
├── Conversiones/
│   ├── longitud.py
│   ├── tamaño_archivos.py
│   └── temperatura.py
├── dist/
│   └── ConversorDeUnidades.exe
├── Levels/
│   ├── file_size_level.py
│   ├── length_level.py
│   ├── number_system_level.py
│   └── temperature_level.py
├── main.py
├── README.md
