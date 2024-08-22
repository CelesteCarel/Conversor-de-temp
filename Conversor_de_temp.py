import tkinter as tk

def Fahrenheit_celsius():
    Fahrenheit = float(tbFahrenheit.get())
    Celsius = (Fahrenheit - 32) * 5 / 9
    tbCelsius.delete(0, tk.END)
    tbCelsius.insert(0, f"{Celsius:.2f}")

def Celsius_fahrenheit():
    Celsius = float(tbCelsius.get())
    Fahrenheit = (Celsius * 9 / 5) + 32
    tbFahrenheit.delete(0, tk.END)
    tbFahrenheit.insert(0, f"{Fahrenheit:.2f}")

def Limpiar():
    tbFahrenheit.delete(0, tk.END)
    tbCelsius.delete(0, tk.END)

ventana = tk.Tk()
ventana.title("Conversor de temperatura")

lbFahrenheit = tk.Label(ventana, text="Fahrenheit: ")
lbFahrenheit.grid(row=0, column=0)
tbFahrenheit = tk.Entry(ventana)
tbFahrenheit.grid(row=0, column=1)

btnFahrenheit = tk.Button(ventana, text="F a C", command=Fahrenheit_celsius)
btnFahrenheit.grid(row=0, column=2)

lbCelsius = tk.Label(ventana, text="Celsius: ")
lbCelsius.grid(row=1, column=0)
tbCelsius = tk.Entry(ventana)
tbCelsius.grid(row=1, column=1)

btnCelsius = tk.Button(ventana, text="C a F", command=Celsius_fahrenheit)
btnCelsius.grid(row=1, column=2)

btnLimpiar = tk.Button(ventana, text="Limpiar", command=Limpiar)
btnLimpiar.grid(row=2, column=1)

ventana.mainloop()
