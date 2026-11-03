# ==========================================
# INTERFAZ GRAFICA - SISTEMA RURAL-PE
# ==========================================
import tkinter as tk
from tkinter import ttk
from modelos import Paciente, Medico, CentroSalud, AreaAtencion
from gestor import GestorCitas

# Datos ficticios para las pruebas
pacientes = {
    "P001": Paciente("Ana Torres", "P001"),
    "P002": Paciente("Pedro Ruiz", "P002")
}

medicos = {
    "M001": Medico("Luis Perez", "M001", "Medicina General")
}

centro = CentroSalud(
    "Centro de Salud Rural Santa Rosa",
    "Av. Principal s/n",
    "Chugur"
)

area = AreaAtencion("A001", "Medicina General", 1, 1)

gestor = GestorCitas()
contador_citas = 1

# Crear la ventana principal
ventana = tk.Tk()

ventana.title("SistemaRural-PE - Gestion de Citas")
ventana.geometry("800x550")
ventana.resizable(False, False)

# Titulo principal
titulo = tk.Label(
    ventana,
    text="SISTEMA RURAL-PE",
    font=("Arial", 20, "bold")
)
titulo.pack(pady=15)

subtitulo = tk.Label(
    ventana,
    text="Centro de Salud Rural Santa Rosa - Chugur, Cajamarca",
    font=("Arial", 11)
)
subtitulo.pack()

# Crear un marco para organizar el contenido
marco = ttk.Frame(ventana, padding=20)
marco.pack(fill="both", expand=True)

# Mensaje de bienvenida
bienvenida = ttk.Label(
    marco,
    text="Sistema de Gestion de Citas Medicas",
    font=("Arial", 15, "bold")
)
bienvenida.pack(pady=20)

# Formulario para registrar una cita
formulario = ttk.LabelFrame(
    marco,
    text="Registro de citas",
    padding=15
)
formulario.pack(pady=10)

# Campo para el codigo del paciente
ttk.Label(formulario, text="Codigo del paciente:").grid(
    row=0, column=0, padx=10, pady=8, sticky="w"
)
entrada_paciente = ttk.Entry(formulario, width=25)
entrada_paciente.grid(row=0, column=1, padx=10, pady=8)

# Campo para el codigo del medico
ttk.Label(formulario, text="Codigo del medico:").grid(
    row=1, column=0, padx=10, pady=8, sticky="w"
)
entrada_medico = ttk.Entry(formulario, width=25)
entrada_medico.grid(row=1, column=1, padx=10, pady=8)

# Campo para la fecha
ttk.Label(formulario, text="Fecha (AAAA-MM-DD):").grid(
    row=2, column=0, padx=10, pady=8, sticky="w"
)
entrada_fecha = ttk.Entry(formulario, width=25)
entrada_fecha.grid(row=2, column=1, padx=10, pady=8)

# Campo para la hora de inicio
ttk.Label(formulario, text="Hora de inicio (HH:MM):").grid(
    row=3, column=0, padx=10, pady=8, sticky="w"
)
entrada_inicio = ttk.Entry(formulario, width=25)
entrada_inicio.grid(row=3, column=1, padx=10, pady=8)

# Campo para la hora final
ttk.Label(formulario, text="Hora final (HH:MM):").grid(
    row=4, column=0, padx=10, pady=8, sticky="w"
)
entrada_fin = ttk.Entry(formulario, width=25)
entrada_fin.grid(row=4, column=1, padx=10, pady=8)


# Funcion para registrar una cita desde la interfaz
def registrar_cita():
    global contador_citas

    try:
        codigo_paciente = entrada_paciente.get().strip()
        codigo_medico = entrada_medico.get().strip()
        fecha = entrada_fecha.get().strip()
        hora_inicio = entrada_inicio.get().strip()
        hora_fin = entrada_fin.get().strip()

        paciente = pacientes[codigo_paciente]
        medico = medicos[codigo_medico]

        codigo_cita = f"C{contador_citas:03d}"

        cita = gestor.registrar_cita(
            codigo_cita,
            paciente,
            medico,
            centro,
            area,
            fecha,
            hora_inicio,
            hora_fin
        )

        contador_citas += 1

        resultado.config(
            text=f"Cita {cita.codigo} registrada correctamente",
            foreground="green"
        )

    except KeyError:
        resultado.config(
            text="Codigo de paciente o medico no valido",
            foreground="red"
        )

    except ValueError as error:
        resultado.config(
            text=str(error),
            foreground="red"
        )

# Boton para registrar
boton_registrar = ttk.Button(
    formulario,
    text="Registrar cita",
    command=registrar_cita
)
boton_registrar.grid(
    row=5, column=0, columnspan=2, pady=15
)

# Mensaje del resultado
resultado = ttk.Label(formulario, text="")
resultado.grid(row=6, column=0, columnspan=2, pady=5)

# Boton inicial
boton_salir = ttk.Button(
    marco,
    text="Salir",
    command=ventana.destroy
)
boton_salir.pack(pady=15)

# Mantener la ventana abierta
ventana.mainloop()
