import tkinter as tk
from tkinter import messagebox

class Aplicacion:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.configure(bg="#7d2020")
        self.ventana.title("Inicio")
        self.ventana.geometry("500x500")
        self.ventana.iconbitmap("mano.ico")
        self.etiqueta = tk.Label(
            self.ventana,
            text="Ingresa tu nombre:",
            font="arial 20 bold"
        )
        self.etiqueta.pack(pady=20)

        self.entrada = tk.Entry(self.ventana)
        self.entrada.pack(pady=5)

        self.boton = tk.Button(
            self.ventana,
            text="Saludar",
            command=self.saludar
        )
        self.boton.pack(pady=10)

        self.resultado = tk.Label(
            self.ventana,
            text=""
        )
        self.resultado.pack(pady=5)

        self.imagen_original = tk.PhotoImage(file="mio.png")
        self.imagen = self.imagen_original.subsample(2,2)
        self.image = tk.Label(self.ventana, image=self.imagen)
        self.image.pack(pady=10)

    def saludar(self):
        nombre = self.entrada.get().strip()

        if nombre == "":
            messagebox.showwarning(
                "Aviso",
                "Debes ingresar tu nombre."
            )
        else:
            self.resultado.config(
                text=f"¡Hola, {nombre}!"
            )


ventana = tk.Tk()
app = Aplicacion(ventana)
ventana.mainloop()